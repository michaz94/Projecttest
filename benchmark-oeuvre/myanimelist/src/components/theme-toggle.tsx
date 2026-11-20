"use client";

import { useEffect, useSyncExternalStore } from "react";

type Theme = "dark" | "light";

const COULEUR_BARRE: Record<Theme, string> = {
  dark: "#14110e",
  light: "#f1ebdd",
};

/** Le thème vit dans l'attribut `data-theme` de <html> : on s'y abonne. */
function subscribe(rappel: () => void) {
  const obs = new MutationObserver(rappel);
  obs.observe(document.documentElement, {
    attributes: true,
    attributeFilter: ["data-theme"],
  });
  return () => obs.disconnect();
}

const lire = (): Theme =>
  document.documentElement.dataset.theme === "light" ? "light" : "dark";
const lireServeur = (): Theme => "dark";

export function ThemeToggle({ etendu = false }: { etendu?: boolean }) {
  const theme = useSyncExternalStore(subscribe, lire, lireServeur);

  // Garde la couleur de la barre du navigateur en phase avec le thème.
  useEffect(() => {
    document
      .querySelector('meta[name="theme-color"]')
      ?.setAttribute("content", COULEUR_BARRE[theme]);
  }, [theme]);

  function basculer() {
    const suivant: Theme = theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = suivant;
    try {
      localStorage.setItem("theme", suivant);
    } catch {
      /* stockage indisponible : le choix vaut pour cette page seulement */
    }
  }

  const versClair = theme === "dark";
  const libelle = versClair ? "Passer en thème clair" : "Passer en thème sombre";

  return (
    <button
      type="button"
      onClick={basculer}
      aria-label={libelle}
      title={libelle}
      className={
        etendu
          ? "flex min-h-11 w-full items-center gap-3 rounded-lg px-3 text-sm text-zinc-400 transition-colors hover:bg-zinc-800/60 hover:text-zinc-100"
          : "inline-flex size-11 items-center justify-center rounded-lg text-zinc-400 transition-colors active:bg-zinc-800"
      }
    >
      <svg
        viewBox="0 0 24 24"
        className="size-5 shrink-0"
        fill="none"
        stroke="currentColor"
        strokeWidth={1.8}
        strokeLinecap="round"
        strokeLinejoin="round"
        aria-hidden
      >
        {versClair ? (
          <>
            <circle cx="12" cy="12" r="4" />
            <path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6 7 7M17 17l1.4 1.4M18.4 5.6 17 7M7 17l-1.4 1.4" />
          </>
        ) : (
          <path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z" />
        )}
      </svg>
      {etendu ? <span>{versClair ? "Thème clair" : "Thème sombre"}</span> : null}
    </button>
  );
}
