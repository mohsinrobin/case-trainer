import { useEffect } from 'react';
import type { ConnectorTableData, RefCell } from '../types';

interface Props {
  data: ConnectorTableData;
  /** Cell to highlight after an answer has been given (null = nothing highlighted). */
  highlight?: RefCell | null;
  /** The connector that was the right answer (shown bold inside the highlighted cell). */
  answer?: string | null;
}

/** Connectors by logical relation (rows) and word-order class (columns). */
export default function ConnectorTable({ data, highlight = null, answer = null }: Props) {
  const hl = highlight?.table === 'connector' ? highlight : null;

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
    <div className="ref-block is-active conn-block">
      <div className="sidebar-title">Connectors</div>
      {!hl && <p className="chunk-hint">Find the logical relation first, then check the word order after the blank.</p>}
      <table className="ref-table conn-table">
        <thead>
          <tr>
            <th></th>
            {data.classes.map((c) => (
              <th key={c.key} className={hl?.col === c.key ? 'hl-axis' : undefined}>
                {c.title}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.rows.map((row) => (
            <tr key={row.key} className={`conn-row${hl?.row === row.key ? ' is-current' : ''}`}>
              <td className={`case-label${hl?.row === row.key ? ' hl-axis' : ''}`}>{row.label}</td>
              {data.classes.map((c) => {
                const words = row.cells[c.key] ?? [];
                const here = hl?.row === row.key && hl.col === c.key;
                return (
                  <td key={c.key} className={here ? 'hl' : undefined}>
                    {words.length === 0
                      ? '–'
                      : words.map((w, i) => (
                          <span key={w}>
                            {i > 0 && ', '}
                            {here && answer && w.toLowerCase() === answer.toLowerCase() ? <u>{w}</u> : w}
                          </span>
                        ))}
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
