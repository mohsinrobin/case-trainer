import { useState, useEffect, useCallback } from 'react';
import type { ChunkGroup, ConnectorTableData, Exercise, PanelGroup } from './types';
import ReferenceTables from './components/ReferenceTables';
import ChunkList from './components/ChunkList';
import AdjectiveTables from './components/AdjectiveTables';
import PossessiveTables from './components/PossessiveTables';
import ChipPanel from './components/ChipPanel';
import ConnectorTable from './components/ConnectorTable';
import QuestionCard from './components/QuestionCard';
import aDataRaw from './data/a.json';
import bDataRaw from './data/b.json';
import cDataRaw from './data/c.json';
import vpDataRaw from './data/vp.json';
import adjDataRaw from './data/adj.json';
import possDataRaw from './data/poss.json';
import decDataRaw from './data/dec.json';
import decRulesRaw from './data/dec_rules.json';
import fuzDataRaw from './data/fuz.json';
import fuzGroupsRaw from './data/fuz_groups.json';
import lazyDataRaw from './data/lazy.json';
import lazyLaddersRaw from './data/lazy_ladders.json';
import konDataRaw from './data/kon.json';
import konTableRaw from './data/kon_table.json';
import vpChunksRaw from './data/vp_chunks.json';

const DATA: Record<string, Exercise[]> = {
  A: aDataRaw as Exercise[],
  B: bDataRaw as Exercise[],
  C: cDataRaw as Exercise[],
  VP: vpDataRaw as Exercise[],
  ADJ: adjDataRaw as Exercise[],
  EIN: possDataRaw as Exercise[],
  DEC: decDataRaw as Exercise[],
  FUZ: fuzDataRaw as Exercise[],
  LAZY: lazyDataRaw as Exercise[],
  KON: konDataRaw as Exercise[],
};

const DEC_RULES = decRulesRaw as PanelGroup[];
const FUZ_GROUPS = fuzGroupsRaw as PanelGroup[];
const LAZY_LADDERS = lazyLaddersRaw as PanelGroup[];
const KON_TABLE = konTableRaw as ConnectorTableData;

const CHUNK_GROUPS = vpChunksRaw as ChunkGroup[];

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

type Level = 'A' | 'B' | 'C' | 'VP' | 'ADJ' | 'EIN' | 'DEC' | 'FUZ' | 'LAZY' | 'KON';
const GROUPS: { title: string; hint: string; levels: Level[] }[] = [
  {
    title: 'Case',
    hint: 'A = everyday · B = workplace / travel · C = abstract / academic · V+P = verb + preposition chunks · ADJ = adjective endings · EIN = ein / kein / mein endings',
    levels: ['A', 'B', 'C', 'VP', 'ADJ', 'EIN'],
  },
  {
    title: 'B2 Wortschatz',
    hint: 'Decoder = English → German by rules · Bug hunt = wrong collocation · Upgrade = replace lazy words · Logik = connectors',
    levels: ['DEC', 'FUZ', 'LAZY', 'KON'],
  },
];
const LEVEL_LABEL: Record<Level, string> = { A: 'A', B: 'B', C: 'C', VP: 'V+P', ADJ: 'ADJ', EIN: 'EIN', DEC: 'Decoder', FUZ: 'Bug hunt', LAZY: 'Upgrade', KON: 'Logik' };

