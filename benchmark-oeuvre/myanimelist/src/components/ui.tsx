import type { ReactNode } from "react";

/* Badge « tampon » : angles vifs, capitales espacées. */
export function Badge({
  children,
  classe,
  title,
}: {
  children: ReactNode;
  classe: string;
  title?: string;
}) {
  return (
    <span
      title={title}
      className={`inline-flex items-center rounded-[3px] px-1.5 py-0.5 font-mono text-[10px] leading-none font-semibold tracking-wider uppercase ring-1 ring-inset ${classe}`}
    >
      {children}
    </span>
  );
}

export function Card({
  children,
  className = "",
  dur = false,
}: {
  children: ReactNode;
  className?: string;
  /** Ombre dure façon case de manga, réservée aux éléments d'attention. */
  dur?: boolean;
}) {
  return (
    <div
      className={`rounded-lg border border-zinc-700 bg-zinc-900 p-4 sm:p-5 ${
        dur ? "panel-hard" : ""
      } ${className}`}
    >
      {children}
    </div>
  );
}

export function PageHeader({
  titre,
  chapo,
  precision,
  kicker,
}: {
  titre: string;
  chapo: string;
  precision?: string;
  kicker?: string;
}) {
  return (
    <header className="relative mb-7 sm:mb-9">
      <div className="halftone pointer-events-none absolute -top-2 right-0 h-28 w-48 opacity-40 sm:w-72" />
      <div className="relative">
        {kicker ? (
          <p className="mb-2 flex items-center gap-2 font-mono text-[11px] font-semibold tracking-[0.18em] text-vermilion uppercase">
            <span className="h-px w-5 bg-vermilion" />
            {kicker}
          </p>
        ) : null}
        <h1 className="text-[1.75rem] leading-[1.05] font-extrabold tracking-tight text-zinc-100 sm:text-4xl">
          {titre}
        </h1>
        <p className="mt-3 max-w-2xl text-[15px] leading-relaxed text-zinc-400">
          {chapo}
        </p>
        {precision ? (
          <aside className="mt-4 max-w-2xl rounded-r-md border-l-[3px] border-vermilion bg-zinc-900 px-3.5 py-2.5 text-xs leading-relaxed text-zinc-500">
            {precision}
          </aside>
        ) : null}
      </div>
    </header>
  );
}

const inputClass =
  "w-full min-h-11 rounded-md border border-zinc-700 bg-field px-3 py-2.5 text-base sm:text-sm text-zinc-100 placeholder:text-zinc-600 focus:border-zinc-100 focus:outline-none focus:ring-2 focus:ring-vermilion/30";

const labelClass =
  "mb-1 block font-mono text-[10px] font-semibold tracking-wider text-zinc-500 uppercase";

export function Field({
  label,
  name,
  defaultValue = "",
  placeholder,
  aide,
  required,
  wide,
}: {
  label: string;
  name: string;
  defaultValue?: string;
  placeholder?: string;
  aide?: string;
  required?: boolean;
  wide?: boolean;
}) {
  return (
    <label className={`block ${wide ? "sm:col-span-2" : ""}`}>
      <span className={labelClass}>
        {label}
        {required ? <span className="text-vermilion"> *</span> : null}
      </span>
      <input
        name={name}
        defaultValue={defaultValue}
        placeholder={placeholder}
        required={required}
        className={inputClass}
      />
      {aide ? <span className="mt-1 block text-[11px] text-zinc-600">{aide}</span> : null}
    </label>
  );
}

export function Area({
  label,
  name,
  defaultValue = "",
  placeholder,
  aide,
  rows = 3,
}: {
  label: string;
  name: string;
  defaultValue?: string;
  placeholder?: string;
  aide?: string;
  rows?: number;
}) {
  return (
    <label className="block sm:col-span-2">
      <span className={labelClass}>{label}</span>
      <textarea
        name={name}
        rows={rows}
        defaultValue={defaultValue}
        placeholder={placeholder}
        className={`${inputClass} leading-relaxed`}
      />
      {aide ? <span className="mt-1 block text-[11px] text-zinc-600">{aide}</span> : null}
    </label>
  );
}

export function Select({
  label,
  name,
  options,
  defaultValue,
  aide,
}: {
  label: string;
  name: string;
  options: { value: string; label: string }[];
  defaultValue?: string;
  aide?: string;
}) {
  return (
    <label className="block">
      <span className={labelClass}>{label}</span>
      <select name={name} defaultValue={defaultValue} className={inputClass}>
        {options.map((o) => (
          <option key={o.value} value={o.value}>
            {o.label}
          </option>
        ))}
      </select>
      {aide ? <span className="mt-1 block text-[11px] text-zinc-600">{aide}</span> : null}
    </label>
  );
}

