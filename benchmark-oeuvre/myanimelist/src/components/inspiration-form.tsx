import { Area, Button, Field, Select } from "@/components/ui";
import type { Inspiration } from "@/db/schema";
import { STATUT_INSPIRATION, STATUTS_INSPIRATION } from "@/lib/labels";
import { upsertInspiration } from "@/app/actions";

const optionsStatut = STATUTS_INSPIRATION.map((s) => ({
  value: s,
  label: STATUT_INSPIRATION[s].label,
}));

/** Formulaire partagé par la création et la modification. */
export function InspirationForm({ i }: { i?: Inspiration }) {
  return (
    <form action={upsertInspiration} className="grid gap-4 sm:grid-cols-2">
      {i ? <input type="hidden" name="id" value={i.id} /> : null}
      <Field label="Nom" name="nom" defaultValue={i?.nom ?? ""} required />
      <Field
        label="Catégorie"
        name="categorie"
        defaultValue={i?.categorie ?? ""}
        placeholder="Worldbuilding · Folklore · Esthétique…"
      />
      <Select
        label="Statut"
        name="statut"
        options={optionsStatut}
        defaultValue={i?.statut ?? "reference"}
        aide="« Référence » par défaut : aimer une source ne l'intègre pas à l'œuvre."
      />
      <Field
        label="Média d'origine"
        name="medium"
        defaultValue={i?.medium ?? ""}
        placeholder="Manga · Roman · Web serial · Jeu vidéo…"
      />
      <Field
        label="Économie de publication"
        name="economie"
        defaultValue={i?.economie ?? ""}
        placeholder="Et son écart avec la vôtre"
        wide
      />
      <Area
        label="Ce que vous en dites"
        name="ceQueVousEnDites"
        defaultValue={i?.ceQueVousEnDites ?? ""}
        rows={4}
      />
      <Area
        label="Pièges d'interprétation"
        name="piegesInterpretation"
        defaultValue={i?.piegesInterpretation ?? ""}
        rows={4}
        aide="Les glissements à ne pas commettre à partir de cette référence : par l'outil, par une autre IA, ou par vous dans six mois."
      />
      <Area
        label="Ce qui reste ouvert"
        name="resteOuvert"
        defaultValue={i?.resteOuvert ?? ""}
        rows={3}
      />
      <div className="sm:col-span-2">
        <Button>{i ? "Enregistrer les modifications" : "Ajouter l'inspiration"}</Button>
      </div>
    </form>
  );
}
