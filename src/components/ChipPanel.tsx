import { useEffect } from 'react';
import type { PanelGroup, RefCell } from '../types';

interface Props {
  /** Which ref table this panel belongs to (rules | ladder). */
  table: string;
  title: string;
  /** Shown on phones until an answer has been given. */
  hint: string;
  groups: PanelGroup[];
  /** Item to highlight after an answer has been given (null = nothing highlighted). */
  highlight?: RefCell | null;
}

/**
 * Reference list: groups of chips (sound-shift rules, collocation partners, upgrade ladders).
 * Desktop: the whole list, the answered item is highlighted and explained.
 * Phone: only the group of the answered item (the full list would not fit), a hint before answering.
 */
export default function ChipPanel({ table, title, hint, groups, highlight = null }: Props) {
  const hl = highlight?.table === table ? highlight : null;

  // keep the highlighted chip in view in the (scrollable) desktop sidebar
  useEffect(() => {
    const box = document.querySelector('.sidebar');
    if (!(box instanceof HTMLElement)) return;
    const el = [...box.querySelectorAll('.chunk-verb.hl')].find((c) => (c as HTMLElement).offsetParent !== null);
    let top = 0;
    if (el) {
      const b = box.getBoundingClientRect();
      const c = el.getBoundingClientRect();
      top = Math.max(0, box.scrollTop + (c.top - b.top) - box.clientHeight / 2 + c.height / 2);
    }
    box.scrollTo({ top, behavior: 'smooth' });
  }, [highlight]);

  return (
    <div className="chunk-list">
      <div className="sidebar-title">{title}</div>
      {!hl && <p className="chunk-hint">{hint}</p>}
      {groups.map((g) => {
        const current = hl?.row === g.key;
        const hit = current ? g.items.find((i) => i.key === hl?.col) : undefined;
        return (
          <div key={g.key} className={`chunk-group${current ? ' is-current' : ''}`}>
            <div className={`chunk-title${current ? ' hl-axis' : ''}`}>{g.title}</div>
            <div className="chunk-verbs">
              {g.items.map((it) => (
                <span key={it.key} title={it.gloss} className={`chunk-verb${hit?.key === it.key ? ' hl' : ''}`}>
                  {it.label}
                </span>
              ))}
            </div>
            {hit && hit.gloss && <p className="chip-gloss">{hit.gloss}</p>}
          </div>
        );
      })}
    </div>
  );
}
