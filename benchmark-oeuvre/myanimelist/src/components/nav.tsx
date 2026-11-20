"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState, type ReactNode } from "react";

import { ThemeToggle } from "@/components/theme-toggle";

type Lien = { href: string; label: string; aide: string };

/** Organisation par intention, pas par ordre de création. */
const GROUPES: { titre: string; liens: Lien[] }[] = [
  {
    titre: "Projet",
    liens: [
      { href: "/", label: "Accueil", aide: "Cadrage et état" },
      { href: "/inspirations", label: "Inspirations", aide: "Références et pièges" },
      { href: "/decisions", label: "Décisions", aide: "Choisi, indéterminé…" },
      { href: "/ambiguites", label: "Ambiguïtés", aide: "Ce qui reste ouvert" },
    ],
  },
  {
    titre: "Étude",
    liens: [
      { href: "/catalogue", label: "Catalogue", aide: "2 951 œuvres MAL" },
      { href: "/constats", label: "Constats", aide: "Comptages mesurés" },
      { href: "/mecaniques", label: "Mécaniques", aide: "Genre à comprendre" },
      { href: "/corpus/cas", label: "Cas d'œuvres", aide: "Réussites et échecs" },
      { href: "/corpus/editeurs", label: "Éditeurs", aide: "À renseigner" },
      { href: "/corpus/segments", label: "Publics", aide: "Segments de lecteurs" },
    ],
  },
  {
    titre: "Méthode",
    liens: [
      { href: "/verifications", label: "Vérifications", aide: "Fact-check" },
      { href: "/documents", label: "Rapports", aide: "Portée de vos fichiers" },
      { href: "/api-mobile", label: "API", aide: "Accès externe" },
    ],
  },
];

const ONGLETS = ["/", "/catalogue", "/inspirations", "/decisions"] as const;

function Icone({ nom, className = "size-5" }: { nom: string; className?: string }) {
  const p = {
    className,
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    strokeWidth: 1.8,
    strokeLinecap: "round" as const,
    strokeLinejoin: "round" as const,
    "aria-hidden": true,
  };
  const formes: Record<string, ReactNode> = {
    "/": <path d="M4 11.5 12 5l8 6.5V19a1 1 0 0 1-1 1h-4v-5H9v5H5a1 1 0 0 1-1-1z" />,
    "/catalogue": (
      <>
        <rect x="4" y="4" width="7" height="7" rx="1" />
        <rect x="13" y="4" width="7" height="7" rx="1" />
        <rect x="4" y="13" width="7" height="7" rx="1" />
        <rect x="13" y="13" width="7" height="7" rx="1" />
      </>
    ),
    "/inspirations": <path d="m12 4 2.4 5 5.6.7-4.1 3.8 1.1 5.5L12 16.3 7 19l1.1-5.5L4 9.7 9.6 9z" />,
    "/decisions": (
      <>
        <circle cx="12" cy="12" r="8" />
        <path d="m8.5 12.3 2.4 2.4 4.6-5" />
      </>
    ),
    plus: (
      <>
        <circle cx="6" cy="12" r="1.2" />
        <circle cx="12" cy="12" r="1.2" />
        <circle cx="18" cy="12" r="1.2" />
      </>
    ),
    fermer: <path d="M6 6l12 12M18 6 6 18" />,
  };
  return <svg {...p}>{formes[nom]}</svg>;
}

