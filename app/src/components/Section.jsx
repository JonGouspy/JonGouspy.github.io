export default function SectionTitle({ children }) {
  return <h2 className="h-sec"><span className="sec-mark"></span>{children}</h2>;
}

export const Tags = ({ items }) => (
  <div className="tags">{items.map((t) => <span className="tag" key={t}>{t}</span>)}</div>
);
