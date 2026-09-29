import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const DATA_DIR = path.join(__dirname, '..', 'src', 'data');
const LEVELS = ['a', 'b', 'c'] as const;
const VALID_LEVELS = new Set(['A', 'B', 'C']);

let errors = 0;
const allIds = new Set<string>();
const allSentences = new Map<string, string>(); // sentence -> id

function loadLevel(level: string) {
  const filePath = path.join(DATA_DIR, `${level}.json`);
  if (!fs.existsSync(filePath)) {
    console.error(`❌ ${level}.json not found`);
    errors++;
    return [];
  }
  try {
    const raw = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(raw) as any[];
  } catch (e) {
    console.error(`❌ ${level}.json: invalid JSON — ${e}`);
    errors++;
    return [];
  }
}

function validate(exercises: any[]) {
  for (const ex of exercises) {
    const id = ex.id;

    // id exists
    if (!id) {
      console.error(`❌ Missing id`);
      errors++;
      continue;
    }

    // unique id
    if (allIds.has(id)) {
      console.error(`❌ ${id}: duplicate id`);
      errors++;
    }
    allIds.add(id);

    // level
    if (!VALID_LEVELS.has(ex.level)) {
      console.error(`❌ ${id}: invalid level "${ex.level}" (must be A, B, or C)`);
      errors++;
    }

    // sentence has exactly one ___
    if (!ex.sentence || typeof ex.sentence !== 'string') {
      console.error(`❌ ${id}: missing sentence`);
      errors++;
    } else {
      const blanks = (ex.sentence.match(/___/g) || []).length;
      if (blanks !== 1) {
        console.error(`❌ ${id}: sentence must contain exactly one "___" (found ${blanks})`);
        errors++;
      }

      // duplicate sentence
      if (allSentences.has(ex.sentence)) {
        console.error(`❌ ${id}: duplicate sentence (also in ${allSentences.get(ex.sentence)})`);
        errors++;
      }
      allSentences.set(ex.sentence, id);
    }

    // options
    if (!Array.isArray(ex.options) || ex.options.length === 0) {
      console.error(`❌ ${id}: options must be a non-empty array`);
      errors++;
    }

    // answer exists
    if (!ex.answer) {
      console.error(`❌ ${id}: missing answer`);
      errors++;
    }

    // answer in options
    if (ex.answer && Array.isArray(ex.options) && !ex.options.includes(ex.answer)) {
      console.error(`❌ ${id}: answer "${ex.answer}" not found in options`);
      errors++;
    }

    // explanation
    if (!ex.explanation) {
      console.error(`❌ ${id}: missing explanation`);
      errors++;
    }
  }
}

console.log('🔍 Validating exercises...\n');

for (const level of LEVELS) {
  const exercises = loadLevel(level);
  validate(exercises);
}

console.log(`\n${errors === 0 ? '✅ All exercises valid!' : `❌ ${errors} error(s) found.`}`);
process.exit(errors > 0 ? 1 : 0);
