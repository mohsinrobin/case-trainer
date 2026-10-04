import { useEffect } from 'react';
import type { RefCell } from '../types';

type Decl = 'weak' | 'mixed' | 'strong';

const COLS = ['m', 'f', 'n', 'pl'];
const CASES = ['Nom', 'Akk', 'Dat', 'Gen'];

const TABLES: { key: Decl; title: string; note: string; cells: Record<string, string[]> }[] = [
  {
    key: 'weak',
    title: 'After der / die / das · dieser',
    note: '-en everywhere, except -e in Nom m and Nom/Akk f, n',
    cells: {
      Nom: ['e', 'e', 'e', 'en'],
      Akk: ['en', 'e', 'e', 'en'],
      Dat: ['en', 'en', 'en', 'en'],
      Gen: ['en', 'en', 'en', 'en'],
    },
  },
  {
    key: 'mixed',
    title: 'After ein / kein / mein …',
    note: 'like weak, but -er / -es where "ein" has no ending (Nom m, Nom/Akk n)',
    cells: {
      Nom: ['er', 'e', 'es', 'en'],
      Akk: ['en', 'e', 'es', 'en'],
      Dat: ['en', 'en', 'en', 'en'],
      Gen: ['en', 'en', 'en', 'en'],
    },
  },
  {
    key: 'strong',
    title: 'No article',
    note: 'the ending of der / die / das (exception: Gen m, n → -en)',
    cells: {
      Nom: ['er', 'e', 'es', 'e'],
      Akk: ['en', 'e', 'es', 'e'],
      Dat: ['em', 'er', 'em', 'en'],
      Gen: ['en', 'er', 'en', 'er'],
    },
  },
];

interface Props {
  /** Cell to highlight after an answer has been given (null = nothing highlighted). */
  highlight?: RefCell | null;
  /** Which table the current exercise uses. On phones only this table is shown. */
  active?: Decl;
}

/** Adjective endings: three small tables (weak / mixed / strong), the answered cell is highlighted. */
export default function AdjectiveTables({ highlight = null, active = 'weak' }: Props) {
  const hl = highlight?.table === 'adjective' ? highlight : null;
  const [hlDecl, hlCase] = hl ? hl.row.split(' ') : ['', ''];

  // keep the highlighted cell in view in the (scrollable) desktop sidebar
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

  return (
    <>
      {TABLES.map((t) => {
        const here = hlDecl === t.key;
        return (
          <div key={t.key} className={`ref-block${active === t.key ? ' is-active' : ''}`}>
            <div className="sidebar-title">{t.title}</div>
            <table className="ref-table adj-table">
              <thead>
                <tr>
                  <th></th>
                  {COLS.map((c) => (
                    <th key={c} className={here && hl?.col === c ? 'hl-axis' : undefined}>
                      {c}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {CASES.map((c) => (
                  <tr key={c}>
                    <td className={`case-label${here && hlCase === c ? ' hl-axis' : ''}`}>{c}.</td>
                    {t.cells[c].map((cell, i) => (
                      <td key={COLS[i]} className={here && hlCase === c && hl?.col === COLS[i] ? 'hl' : undefined}>
                        -{cell}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
            <p className="adj-note">{t.note}</p>
          </div>
        );
      })}
    </>
  );
}
