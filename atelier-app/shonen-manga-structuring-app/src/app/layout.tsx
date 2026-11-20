import type { Metadata } from "next";
import type { ReactNode } from "react";

import { Nav } from "@/components/nav";
import "./globals.css";

export const viewport = {
  width: "device-width",
  initialScale: 1,
  viewportFit: "cover" as const,
};

export const metadata: Metadata = {
  title: "Atelier éditorial — projet shonen",
  description:
    "Couche éditoriale complémentaire d'un outil de structuration : corpus de recherche, décisions qualifiées, ambiguïtés ouvertes.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="fr">
      <body className="min-h-screen bg-zinc-950 text-zinc-200 antialiased">
        <Nav />
        <main className="mx-auto max-w-6xl px-4 py-6 sm:px-6 sm:py-10">{children}</main>
        <footer className="safe-bottom mx-auto max-w-6xl px-4 pb-10 text-[11px] leading-relaxed text-zinc-600 sm:px-6">
          Cet outil ne produit aucun jugement automatique. Les verdicts, scores et
          arbitrages affichés sont ceux que vous avez saisis.
        </footer>
      </body>
    </html>
  );
}