export default function App() {
  const [level, setLevel] = useState<Level | null>(null);
  const [random, setRandom] = useState(false);
  const [queue, setQueue] = useState<Exercise[]>([]);
  const [idx, setIdx] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);

  // Build queue when level changes — shuffle once if random is on
  useEffect(() => {
    if (!level) return;
    const data = DATA[level] || [];
    setQueue(random ? shuffle(data) : data);
    setIdx(0);
    setSelectedAnswer(null);
  }, [level]);

  // Reshuffle only remaining items when random toggles during practice
  const handleRandomToggle = useCallback(() => {
    setRandom((prev) => {
      if (!prev) {
        // Turning random ON: shuffle only the remaining (unsolved) items
        const remainingItems = queue.slice(idx);
        const shuffledRemaining = shuffle(remainingItems);
        setQueue((q) => [...q.slice(0, idx), ...shuffledRemaining]);
      } else {
        // Turning random OFF: restore original order for remaining items
        const data = DATA[level!] || [];
        const originalRemaining = data.slice(idx);
        setQueue((q) => [...q.slice(0, idx), ...originalRemaining]);
      }
      setSelectedAnswer(null);
      return !prev;
    });
  }, [level, queue, idx]);


  // The top bar can wrap on narrow phones; the sticky reference panel must start right below it.
  useEffect(() => {
    const bar = document.querySelector('.top-bar');
    if (!(bar instanceof HTMLElement)) return;
    const update = () => document.documentElement.style.setProperty('--topbar-h', `${bar.offsetHeight}px`);
    update();
    const ro = new ResizeObserver(update);
    ro.observe(bar);
    return () => ro.disconnect();
  }, [level]);

  const current = queue[idx] ?? null;
  const total = queue.length;
  const solved = idx + (selectedAnswer !== null ? 1 : 0);
  const remaining = Math.max(0, total - solved);
  const isFinished = idx >= total;

  const handleSelect = useCallback((option: string) => {
    setSelectedAnswer(option);
  }, []);

  const goNext = useCallback(() => {
    if (!current || selectedAnswer === null) return;
    setIdx((prev) => prev + 1);
    setSelectedAnswer(null);
  }, [current, selectedAnswer]);

  // Keyboard shortcut: N or Enter
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
      if (e.target instanceof HTMLInputElement || e.target instanceof HTMLTextAreaElement) return;
      if (e.key === 'n' || e.key === 'N' || e.key === 'Enter') {
        e.preventDefault();
        goNext();
      }
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [goNext]);

  // --- Home screen ---
  if (!level) {
    return (
      <div className="home">
        <h1>German Case Practice</h1>
        <p className="tagline">Repetitive practice. No lessons. Just do.</p>
        {GROUPS.map((g) => (
          <div key={g.title} className="home-group">
            <div className="home-group-title">{g.title}</div>
            <div className="level-buttons">
              {g.levels.map((l) => (
                <button key={l} className={`level-btn${LEVEL_LABEL[l].length > 4 ? ' wide' : ''}`} onClick={() => setLevel(l)}>
                  {LEVEL_LABEL[l]}
                </button>
              ))}
            </div>
            <p className="level-hint">{g.hint}</p>
          </div>
        ))}
      </div>
    );
  }

  // --- Practice screen ---
  return (
    <div className={`practice${level === 'KON' ? ' wide-side' : ''}`}>
      {/* Top bar */}
      <div className="top-bar">
        <div className="top-bar-left">
          <span className="top-bar-title">Case Practice</span>
          <select className="level-select" value={level} onChange={(e) => setLevel(e.target.value as Level)}>
            {GROUPS.map((g) => (
              <optgroup key={g.title} label={g.title}>
                {g.levels.map((l) => (
                  <option key={l} value={l}>
                    {LEVEL_LABEL[l]}
                  </option>
                ))}
              </optgroup>
            ))}
          </select>
        </div>
        <div className="top-bar-right">
          <div className="counter">
            <span className="counter-solved">✓ {solved}</span>
            <span className="counter-sep">/</span>
            <span className="counter-total">{total}</span>
            {remaining > 0 && <span className="counter-remaining">({remaining} left)</span>}
          </div>
          <button
            className={`random-btn ${random ? 'active' : ''}`}
            onClick={handleRandomToggle}
          >
            🔀 <span className="random-label">Random</span>
          </button>
        </div>
      </div>

      {/* Sidebar — reference tables */}
      <aside className="sidebar">
        {level === 'DEC' ? (
          <ChipPanel
            table="rules"
            title="Sound-shift rules"
            hint="Predict the German form. The rule you needed shows up here after you answer."
            groups={DEC_RULES}
            highlight={selectedAnswer !== null ? current?.ref ?? null : null}
          />
        ) : level === 'FUZ' ? (
          <ChipPanel
            table="ladder"
            title="Natural partners"
            hint="Tap the word that does not belong. The natural partners show up here after you answer."
            groups={FUZ_GROUPS}
            highlight={selectedAnswer !== null ? current?.ref ?? null : null}
          />
        ) : level === 'LAZY' ? (
          <ChipPanel
            table="ladder"
            title="Upgrade ladders"
            hint="Pick the precise word. The ladder of the lazy word shows up here after you answer."
            groups={LAZY_LADDERS}
            highlight={selectedAnswer !== null ? current?.ref ?? null : null}
          />
        ) : level === 'KON' ? (
          <ConnectorTable data={KON_TABLE} highlight={selectedAnswer !== null ? current?.ref ?? null : null} answer={current?.answer ?? null} />
        ) : level === 'VP' ? (
          <ChunkList groups={CHUNK_GROUPS} highlight={selectedAnswer !== null ? current?.ref ?? null : null} />
        ) : level === 'EIN' ? (
          <PossessiveTables highlight={selectedAnswer !== null ? current?.ref ?? null : null} />
        ) : level === 'ADJ' ? (
          <AdjectiveTables
            active={(current?.ref?.row.split(' ')[0] as 'weak' | 'mixed' | 'strong' | undefined) ?? 'weak'}
            highlight={selectedAnswer !== null ? current?.ref ?? null : null}
          />
        ) : (
          <ReferenceTables
            active={current?.type === 'personal_pronoun' ? 'pronoun' : 'article'}
            highlight={selectedAnswer !== null ? current?.ref ?? null : null}
          />
        )}
      </aside>

      {/* Main content */}
      <div className="main-content">
        {isFinished ? (
          <div className="finished-card">
            <p className="finished-text">All {total} sentences completed!</p>
            <p className="finished-sub">Switch level or toggle Random to start again.</p>
          </div>
        ) : (
          <>
            {current && (
              <QuestionCard
                exercise={current}
                selectedAnswer={selectedAnswer}
                onSelect={handleSelect}
              />
            )}

            {selectedAnswer !== null && (
              <button className="next-btn" onClick={goNext}>
                Next sentence
                <span className="shortcut-hint">(press N)</span>
              </button>
            )}
          </>
        )}
      </div>
    </div>
  );
}
