import type { Exercise } from '../types';

interface Props {
  exercise: Exercise;
  selectedAnswer: string | null;
  onSelect: (option: string) => void;
}

export default function QuestionCard({ exercise, selectedAnswer, onSelect }: Props) {
  const answered = selectedAnswer !== null;
  const isCorrect = selectedAnswer === exercise.answer;

  // Split sentence at ___ to show the blank
  const parts = exercise.sentence.split('___');

  return (
    <div className="question-card">
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

      {answered && (
        <div className={`feedback ${isCorrect ? 'correct' : 'incorrect'}`}>
          <span className="feedback-icon">{isCorrect ? '✓' : '✗'}</span>
          <span className="feedback-text">{isCorrect ? 'Correct' : 'Incorrect'}</span>
        </div>
      )}

      {answered && (
        <div className="explanation">
          <strong>Correct answer:</strong> {exercise.answer}
          <br />
          <strong>Why:</strong> {exercise.explanation}
        </div>
      )}
    </div>
  );
}
