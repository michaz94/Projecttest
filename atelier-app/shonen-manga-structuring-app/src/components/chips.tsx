/**
 * Sélection multiple tactile.
 *
 * L'état visuel est piloté par CSS (`has-[:checked]`), pas par React :
 * la puce change de couleur au doigt, avant toute soumission du formulaire.
 * Une coloration issue du rendu serveur ne réagirait qu'après rechargement.
 */
export function Chips({
  name,
  options,
  selected,
  ton = "neutre",
  limite,
}: {
  name: string;
  options: { nom: string; n: number }[];
  selected: string[];
  ton?: "neutre" | "exclusion";
  limite?: number;
}) {
  const set = new Set(selected);
  const visibles = limite
    ? [
        ...options.filter((o) => set.has(o.nom)),
        ...options.filter((o) => !set.has(o.nom)).slice(0, limite),
      ]
    : options;
  const reste = options.length - visibles.length;

  const base =
    "inline-flex min-h-10 cursor-pointer items-center gap-1.5 rounded-full border px-3 text-xs transition-colors duration-100 select-none " +
    "border-zinc-700 bg-zinc-950/60 text-zinc-400 active:bg-zinc-800";
  const coche =
    ton === "exclusion"
      ? "has-[:checked]:border-rose-400 has-[:checked]:bg-rose-500/20 has-[:checked]:font-medium has-[:checked]:text-rose-200"
      : "has-[:checked]:border-sky-400 has-[:checked]:bg-sky-500/20 has-[:checked]:font-medium has-[:checked]:text-sky-200";
  // Anneau de focus au clavier, sans halo permanent à la souris
  const focus =
    "has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-sky-500/60 has-[:focus-visible]:ring-offset-1 has-[:focus-visible]:ring-offset-zinc-950";

  return (
    <div className="flex flex-wrap gap-1.5">
      {visibles.map((o) => (
        <label key={o.nom} className={`${base} ${coche} ${focus}`}>
          <input
            type="checkbox"
            name={name}
            value={o.nom}
            defaultChecked={set.has(o.nom)}
            className="peer sr-only"
          />
          {/* Marqueur visible uniquement une fois coché */}
          <span className="hidden peer-checked:inline">
            {ton === "exclusion" ? "−" : "✓"}
          </span>
          <span>{o.nom}</span>
          <span className="text-[10px] opacity-60">{o.n}</span>
        </label>
      ))}
      {reste > 0 ? (
        <span className="inline-flex min-h-10 items-center px-2 text-[11px] text-zinc-600">
          +{reste} autres
        </span>
      ) : null}
    </div>
  );
}

/** Choix exclusif tactile. Même principe : l'état actif vient du CSS. */
export function Segmented({
  name,
  options,
  value,
}: {
  name: string;
  options: { v: string; label: string }[];
  value: string;
}) {
  return (
    <div className="inline-flex overflow-hidden rounded-lg border border-zinc-700">
      {options.map((o) => (
        <label
          key={o.v}
          className={
            "flex min-h-9 cursor-pointer items-center px-3 text-xs transition-colors duration-100 select-none " +
            "bg-zinc-950/60 text-zinc-400 active:bg-zinc-800 " +
            "has-[:checked]:bg-zinc-100 has-[:checked]:font-medium has-[:checked]:text-zinc-900 " +
            "has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-sky-500/60 has-[:focus-visible]:ring-inset"
          }
        >
          <input
            type="radio"
            name={name}
            value={o.v}
            defaultChecked={value === o.v}
            className="sr-only"
          />
          {o.label}
        </label>
      ))}
    </div>
  );
}
