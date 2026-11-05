import { useState } from "react";
import { Link } from "react-router-dom";
import Deco from "../components/Deco.jsx";
import Layout from "../components/Layout.jsx";
import SectionTitle, { Tags } from "../components/Section.jsx";
import { projectPath, projects, site, themeLabels, ui } from "../content";

export default function Home({ lang }) {
  const U = ui[lang];
  const list = projects[lang];
  const used = [...new Set(list.map((p) => p.theme))];
  const [filter, setFilter] = useState("all");

  return (
    <Layout lang={lang} title={`${site.name} — Portfolio`} description={U.site_desc} bodyClass="theme-home">
      <main>
        <section className="hero wrap">
          <p className="eyebrow mono"><span className="pulse"></span> Portfolio · 2026</p>
          <h1>{U.hero_a}<br /><span className="accent">{U.hero_b}</span></h1>
          <p className="lead">{U.hero_lead.replace("{name}", site.name)}</p>
          <div className="actions">
            <a className="btn" href="#projets">{U.btn_projects}</a>
            <a className="btn ghost" href={site.github} target="_blank" rel="noopener noreferrer">GitHub ↗</a>
          </div>
          <div className="stack mono">
            {["C", "C++", "CUDA", "VHDL", "ESP-IDF", "KiCad"].map((s) => <span key={s}>{s}</span>)}
          </div>
        </section>

        <section id="projets" className="wrap section">
          <div className="sec-head">
            <SectionTitle>{U.nav_projects}</SectionTitle>
            <div className="filters">
              <button className={`chip${filter === "all" ? " active" : ""}`} onClick={() => setFilter("all")}>{U.filter_all}</button>
              {used.map((t) => (
                <button key={t} className={`chip theme-${t}${filter === t ? " active" : ""}`} onClick={() => setFilter(t)}>
                  <i></i>{themeLabels[t][lang]}
                </button>
              ))}
            </div>
          </div>
          <div className="grid">
            {list.map((p) => (
              <Link key={p.slug} className={`card theme-${p.theme}`} to={projectPath(lang, p.slug)}
                hidden={filter !== "all" && p.theme !== filter}>
                <Deco theme={p.theme} className="card-deco" />
                <div className="card-top"><span className="theme-badge">{themeLabels[p.theme][lang]}</span><span className="mono dim">{p.num}</span></div>
                <h3>{p.title}</h3>
                <p>{p.tagline}</p>
                <Tags items={p.tags.slice(0, 4)} />
                <span className="card-go mono">{U.discover}</span>
              </Link>
            ))}
          </div>
        </section>

        <section id="apropos" className="wrap section">
          <SectionTitle>{U.nav_about}</SectionTitle>
          <div className="about">
            <div className="prose">{U.about.map((t) => <p key={t}>{t}</p>)}</div>
            <div className="skills">
              {U.skills.map(([title, items]) => (
                <div className="skill" key={title}>
                  <h3 className="mono">{title}</h3>
                  <ul>{items.map((x) => <li key={x}>{x}</li>)}</ul>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section id="contact" className="wrap section contact">
          <h2>{U.contact_h}</h2>
          <p className="dim">{U.contact_p}</p>
          <div className="actions center">
            <a className="btn" href={`mailto:${site.email}`}>{site.email}</a>
            <a className="btn ghost" href={site.github} target="_blank" rel="noopener noreferrer">GitHub ↗</a>
            <a className="btn ghost" href={site.linkedin} target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
          </div>
        </section>
      </main>
    </Layout>
  );
}
