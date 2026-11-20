/**
 * Sélection multiple tactile.
 * L'état visuel est piloté par CSS (`has-[:checked]`) : la puce réagit au doigt,
 * avant toute soumission du formulaire.
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
    "inline-flex min-h-10 cursor-pointer items-center gap-1.5 rounded-md border px-3 text-[13px] transition-colors duration-100 select-none " +
    "border-zinc-700 bg-field text-zinc-400 active:bg-zinc-800";
  const coche =
    ton === "exclusion"
      ? "has-[:checked]:border-rose-400 has-[:checked]:bg-rose-500 has-[:checked]:font-semibold has-[:checked]:text-white"
      : "has-[:checked]:border-zinc-100 has-[:checked]:bg-zinc-100 has-[:checked]:font-semibold has-[:checked]:text-zinc-900";
  const focus =
    "has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-vermilion has-[:focus-visible]:ring-offset-1 has-[:focus-visible]:ring-offset-zinc-950";

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
          <span className="hidden peer-checked:inline">
            {ton === "exclusion" ? "−" : "✓"}
          </span>
          <span>{o.nom}</span>
          <span className="font-mono text-[10px] opacity-60">{o.n}</span>
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

/** Choix exclusif tactile. */
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
    <div className="inline-flex overflow-hidden rounded-md border border-zinc-100">
      {options.map((o) => (
        <label
          key={o.v}
          className={
            "flex min-h-9 cursor-pointer items-center px-3 text-xs font-medium transition-colors duration-100 select-none " +
            "bg-field text-zinc-400 active:bg-zinc-800 " +
            "has-[:checked]:bg-zinc-100 has-[:checked]:font-semibold has-[:checked]:text-zinc-900 " +
            "has-[:focus-visible]:ring-2 has-[:focus-visible]:ring-vermilion has-[:focus-visible]:ring-inset"
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
