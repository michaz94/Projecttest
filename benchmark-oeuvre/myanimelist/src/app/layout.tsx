import type { Metadata, Viewport } from "next";
import type { ReactNode } from "react";

import "@fontsource-variable/inter/index.css";
import "@fontsource-variable/bricolage-grotesque/index.css";
import "@fontsource-variable/jetbrains-mono/index.css";

import { Nav } from "@/components/nav";
import "./globals.css";

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover",
  themeColor: "#14110e",
  colorScheme: "dark light",
};

export const metadata: Metadata = {
  title: "Atelier — projet shōnen",
  description:
    "Atelier éditorial : corpus de recherche, décisions qualifiées, ambiguïtés ouvertes.",
};

/**
 * Exécuté avant le premier affichage : applique le thème mémorisé sans flash.
 * Sombre par défaut ; seul un choix explicite « clair » le remplace.
 */
const SCRIPT_THEME = `(function(){try{var t=localStorage.getItem("theme");document.documentElement.dataset.theme=t==="light"?"light":"dark";}catch(e){document.documentElement.dataset.theme="dark";}})();`;

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fr" data-theme="dark" suppressHydrationWarning>
      <head>
        <script dangerouslySetInnerHTML={{ __html: SCRIPT_THEME }} />
      </head>
      <body className="min-h-screen bg-zinc-950 text-zinc-200 antialiased">
        <Nav />
        <div className="lg:pl-64">
          <main className="mx-auto max-w-5xl px-4 pt-5 pb-28 sm:px-6 sm:pt-8 lg:pb-14">
            {children}
            <footer className="mt-14 border-t border-zinc-800 pt-4 text-[11px] leading-relaxed text-zinc-600">
              Aucun jugement automatique : les verdicts, scores et arbitrages affichés
              sont ceux que vous avez saisis. Les propositions de l&apos;outil sont
              toujours étiquetées comme telles.
            </footer>
          </main>
        </div>
      </body>
    </html>
  );
}
