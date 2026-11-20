import type { ReactNode } from "react";

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
      className={`inline-flex items-center rounded-full px-2 py-0.5 text-[11px] font-medium uppercase tracking-wide ring-1 ring-inset ${classe}`}
    >
      {children}
    </span>
  );
}

export function Card({
  children,
  className = "",
}: {
  children: ReactNode;
  className?: string;
}) {
  return (
    <div
      className={`rounded-xl border border-zinc-800 bg-zinc-900/60 p-4 sm:p-5 ${className}`}
    >
      {children}
    </div>
  );
}

export function PageHeader({
  titre,
  chapo,
  precision,
}: {
  titre: string;
  chapo: string;
  precision?: string;
}) {
  return (
    <header className="mb-6 border-b border-zinc-800 pb-5 sm:mb-8 sm:pb-6">
      <h1 className="text-xl font-semibold tracking-tight text-zinc-50 sm:text-2xl">
        {titre}
      </h1>
      <p className="mt-2 max-w-3xl text-sm leading-relaxed text-zinc-400">
        {chapo}
      </p>
      {precision ? (
        <p className="mt-3 max-w-3xl rounded-lg border border-zinc-800 bg-zinc-900/60 px-3 py-2 text-xs leading-relaxed text-zinc-500">
          {precision}
        </p>
      ) : null}
    </header>
  );
}

const inputClass =
  "w-full min-h-11 rounded-lg border border-zinc-700 bg-zinc-950/70 px-3 py-2.5 text-base sm:text-sm text-zinc-100 placeholder:text-zinc-600 focus:border-zinc-500 focus:outline-none focus:ring-2 focus:ring-sky-500/40";

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
      <span className="mb-1 block text-xs font-medium text-zinc-400">
        {label}
        {required ? <span className="text-rose-400"> *</span> : null}
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
      <span className="mb-1 block text-xs font-medium text-zinc-400">{label}</span>
      <textarea
        name={name}
        rows={rows}
        defaultValue={defaultValue}
        placeholder={placeholder}
        className={inputClass}
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
      <span className="mb-1 block text-xs font-medium text-zinc-400">{label}</span>
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
    primary: "bg-zinc-100 text-zinc-900 hover:bg-white",
    ghost: "border border-zinc-700 text-zinc-300 hover:bg-zinc-800",
    danger: "border border-rose-900/60 text-rose-300 hover:bg-rose-950/40",
  } as const;
  return (
    <button
      type={type}
      className={`inline-flex min-h-11 items-center justify-center rounded-lg px-4 text-sm font-medium transition active:scale-[0.98] ${styles[variant]}`}
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
    <details className="group rounded-xl border border-zinc-800 bg-zinc-900/40">
      <summary
        className={`flex min-h-12 cursor-pointer list-none items-center px-4 py-3 text-sm font-medium select-none ${
          tone === "accent" ? "text-zinc-100" : "text-zinc-400"
        } hover:text-zinc-100`}
      >
        <span className="mr-2 inline-block transition group-open:rotate-90">›</span>
        {summary}
      </summary>
      <div className="border-t border-zinc-800 p-4">{children}</div>
    </details>
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
    <div className="rounded-xl border border-dashed border-zinc-800 bg-zinc-900/30 p-8 text-center">
      <p className="text-sm font-medium text-zinc-300">{titre}</p>
      <div className="mx-auto mt-2 max-w-md text-xs leading-relaxed text-zinc-500">
        {children}
      </div>
    </div>
  );
}

export function Prop({ label, value }: { label: string; value: string }) {
  if (!value) return null;
  return (
    <div className="mt-2">
      <dt className="text-[11px] font-medium uppercase tracking-wide text-zinc-600">
        {label}
      </dt>
      <dd className="mt-0.5 text-sm whitespace-pre-line text-zinc-300">{value}</dd>
    </div>
  );
}
