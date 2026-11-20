"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const LIENS = [
  { href: "/", label: "Tableau de bord", court: "Accueil" },
  { href: "/catalogue", label: "Catalogue", court: "Catalogue" },
  { href: "/inspirations", label: "Inspirations", court: "Inspirations" },
  { href: "/mecaniques", label: "Mécaniques", court: "Mécaniques" },
  { href: "/decisions", label: "Décisions", court: "Décisions" },
  { href: "/ambiguites", label: "Ambiguïtés", court: "Ambiguïtés" },
  { href: "/constats", label: "Constats", court: "Constats" },
  { href: "/verifications", label: "Vérifications", court: "Vérifs" },
  { href: "/documents", label: "Rapports", court: "Rapports" },
  { href: "/corpus/editeurs", label: "Éditeurs", court: "Éditeurs" },
  { href: "/corpus/cas", label: "Cas d'œuvres", court: "Cas" },
  { href: "/corpus/segments", label: "Publics", court: "Publics" },
  { href: "/api-mobile", label: "API mobile", court: "API" },
];

export function Nav() {
  const pathname = usePathname();
  const actifDe = (href: string) =>
    href === "/" ? pathname === "/" : pathname.startsWith(href);
  const courant = LIENS.find((l) => actifDe(l.href));

  return (
    <nav className="sticky top-0 z-20 border-b border-zinc-800 bg-zinc-950/95 backdrop-blur">
      <div className="mx-auto max-w-6xl px-4 sm:px-6">
        {/* Titre + page courante : visible seulement sur petit écran */}
        <div className="flex items-baseline gap-2 pt-2 sm:hidden">
          <Link href="/" className="text-sm font-semibold text-zinc-100">
            Atelier
          </Link>
          {courant ? (
            <span className="truncate text-xs text-zinc-500">
              / {courant.label}
            </span>
          ) : null}
        </div>

        <div className="flex items-center gap-3">
          <Link
            href="/"
            className="hidden shrink-0 py-3 text-sm font-semibold tracking-tight text-zinc-100 sm:block"
          >
            Atelier éditorial
          </Link>

          {/* Onglets : défilement horizontal au doigt, pas de retour à la ligne */}
          <div className="scroll-x -mx-1 flex-1">
            <ul className="flex w-max gap-1 px-1 py-2">
              {LIENS.map((lien) => {
                const actif = actifDe(lien.href);
                return (
                  <li key={lien.href}>
                    <Link
                      href={lien.href}
                      aria-current={actif ? "page" : undefined}
                      className={`flex min-h-11 items-center rounded-lg px-3 text-xs whitespace-nowrap transition ${
                        actif
                          ? "bg-zinc-100 font-medium text-zinc-900"
                          : "text-zinc-400 active:bg-zinc-800 sm:hover:bg-zinc-900 sm:hover:text-zinc-200"
                      }`}
                    >
                      <span className="sm:hidden">{lien.court}</span>
                      <span className="hidden sm:inline">{lien.label}</span>
                    </Link>
                  </li>
                );
              })}
            </ul>
          </div>
        </div>
      </div>
    </nav>
  );
}
