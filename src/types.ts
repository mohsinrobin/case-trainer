/** Which cell of the reference tables an answer comes from (used to highlight it). */
export interface RefCell {
  table: 'article' | 'pronoun' | 'chunks';
  /** article table: Nom | Akk | Dat | Gen   -   pronoun table: ich | du | er | sie | es | wir | ihr | sie/Sie
   *  chunk list: group key such as "auf + Akk" */
  row: string;
  /** article table: m | f | n | pl   -   pronoun table: Nom | Akk | Dat   -   chunk list: the verb */
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

/** One group of the verb + preposition chunk list, e.g. "auf + Akk" with all its verbs. */
export interface ChunkGroup {
  key: string;
  prep: string;
  case: string;
  verbs: { verb: string; gloss: string; level: 'A' | 'B' | 'C' }[];
}
