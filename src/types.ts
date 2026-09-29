export interface Exercise {
  id: string;
  level: 'A' | 'B' | 'C';
  type: string;
  sentence: string;
  options: string[];
  answer: string;
  case: string;
  focus: string;
  explanation: string;
  tags: string[];
}
