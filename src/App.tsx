import { useState, useEffect, useCallback } from 'react';
import type { Exercise } from './types';
import ReferenceTables from './components/ReferenceTables';
import QuestionCard from './components/QuestionCard';
import aDataRaw from './data/a.json';
import bDataRaw from './data/b.json';
import cDataRaw from './data/c.json';

const DATA: Record<string, Exercise[]> = {
  A: aDataRaw as Exercise[],
  B: bDataRaw as Exercise[],
  C: cDataRaw as Exercise[],
};

function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

type Level = 'A' | 'B' | 'C';

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
        <div className="level-buttons">
          {(['A', 'B', 'C'] as Level[]).map((l) => (
            <button key={l} className="level-btn" onClick={() => setLevel(l)}>
              {l}
            </button>
          ))}
        </div>
        <p className="level-hint">
          A = everyday · B = workplace / travel · C = abstract / academic
        </p>
      </div>
    );
  }

  // --- Practice screen ---
  return (
    <div className="practice">
      {/* Top bar */}
      <div className="top-bar">
        <div className="top-bar-left">
          <span className="top-bar-title">Case Practice</span>
          <div className="level-switch">
            {(['A', 'B', 'C'] as Level[]).map((l) => (
              <button
                key={l}
                className={`mini-level-btn ${level === l ? 'active' : ''}`}
                onClick={() => setLevel(l)}
              >
                {l}
              </button>
            ))}
          </div>
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
            🔀 Random
          </button>
        </div>
      </div>

      {/* Sidebar — reference tables */}
      <aside className="sidebar">
        <ReferenceTables
          active={current?.type === 'personal_pronoun' ? 'pronoun' : 'article'}
          highlight={selectedAnswer !== null ? current?.ref ?? null : null}
        />
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
