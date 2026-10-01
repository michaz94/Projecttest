/* Atelier — service worker
   Objectif : l'app doit se lancer et rester utilisable sans réseau.
   - coquille de l'app : cache-first (elle ne change qu'au déploiement)
   - polices Google + images distantes : stale-while-revalidate, pour que
     le 2e lancement fonctionne hors-ligne même si tout n'est pas local.
   Les données de l'utilisateur ne passent PAS ici : elles vivent dans
   IndexedDB, qui est déjà hors-ligne par nature.                        */

const VERSION = "atelier-v6";
const SHELL = `${VERSION}-shell`;
const RUNTIME = `${VERSION}-runtime`;

const SHELL_FILES = [
  "./",
  "./index.html",
  "./manifest.json",
  "./icon.svg",
  "./icon-maskable.svg",
];

self.addEventListener("install", (e) => {
  e.waitUntil(
    caches
      .open(SHELL)
      .then((c) => Promise.allSettled(SHELL_FILES.map((f) => c.add(f))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (e) => {
  e.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((k) => k !== SHELL && k !== RUNTIME)
            .map((k) => caches.delete(k))
        )
      )
      .then(() => self.clients.claim())
  );
});

function isShell(url) {
  return (
    url.origin === self.location.origin &&
    (url.pathname.endsWith("/atelier/") ||
      url.pathname.endsWith("/index.html") ||
      url.pathname.endsWith("/manifest.json") ||
      url.pathname.endsWith(".svg"))
  );
}

function isRuntime(url) {
  return /(^|\.)(googleapis|gstatic|pexels|postimg)\.(com|cc)$/.test(url.hostname);
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;

  let url;
  try {
    url = new URL(request.url);
  } catch {
    return;
  }

  // Navigation : on sert l'app même hors-ligne.
  if (request.mode === "navigate") {
    event.respondWith(
      fetch(request)
        .then((r) => {
          const copy = r.clone();
          caches.open(SHELL).then((c) => c.put("./index.html", copy));
          return r;
        })
        .catch(() =>
          caches.match("./index.html").then((r) => r || Response.error())
        )
    );
    return;
  }

  if (isShell(url)) {
    event.respondWith(
      caches.match(request).then((hit) => hit || fetch(request))
    );
    return;
  }

  if (isRuntime(url)) {
    event.respondWith(
      caches.open(RUNTIME).then(async (cache) => {
        const hit = await cache.match(request);
        const net = fetch(request)
          .then((r) => {
            if (r && (r.ok || r.type === "opaque")) cache.put(request, r.clone());
            return r;
          })
          .catch(() => null);
        return hit || (await net) || Response.error();
      })
    );
  }
});
