import { useEffect, useState } from "react";
import { Link, useLocation } from "react-router-dom";
import { homePath, langNames, langs, projectPath, site, ui } from "../content";

const SunMoon = (
  <>
    <svg className="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.5" /><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8" /></svg>
    <svg className="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5Z" /></svg>
  </>
);

function useMode() {
  const [mode, setMode] = useState(() => document.documentElement.dataset.mode || "dark");
  const toggle = () => {
    const m = mode === "light" ? "dark" : "light";
    document.documentElement.dataset.mode = m;
    try { localStorage.setItem("mode", m); } catch {}
    setMode(m);
  };
  return toggle;
}

function Topbar({ lang, slug }) {
  const U = ui[lang];
  const toggleMode = useMode();
  const home = homePath(lang);
  const homeHash = (h) => ({ pathname: home, hash: h });
  return (
    <header className="topbar">
      <Link className="logo" to={home}><span className="logo-mark">JG</span><span className="logo-text">{site.name}</span></Link>
      <nav>
        <Link className="nl" to={homeHash("#projets")}>{U.nav_projects}</Link>
        <Link className="nl" to={homeHash("#apropos")}>{U.nav_about}</Link>
        <Link className="nl" to={homeHash("#contact")}>{U.nav_contact}</Link>
        <a className="btn-gh" href={site.github} target="_blank" rel="noopener noreferrer">GitHub ↗</a>
        <div className="lang-switch" role="group" aria-label={U.lang}>
          {langs.map((l) => (
            <Link key={l} to={slug ? projectPath(l, slug) : homePath(l)} hrefLang={l} lang={l} title={langNames[l]}
              className={l === lang ? "active" : undefined} aria-current={l === lang ? "true" : undefined}
              onClick={() => { try { localStorage.setItem("lang", l); } catch {} }}>
              {l.toUpperCase()}
            </Link>
          ))}
        </div>
        <button className="mode-toggle" type="button" aria-label={U.mode} title={U.mode} onClick={toggleMode}>{SunMoon}</button>
      </nav>
    </header>
  );
}

export default function Layout({ lang, slug, title, description, bodyClass, children }) {
  const { pathname } = useLocation();
  useEffect(() => {
    document.documentElement.lang = lang;
    document.title = title;
    document.querySelector('meta[name="description"]')?.setAttribute("content", description);
    document.body.className = bodyClass;
  }, [lang, title, description, bodyClass, pathname]);

  return (
    <>
      <Topbar lang={lang} slug={slug} />
      {children}
      <footer className="footer">
        <div className="wrap footer-in">
          <span>© 2026 {site.name}</span>
          <span className="mono dim">{ui[lang].footer}</span>
        </div>
      </footer>
    </>
  );
}
