import { useLayoutEffect, useRef, useState } from "react";
import { Link, Navigate, useParams } from "react-router-dom";
import Deco from "../components/Deco.jsx";
import Layout from "../components/Layout.jsx";
import SectionTitle, { Tags } from "../components/Section.jsx";
import { homePath, projectPath, projects, site, themeLabels, ui } from "../content";

// Context text with an image on its right, scaled to twice the height of the text block.
function ContextWithImage({ html, image, alt }) {
  const textRef = useRef(null);
  const [h, setH] = useState(null);
  useLayoutEffect(() => {
    const el = textRef.current;
    const ro = new ResizeObserver(() => setH(el.offsetHeight));
    ro.observe(el);
    return () => ro.disconnect();
  }, []);
  return (
    <div className="context-grid">
      <div ref={textRef} className="prose" dangerouslySetInnerHTML={{ __html: html }} />
      <figure className="media portrait" style={{ "--h": h ? `${h * 2}px` : "auto" }}>
        <img src={image} alt={alt} width="179" height="440" loading="lazy" />
      </figure>
    </div>
  );
}

export default function Project({ lang }) {
  const { slug } = useParams();
  const list = projects[lang];
  const i = list.findIndex((p) => p.slug === slug);
  if (i < 0) return <Navigate to={homePath(lang)} replace />;

  const U = ui[lang];
  const p = list[i];
  const prev = list[(i - 1 + list.length) % list.length];
  const next = list[(i + 1) % list.length];

  return (
    <Layout lang={lang} slug={slug} title={`${p.title} — ${site.name}`} description={p.tagline} bodyClass={`theme-${p.theme}`}>
      <main>
        <section className="p-hero wrap">
          <Link className="back mono" to={{ pathname: homePath(lang), hash: "#projets" }}>{U.back}</Link>
          <div className="p-hero-grid">
            <div className="p-hero-main">
              <p className="eyebrow"><span className="theme-badge">{themeLabels[p.theme][lang]}</span><span className="mono dim">{p.num} / {p.domain}</span></p>
              <h1>{p.title}</h1>
              <p className="lead">{p.tagline}</p>
              <Tags items={p.tags} />
              <div className="actions">
                <a className="btn" href={p.repo ?? `${site.github}/${p.slug}`} target="_blank" rel="noopener noreferrer">{U.view_code}</a>
              </div>
            </div>
            <div className="p-hero-side">
              <Deco theme={p.theme} className="deco" />
              <dl className="facts">
                {p.facts.map(([k, v]) => <div className="fact" key={k}><dt>{k}</dt><dd>{v}</dd></div>)}
              </dl>
            </div>
          </div>
        </section>

        <section className="wrap section">
          <SectionTitle>{U.s_context}</SectionTitle>
          {p.image ? (
            <ContextWithImage html={p.context} image={p.image} alt={p.title} />
          ) : (
            <div className="prose" dangerouslySetInnerHTML={{ __html: p.context }} />
          )}
        </section>

        <section className="wrap section">
          <SectionTitle>{U.s_arch}</SectionTitle>
          <ol className="pipeline">
            {p.pipeline.map((s, k) => <li key={s}><span className="step-n">{String(k + 1).padStart(2, "0")}</span>{s}</li>)}
          </ol>
          <p className="caption">{p.pipeline_caption}</p>
        </section>

        <section className="wrap section">
          <SectionTitle>{U.s_points}</SectionTitle>
          <div className="points">
            {p.points.map(([t, d]) => <div className="point" key={t}><h3>{t}</h3><p>{d}</p></div>)}
          </div>
        </section>

        <section className="wrap section">
          <SectionTitle>{U.s_code}</SectionTitle>
          <div className="code">
            <div className="code-bar mono"><span className="dots"><i></i><i></i><i></i></span>{p.code_lang}</div>
            <pre><code>{p.code}</code></pre>
          </div>
        </section>

        <section className="wrap section">
          <SectionTitle>{U.s_learned}</SectionTitle>
          <ul className="learned">{p.learned.map((l) => <li key={l}>{l}</li>)}</ul>
        </section>

        <nav className="wrap pager">
          <Link className={`theme-${prev.theme}`} to={projectPath(lang, prev.slug)}><span className="mono dim">{U.prev}</span><strong>{prev.title}</strong></Link>
          <Link className={`next theme-${next.theme}`} to={projectPath(lang, next.slug)}><span className="mono dim">{U.next}</span><strong>{next.title}</strong></Link>
        </nav>
      </main>
    </Layout>
  );
}