export function Nav() {
  const pathname = usePathname();
  const [ouvert, setOuvert] = useState(false);

  const actif = (href: string) =>
    href === "/" ? pathname === "/" : pathname.startsWith(href);
  const courant = GROUPES.flatMap((g) => g.liens).find((l) => actif(l.href));
  const horsOnglets = !ONGLETS.some((o) => actif(o));

  const lienClasse = (a: boolean) =>
    `group flex items-center gap-3 rounded-lg px-3 py-2 text-sm transition-colors ${
      a
        ? "bg-zinc-100 font-semibold text-zinc-900"
        : "text-zinc-400 hover:bg-zinc-800/60 hover:text-zinc-100"
    }`;

  return (
    <>
      {/* ───── Mobile : barre supérieure ───── */}
      <header className="sticky top-0 z-30 flex h-12 items-center justify-between border-b border-zinc-800 bg-zinc-950/92 px-4 backdrop-blur lg:hidden">
        <Link href="/" className="flex items-center gap-2">
          <Marque />
          <span className="font-display text-base font-bold tracking-tight text-zinc-100">
            Atelier
          </span>
        </Link>
        <div className="flex items-center gap-1">
          {courant && courant.href !== "/" ? (
            <span className="font-mono text-[11px] tracking-wider text-zinc-500 uppercase">
              {courant.label}
            </span>
          ) : null}
          <ThemeToggle />
        </div>
      </header>

      {/* ───── Desktop : barre latérale ───── */}
      <aside className="fixed inset-y-0 left-0 z-30 hidden w-64 flex-col border-r border-zinc-800 bg-zinc-900/70 px-4 py-6 backdrop-blur lg:flex">
        <Link href="/" className="mb-8 flex items-center gap-2.5 px-2">
          <Marque grand />
          <span className="leading-tight">
            <span className="block font-display text-lg font-bold tracking-tight text-zinc-100">
              Atelier
            </span>
            <span className="block font-mono text-[10px] tracking-widest text-zinc-500 uppercase">
              projet shōnen
            </span>
          </span>
        </Link>
        <nav className="flex-1 space-y-6 overflow-y-auto">
          {GROUPES.map((g) => (
            <div key={g.titre}>
              <p className="mb-1.5 px-3 font-mono text-[10px] tracking-widest text-zinc-600 uppercase">
                {g.titre}
              </p>
              <ul className="space-y-0.5">
                {g.liens.map((l) => (
                  <li key={l.href}>
                    <Link
                      href={l.href}
                      aria-current={actif(l.href) ? "page" : undefined}
                      className={lienClasse(actif(l.href))}
                    >
                      <span
                        className={`size-1.5 rounded-full ${
                          actif(l.href) ? "bg-vermilion" : "bg-zinc-700"
                        }`}
                      />
                      {l.label}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </nav>
        <div className="border-t border-zinc-800 pt-3">
          <ThemeToggle etendu />
        </div>
      </aside>

      {/* ───── Mobile : barre d'onglets ───── */}
      <nav
        aria-label="Navigation principale"
        className="safe-bottom fixed inset-x-0 bottom-0 z-40 border-t border-zinc-700 bg-zinc-900/96 backdrop-blur lg:hidden"
      >
        <ul className="mx-auto grid max-w-lg grid-cols-5">
          {[
            { href: "/", label: "Accueil" },
            { href: "/catalogue", label: "Catalogue" },
            { href: "/inspirations", label: "Inspirations" },
            { href: "/decisions", label: "Décisions" },
          ].map((o) => {
            const a = actif(o.href);
            return (
              <li key={o.href}>
                <Link
                  href={o.href}
                  onClick={() => setOuvert(false)}
                  aria-current={a ? "page" : undefined}
                  className={`flex min-h-14 flex-col items-center justify-center gap-0.5 text-[10px] font-medium ${
                    a ? "text-zinc-100" : "text-zinc-500"
                  }`}
                >
                  <span
                    className={`flex h-7 w-12 items-center justify-center rounded-full transition-colors ${
                      a ? "bg-vermilion text-white" : ""
                    }`}
                  >
                    <Icone nom={o.href} />
                  </span>
                  {o.label}
                </Link>
              </li>
            );
          })}
          <li>
            <button
              type="button"
              onClick={() => setOuvert((v) => !v)}
              aria-expanded={ouvert}
              aria-controls="feuille-menu"
              className={`flex min-h-14 w-full flex-col items-center justify-center gap-0.5 text-[10px] font-medium ${
                ouvert || horsOnglets ? "text-zinc-100" : "text-zinc-500"
              }`}
            >
              <span
                className={`flex h-7 w-12 items-center justify-center rounded-full transition-colors ${
                  ouvert ? "bg-zinc-100 text-zinc-900" : horsOnglets ? "bg-zinc-800" : ""
                }`}
              >
                <Icone nom={ouvert ? "fermer" : "plus"} />
              </span>
              {horsOnglets && courant && !ouvert ? courant.label.slice(0, 11) : "Plus"}
            </button>
          </li>
        </ul>
      </nav>

      {/* ───── Mobile : feuille « Plus » ───── */}
      {ouvert ? (
        <div className="fixed inset-0 z-30 lg:hidden">
          <button
            type="button"
            aria-label="Fermer le menu"
            onClick={() => setOuvert(false)}
            className="absolute inset-0 bg-scrim backdrop-blur-[2px]"
          />
          <div
            id="feuille-menu"
            className="absolute inset-x-0 bottom-[calc(3.5rem+env(safe-area-inset-bottom))] max-h-[75vh] overflow-y-auto rounded-t-2xl border-x border-t-2 border-zinc-100 bg-zinc-900 px-4 pt-3 pb-4"
          >
            <div className="mx-auto mb-3 h-1 w-10 rounded-full bg-zinc-700" />
            {GROUPES.map((g) => (
              <section key={g.titre} className="mb-4">
                <p className="mb-1.5 font-mono text-[10px] tracking-widest text-zinc-600 uppercase">
                  {g.titre}
                </p>
                <ul className="grid grid-cols-2 gap-2">
                  {g.liens.map((l) => (
                    <li key={l.href}>
                      <Link
                        href={l.href}
                        onClick={() => setOuvert(false)}
                        aria-current={actif(l.href) ? "page" : undefined}
                        className={`block min-h-14 rounded-xl border px-3 py-2 ${
                          actif(l.href)
                            ? "border-zinc-100 bg-zinc-100 text-zinc-900"
                            : "border-zinc-800 bg-zinc-950/60 text-zinc-200 active:bg-zinc-800"
                        }`}
                      >
                        <span className="block text-sm font-semibold">{l.label}</span>
                        <span
                          className={`block text-[11px] ${
                            actif(l.href) ? "text-zinc-700" : "text-zinc-500"
                          }`}
                        >
                          {l.aide}
                        </span>
                      </Link>
                    </li>
                  ))}
                </ul>
              </section>
            ))}
          </div>
        </div>
      ) : null}
    </>
  );
}

/** Marque : carré d'encre, disque vermillon. */
function Marque({ grand = false }: { grand?: boolean }) {
  return (
    <span
      aria-hidden
      className={`relative inline-block rounded-md bg-zinc-100 ${
        grand ? "size-9" : "size-6"
      }`}
    >
      <span
        className={`absolute rounded-full bg-vermilion ${
          grand ? "top-1.5 left-1.5 size-5" : "top-1 left-1 size-3.5"
        }`}
      />
      <span
        className={`absolute rounded-full bg-zinc-900 ${
          grand ? "right-1.5 bottom-1.5 size-2" : "right-1 bottom-1 size-1.5"
        }`}
      />
    </span>
  );
}
