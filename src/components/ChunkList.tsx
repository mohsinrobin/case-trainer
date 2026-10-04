import { useEffect } from 'react';
import type { ChunkGroup, RefCell } from '../types';

interface Props {
  groups: ChunkGroup[];
  /** Chunk to highlight after an answer has been given (null = nothing highlighted). */
  highlight?: RefCell | null;
}

/**
 * Reference list for the "verb + preposition" section: all chunks grouped by preposition + case.
 * Desktop: the whole list, the answered chunk is highlighted.
 * Phone: only the group of the answered chunk (the full list would not fit), a hint before answering.
 */
export default function ChunkList({ groups, highlight = null }: Props) {
  const hl = highlight?.table === 'chunks' ? highlight : null;

  // keep the highlighted verb in view in the (scrollable) desktop sidebar
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

    // phone: the list itself is the small scrollable panel
    const list = box.querySelector('.chunk-list');
    if (list instanceof HTMLElement && list.scrollHeight > list.clientHeight) {
      let inner = 0;
      if (el) {
        const l = list.getBoundingClientRect();
        const c = el.getBoundingClientRect();
        inner = Math.max(0, list.scrollTop + (c.top - l.top) - list.clientHeight / 2 + c.height / 2);
      }
      list.scrollTo({ top: inner, behavior: 'smooth' });
    }
  }, [highlight]);

  return (
    <div className="chunk-list">
      <div className="sidebar-title">Verb + preposition</div>
      {!hl && (
        <p className="chunk-hint">
          Pick the preposition that belongs to the verb. The matching chunk list shows up here after you answer.
        </p>
      )}
      {groups.map((g) => {
        const current = hl?.row === g.key;
        return (
          <div key={g.key} className={`chunk-group${current ? ' is-current' : ''}`}>
            <div className={`chunk-title${current ? ' hl-axis' : ''}`}>
              {g.prep} <span>+ {g.case}</span>
            </div>
            <div className="chunk-verbs">
              {g.verbs.map((v) => (
                <span
                  key={v.verb}
                  title={v.gloss}
                  className={`chunk-verb${current && hl?.col === v.verb ? ' hl' : ''}`}
                >
                  {v.verb}
                </span>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}
