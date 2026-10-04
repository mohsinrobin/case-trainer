import { useEffect } from 'react';
import type { RefCell } from '../types';

const COLS = ['m', 'f', 'n', 'pl'];
const ROWS: { key: string; label: string; ein: string[]; der: string[] }[] = [
  { key: 'Nom', label: 'Nom.', ein: ['–', '-e', '–', '-e'], der: ['der', 'die', 'das', 'die'] },
  { key: 'Akk', label: 'Akk.', ein: ['-en', '-e', '–', '-e'], der: ['den', 'die', 'das', 'die'] },
  { key: 'Dat', label: 'Dat.', ein: ['-em', '-er', '-em', '-en'], der: ['dem', 'der', 'dem', 'den'] },
  { key: 'Gen', label: 'Gen.', ein: ['-es', '-er', '-es', '-er'], der: ['des', 'der', 'des', 'der'] },
];

interface Props {
  /** Cell to highlight after an answer has been given (null = nothing highlighted). */
  highlight?: RefCell | null;
}

/** Endings of ein / kein / mein / dein / sein / ihr / unser, next to der / die / das for comparison. */
export default function PossessiveTables({ highlight = null }: Props) {
  const hl = highlight?.table === 'possessive' ? highlight : null;

  useEffect(() => {
    const box = document.querySelector('.sidebar');
    if (!(box instanceof HTMLElement)) return;
    const cell = [...box.querySelectorAll('td.hl')].find((c) => (c as HTMLElement).offsetParent !== null);
    let top = 0;
    if (cell) {
      const b = box.getBoundingClientRect();
      const c = cell.getBoundingClientRect();
      top = Math.max(0, box.scrollTop + (c.top - b.top) - box.clientHeight / 2 + c.height / 2);
    }
    box.scrollTo({ top, behavior: 'smooth' });
  }, [highlight]);

  const table = (kind: 'ein' | 'der') => (
    <table className="ref-table adj-table">
      <thead>
        <tr>
          <th></th>
          {COLS.map((c) => (
            <th key={c} className={hl?.col === c ? 'hl-axis' : undefined}>
              {c}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {ROWS.map((row) => (
          <tr key={row.key}>
            <td className={`case-label${hl?.row === row.key ? ' hl-axis' : ''}`}>{row.label}</td>
            {row[kind].map((cell, i) => {
              const here = hl?.row === row.key && hl.col === COLS[i];
              return (
                <td key={COLS[i]} className={here ? (kind === 'ein' ? 'hl' : 'hl-axis') : undefined}>
                  {cell}
                </td>
              );
            })}
          </tr>
        ))}
      </tbody>
    </table>
  );

  return (
    <>
      <div className="ref-block is-active">
        <div className="sidebar-title">Endings: ein · kein · mein · dein · sein · ihr · unser</div>
        {table('ein')}
        <p className="adj-note">same as der / die / das, but no ending in Nom m and Nom/Akk n</p>
      </div>
      <div className="ref-block">
        <div className="sidebar-title">For comparison: articles</div>
        {table('der')}
      </div>
    </>
  );
}
