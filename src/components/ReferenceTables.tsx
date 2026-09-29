import { useEffect } from 'react';
import type { RefCell } from '../types';

const ARTICLE_COLS = ['m', 'f', 'n', 'pl'];
const ARTICLE_ROWS: { key: string; label: string; cells: string[] }[] = [
  { key: 'Nom', label: 'Nom.', cells: ['der', 'die', 'das', 'die'] },
  { key: 'Akk', label: 'Akk.', cells: ['den', 'die', 'das', 'die'] },
  { key: 'Dat', label: 'Dat.', cells: ['dem', 'der', 'dem', 'den (+n)'] },
  { key: 'Gen', label: 'Gen.', cells: ['des', 'der', 'des', 'der'] },
];

const PRONOUN_CASES = ['Nom', 'Akk', 'Dat'];
const PRONOUN_ROWS: { key: string; cells: string[] }[] = [
  { key: 'ich', cells: ['ich', 'mich', 'mir'] },
  { key: 'du', cells: ['du', 'dich', 'dir'] },
  { key: 'er', cells: ['er', 'ihn', 'ihm'] },
  { key: 'sie', cells: ['sie', 'sie', 'ihr'] },
  { key: 'es', cells: ['es', 'es', 'ihm'] },
  { key: 'wir', cells: ['wir', 'uns', 'uns'] },
  { key: 'ihr', cells: ['ihr', 'euch', 'euch'] },
  { key: 'sie/Sie', cells: ['sie/Sie', 'sie/Sie', 'ihnen/Ihnen'] },
];

interface Props {
  /** Cell to highlight after an answer has been given (null = nothing highlighted). */
  highlight?: RefCell | null;
  /** Which table the current exercise uses. On phones only this table is shown. */
  active?: 'article' | 'pronoun';
}

/** "ihnen/Ihnen" may wrap after the slash in narrow cells. */
const breakable = (s: string) => s.split('/').flatMap((part, i) => (i === 0 ? [part] : ['/', <wbr key={i} />, part]));

export default function ReferenceTables({ highlight = null, active = 'article' }: Props) {
  const inArticle = highlight?.table === 'article' ? highlight : null;
  const inPronoun = highlight?.table === 'pronoun' ? highlight : null;

  // In the desktop sidebar the tables can be taller than the window: keep the highlighted cell in view.
  // The (hidden) phone variant of the pronoun table has no layout box, so only visible cells count.
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
      <div className={`ref-block${active === 'article' ? ' is-active' : ''}`}>
        <div className="sidebar-title">Articles</div>
        <table className="ref-table">
          <thead>
            <tr>
              <th></th>
              {ARTICLE_COLS.map((c) => (
                <th key={c} className={inArticle?.col === c ? 'hl-axis' : undefined}>
                  {c}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {ARTICLE_ROWS.map((row) => (
              <tr key={row.key}>
                <td className={`case-label${inArticle?.row === row.key ? ' hl-axis' : ''}`}>{row.label}</td>
                {row.cells.map((cell, i) => (
                  <td
                    key={ARTICLE_COLS[i]}
                    className={inArticle?.row === row.key && inArticle.col === ARTICLE_COLS[i] ? 'hl' : undefined}
                  >
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className={`ref-block${active === 'pronoun' ? ' is-active' : ''}`}>
        <div className="sidebar-title">Pronouns</div>

        {/* desktop: one row per person */}
        <table className="ref-table pron-tall">
          <thead>
            <tr>
              {PRONOUN_CASES.map((c) => (
                <th key={c} className={inPronoun?.col === c ? 'hl-axis' : undefined}>
                  {c}.
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {PRONOUN_ROWS.map((row) => (
              <tr key={row.key}>
                {row.cells.map((cell, i) => {
                  const isRow = inPronoun?.row === row.key;
                  const cls = isRow && inPronoun.col === PRONOUN_CASES[i] ? 'hl' : isRow ? 'hl-axis' : undefined;
                  return (
                    <td key={PRONOUN_CASES[i]} className={cls}>
                      {cell}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>

        {/* phone: same table turned 90 degrees so it is short enough to stay visible */}
        <table className="ref-table pron-wide">
          <thead>
            <tr>
              <th></th>
              {PRONOUN_ROWS.map((row) => (
                <th key={row.key} className={inPronoun?.row === row.key ? 'hl-axis' : undefined}>
                  {breakable(row.key)}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {PRONOUN_CASES.map((c, ci) => (
              <tr key={c}>
                <td className={`case-label${inPronoun?.col === c ? ' hl-axis' : ''}`}>{c}.</td>
                {PRONOUN_ROWS.map((row) => (
                  <td key={row.key} className={inPronoun?.row === row.key && inPronoun.col === c ? 'hl' : undefined}>
                    {breakable(row.cells[ci])}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}
