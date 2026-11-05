import { useEffect } from "react";
import { Navigate, Route, Routes, useLocation } from "react-router-dom";
import { langs, projDir } from "./content";
import Home from "./pages/Home.jsx";
import Project from "./pages/Project.jsx";

function ScrollManager() {
  const { pathname, hash } = useLocation();
  useEffect(() => {
    const el = hash && document.getElementById(hash.slice(1));
    if (el) el.scrollIntoView();
    else window.scrollTo(0, 0);
  }, [pathname, hash]);
  return null;
}

// The French home page redirects to the remembered language (same behaviour as the static site).
function FrHome() {
  let saved = null;
  try { saved = localStorage.getItem("lang"); } catch {}
  if (saved === "en" || saved === "eu") return <Navigate to={`/${saved}`} replace />;
  return <Home lang="fr" />;
}

export default function App() {
  return (
    <>
      <ScrollManager />
      <Routes>
        <Route path="/" element={<FrHome />} />
        {langs.map((l) => (
          <Route key={l} path={l === "fr" ? undefined : `/${l}`}>
            {l !== "fr" && <Route index element={<Home lang={l} />} />}
            <Route path={`${l === "fr" ? "/" : ""}${projDir[l]}/:slug`} element={<Project lang={l} />} />
          </Route>
        ))}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </>
  );
}
