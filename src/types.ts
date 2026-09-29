/** Which cell of the reference tables an answer comes from (used to highlight it). */
export interface RefCell {
  table: 'article' | 'pronoun';
  /** article table: Nom | Akk | Dat | Gen   -   pronoun table: ich | du | er | sie | es | wir | ihr | sie/Sie */
  row: string;
  /** article table: m | f | n | pl   -   pronoun table: Nom | Akk | Dat */
  col: string;
}

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
  ref?: RefCell;
}
