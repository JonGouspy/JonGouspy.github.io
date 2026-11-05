import { themes } from "../content";

// Decorative per-theme SVG (generated at export time from the Python builders).
export default function Deco({ theme, className }) {
  return <div className={className} aria-hidden="true" dangerouslySetInnerHTML={{ __html: themes[theme].svg }} />;
}
