import type { Exercise } from '../types';

interface Props {
  exercise: Exercise;
  selectedAnswer: string | null;
  onSelect: (option: string) => void;
}

/** "„Entscheidung“," -> "Entscheidung" (punctuation is not part of the tappable word). */
const clean = (tok: string) => tok.replace(/^[„“"(]+|[.,;:!?“")]+$/g, '');

export default function QuestionCard({ exercise, selectedAnswer, onSelect }: Props) {
  const answered = selectedAnswer !== null;
  const isCorrect = selectedAnswer === exercise.answer;
  const bugHunt = exercise.type === 'collocation_bug';

  // Split sentence at ___ to show the blank
  const parts = exercise.sentence.split('___');

  return (
    <div className="question-card">
      {bugHunt ? (
        <>
          <p className="bug-prompt">One word does not belong here. Tap it.</p>
          <p className="sentence bug-sentence">
            {exercise.sentence.split(' ').map((tok, i) => {
              const word = clean(tok);
              if (!exercise.options.includes(word)) return <span key={i}>{tok} </span>;
              let cls = 'tok';
              if (answered) {
                if (word === exercise.answer) cls += ' correct';
                else if (word === selectedAnswer) cls += ' wrong';
                else cls += ' dimmed';
              }
              return (
                <span key={i}>
                  <button className={cls} disabled={answered} onClick={() => !answered && onSelect(word)}>
                    {tok}
                  </button>{' '}
                </span>
              );
            })}
          </p>
        </>
      ) : (
        <>
          <p className="sentence">
            {parts[0]}
            <span className={`blank${/\p{L}$/u.test(parts[0]) ? ' blank-suffix' : ''}`}>{answered ? exercise.answer : '___'}</span>
            {parts[1]}
          </p>

          <div className="options">
            {exercise.options.map((option) => {
              let cls = 'option-btn';
              if (answered) {
                if (option === exercise.answer) {
                  cls += ' correct';
                } else if (option === selectedAnswer) {
                  cls += ' wrong';
                } else {
                  cls += ' dimmed';
                }
              }
              return (
                <button
                  key={option}
                  className={cls}
                  onClick={() => !answered && onSelect(option)}
                  disabled={answered}
                >
                  {option}
                </button>
              );
            })}
          </div>
        </>
      )}

      {answered && (
        <div className={`feedback ${isCorrect ? 'correct' : 'incorrect'}`}>
          <span className="feedback-icon">{isCorrect ? '✓' : '✗'}</span>
          <span className="feedback-text">{isCorrect ? 'Correct' : 'Incorrect'}</span>
        </div>
      )}

      {answered && (
        <div className="explanation">
          <strong>{bugHunt ? 'The bug:' : 'Correct answer:'}</strong> {exercise.answer}
          <br />
          <strong>Why:</strong> {exercise.explanation}
        </div>
      )}
    </div>
  );
}