export function Button({
  children,
  variant = "primary",
  type = "submit",
}: {
  children: ReactNode;
  variant?: "primary" | "ghost" | "danger";
  type?: "submit" | "button";
}) {
  const styles = {
    primary:
      "bg-zinc-100 text-zinc-900 shadow-[2px_2px_0_0_var(--color-vermilion)] hover:shadow-[3px_3px_0_0_var(--color-vermilion)]",
    ghost: "border border-zinc-700 bg-zinc-900 text-zinc-200 hover:border-zinc-100",
    danger: "border border-rose-400/60 bg-zinc-900 text-rose-300 hover:bg-rose-500/10",
  } as const;
  return (
    <button
      type={type}
      className={`inline-flex min-h-11 items-center justify-center rounded-md px-4 text-sm font-semibold transition-all active:translate-x-px active:translate-y-px ${styles[variant]}`}
    >
      {children}
    </button>
  );
}

export function Disclosure({
  summary,
  children,
  tone = "default",
}: {
  summary: string;
  children: ReactNode;
  tone?: "default" | "accent";
}) {
  return (
    <details
      className={`group rounded-lg border bg-zinc-900 ${
        tone === "accent" ? "border-zinc-100" : "border-zinc-700"
      }`}
    >
      <summary
        className={`flex min-h-12 cursor-pointer list-none items-center gap-2 px-4 py-3 text-sm font-semibold select-none ${
          tone === "accent" ? "text-zinc-100" : "text-zinc-400"
        } hover:text-zinc-100`}
      >
        <span className="inline-block text-vermilion transition-transform group-open:rotate-90">
          ›
        </span>
        {summary}
      </summary>
      <div className="border-t border-zinc-800 p-4">{children}</div>
    </details>
  );
}

/**
 * Accordéon sous lg, bloc statique à partir de lg.
 * `open` est un attribut HTML : on rend donc deux versions.
 */
export function Fold({
  titre,
  children,
  ouvert = false,
  className = "",
}: {
  titre: ReactNode;
  children: ReactNode;
  ouvert?: boolean;
  className?: string;
}) {
  const entete = "font-display text-sm font-bold text-zinc-100";
  return (
    <>
      <details
        open={ouvert}
        className={`group rounded-lg border border-zinc-700 bg-zinc-900 lg:hidden ${className}`}
      >
        <summary
          className={`flex min-h-12 cursor-pointer list-none items-center justify-between gap-2 px-4 select-none ${entete}`}
        >
          {titre}
          <span className="text-vermilion transition-transform group-open:rotate-90">›</span>
        </summary>
        <div className="px-4 pb-4">{children}</div>
      </details>
      <div
        className={`hidden rounded-lg border border-zinc-700 bg-zinc-900 p-5 lg:block ${className}`}
      >
        <h2 className={`mb-3 ${entete}`}>{titre}</h2>
        {children}
      </div>
    </>
  );
}

export function EmptyState({
  titre,
  children,
}: {
  titre: string;
  children: ReactNode;
}) {
  return (
    <div className="rounded-lg border-2 border-dashed border-zinc-700 bg-zinc-900/60 p-8 text-center">
      <p className="font-display text-base font-bold text-zinc-200">{titre}</p>
      <div className="mx-auto mt-2 max-w-md text-sm leading-relaxed text-zinc-500">
        {children}
      </div>
    </div>
  );
}

export function Prop({ label, value }: { label: string; value: string }) {
  if (!value) return null;
  return (
    <div className="mt-2.5">
      <dt className="font-mono text-[10px] font-semibold tracking-wider text-zinc-600 uppercase">
        {label}
      </dt>
      <dd className="mt-0.5 text-sm leading-relaxed whitespace-pre-line text-zinc-300">
        {value}
      </dd>
    </div>
  );
}

/** Pastille chiffrée pour les tuiles de synthèse. */
export function Stat({
  valeur,
  label,
  accent = false,
}: {
  valeur: ReactNode;
  label: string;
  accent?: boolean;
}) {
  return (
    <div
      className={`rounded-lg border bg-zinc-900 px-3.5 py-3 ${
        accent ? "panel-hard-accent border-zinc-100" : "border-zinc-700"
      }`}
    >
      <div className="font-display text-2xl leading-none font-extrabold tracking-tight text-zinc-100 tabular-nums">
        {valeur}
      </div>
      <div className="mt-1.5 text-[11px] leading-tight text-zinc-500">{label}</div>
    </div>
  );
}
