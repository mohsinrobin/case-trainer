You are a senior frontend engineer and product-minded UI developer.

Build a very small, minimalistic German grammar practice web app.

The purpose of the app is NOT to teach grammar through lessons.

The purpose is repetitive practice.

I want to practice thousands of German sentences, make mistakes, immediately see the correct answer and the logic behind it, and continue to the next sentence.

Do not over-engineer this project.

---

# 1. Core learning philosophy

The learner should learn by doing, not by reading lessons first.

The workflow is:

1. Show a German sentence with exactly one blank.
2. Show ALL answer choices as visible buttons.
3. User chooses one answer.
4. Immediately tell the user whether the selection was correct or incorrect.
5. ALWAYS reveal the correct answer.
6. ALWAYS show a very short explanation of WHY that answer is correct.
7. User presses `N` or clicks `Next sentence`.
8. Show the next sentence.
9. Repeat thousands of times.

The explanation must appear after EVERY answer, even when the learner answered correctly.

The learner may have guessed correctly, so "Correct" alone is not enough.

The explanation is therefore an essential part of every question.

Do not show the explanation before the learner answers.

---

# 2. Learning scope

The app is mainly for practicing German case-related form changes such as:

- Nominativ
- Akkusativ
- Dativ
- Genitiv

Practice should include, where appropriate:

- definite articles
- indefinite articles
- negative articles
- personal pronouns
- possessive forms
- der-word / ein-word style changes
- adjective endings
- common endings such as:
  - -e
  - -en
  - -er
  - -em
  - -es
- masculine / feminine / neuter
- singular / plural
- common prepositions
- verbs that determine a case
- direct and indirect objects
- natural sentence contexts

This is NOT a grammar-course application.

There should be no chapter system and no long theory section.

The reference tables described below are enough.

---

# 3. Level system

Only provide three levels:

- A
- B
- C

Do NOT create separate A1, A2, B1, B2, C1 or C2 buttons.

Internally:

A = vocabulary and contexts suitable roughly for A1 + A2

B = vocabulary and contexts suitable roughly for B1 + B2

C = vocabulary and contexts suitable roughly for C1 + C2

The grammar can overlap between levels.

The main difference should be vocabulary, sentence structure, context and overall complexity.

Examples:

A:
short everyday sentences, family, shopping, work, transport, food, home, appointments, simple conversations.

B:
more varied vocabulary, workplace, education, travel, opinions, bureaucracy, relationships, news-like everyday contexts, more complex clauses.

C:
more sophisticated vocabulary, abstract ideas, professional contexts, academic contexts, nuanced sentence structures and more demanding syntax.

---

# 4. Application flow

Initial screen:

Show only a simple title such as:

"German Case Practice"

Then three large level buttons:

[A] [B] [C]

After selecting a level, enter the practice screen.

The user must be able to switch level later without reloading the application.

---

# 5. Practice screen layout

The page should have three main areas.

## AREA 1 — Sticky reference tables

At the top of the screen there should be a compact sticky reference area.

It stays visible while practicing.

Desktop:
show the two reference tables next to each other if space allows.

Mobile:
stack them vertically or allow a compact responsive layout.

Reference table 1:

German article / case transformations.

Include a compact useful table covering:

- Nominativ
- Akkusativ
- Dativ
- Genitiv

and:

- Masculine
- Feminine
- Neuter
- Plural

Include definite article forms such as:

der
die
das
den
dem
des

Also include the most useful ending patterns relevant to this practice system.

Do not add paragraphs explaining the theory.

It should function as a visual cheat sheet.

Reference table 2:

Personal pronoun transformations.

For example the useful Nominativ / Akkusativ / Dativ forms:

ich → mich → mir
du → dich → dir
er → ihn → ihm
sie → sie → ihr
es → es → ihm
wir → uns → uns
ihr → euch → euch
sie/Sie → sie/Sie → ihnen/Ihnen

Keep this table compact and easy to scan while answering.

---

# 6. Question card

Under the reference area show one clean question card.

Example:

Ich sehe ___ Mann jeden Morgen.

Then show all choices visibly as buttons.

For this example:

[der] [die] [das] [den] [dem] [des]

IMPORTANT:

Never use a select/dropdown.

Never hide the options.

All choices belonging to that question must always be visible simultaneously.

The available choices must come from the JSON question object.

This allows different question types to use different choice sets.

Examples:

Article question:

[der] [die] [das] [den] [dem] [des]

Adjective-ending question:

[-e] [-en] [-er] [-em] [-es]

Pronoun question could use the relevant possible forms.

The component should therefore NOT assume that every question uses the same six options.

Render the `options` array supplied by the JSON.

---

# 7. Answer behaviour

When the learner clicks an option:

Immediately lock the current question.

Do not allow the learner to change the recorded answer.

If correct, show a subtle positive state:

"✓ Correct"

If incorrect, show:

"✗ Incorrect"

Also clearly highlight:

- the answer selected by the user
- the actual correct answer

Most importantly:

ALWAYS show the explanation panel after selection.

This applies to BOTH correct and incorrect answers.

Example:

Correct answer: den

Why:
"sehen" takes a direct object here → Akkusativ.
"Mann" is masculine.
Masculine definite article changes from `der` to `den` in Akkusativ.

The explanation should be short.

Usually around 1–3 short lines.

Do not turn the explanation into a lesson.

The learner should quickly understand the logic and continue practicing.

Use German grammar terms such as Akkusativ, Dativ, Nominativ, Genitiv, masculine, feminine etc.

The explanatory sentence itself should be written in English with the important German terminology preserved.

For example:

`sehen` takes a direct object in Akkusativ. `Mann` is masculine, so `der → den`.

---

# 8. Next sentence

After answering, show a clearly visible:

"Next sentence"

button.

Keyboard shortcut:

Pressing the `N` key should perform the exact same action.

Rules:

- `N` only works after the current question has been answered.
- It should move immediately to the next sentence.
- Do not trigger it when the user is interacting with an input element, if inputs are ever added later.

Optional:

Also allow Enter after answering if it does not complicate the implementation.

`N` is the important shortcut.

---

# 9. Random mode

Include one simple toggle/button:

"Random"

Default behaviour can be sequential.

When Random is enabled:

shuffle the questions belonging to the selected level.

Do not repeatedly pick completely random array indexes because that can create many unnecessary repeats.

Instead use a shuffled queue / shuffled array.

Go through the shuffled questions.

When all questions have been used, reshuffle the level.

Avoid showing the exact same question twice consecutively when possible.

The current Random state should be visually obvious.

No complicated random settings are necessary.

---

# 10. Static data architecture

VERY IMPORTANT:

Do NOT use an AI model at runtime.

Do NOT generate sentences dynamically while the learner is practicing.

All exercises are static curated records stored in JSON.

Use files such as:

src/data/a.json
src/data/b.json
src/data/c.json

or another clean equivalent.

Only load/use the selected level's dataset.

The final project may contain approximately 4,000–5,000 exercises.

A reasonable target could eventually be approximately:

A: ~1,500 exercises
B: ~1,500 exercises
C: ~1,500 exercises

The exact distribution does not need to be hardcoded.

The app must work equally well if a JSON file contains 50 exercises or 2,000 exercises.

For the initial implementation, DO NOT waste tokens generating 4,500 sentences.

Create only enough high-quality sample records to demonstrate and test every supported question type.

The real dataset will be populated separately later.

---

# 11. JSON exercise schema

Use a clean extensible schema similar to:

{
  "id": "A-0001",
  "level": "A",
  "type": "definite_article",
  "sentence": "Ich sehe ___ Mann jeden Morgen.",
  "options": [
    "der",
    "die",
    "das",
    "den",
    "dem",
    "des"
  ],
  "answer": "den",
  "case": "Akkusativ",
  "focus": "masculine definite article",
  "explanation": "`sehen`-এর object এখানে Akkusativ। `Mann` masculine, তাই `der → den`।",
  "tags": [
    "akkusativ",
    "masculine",
    "definite-article"
  ]
}

Keep this structure easy to edit manually.

Possible `type` values may include:

- definite_article
- indefinite_article
- possessive
- personal_pronoun
- adjective_ending
- preposition_case
- mixed_case

Do not make the UI dependent on these specific values.

They are mainly metadata for organization and future expansion.

---

# 12. Dataset requirements

Eventually the dataset should contain many different contexts.

Do not create thousands of sentences that are merely the same sentence with one noun replaced.

There should be real contextual variety.

Examples of contexts:

- home
- family
- friends
- dating
- school
- university
- workplace
- meetings
- restaurants
- shopping
- supermarket
- doctor
- pharmacy
- public transport
- Deutsche Bahn
- airport
- travelling
- hotel
- renting an apartment
- government offices
- Anmeldung
- appointments
- phone conversations
- email
- technology
- hobbies
- sports
- news
- environment
- culture
- social situations
- professional situations
- abstract discussions at higher levels

Balance exercises across:

- cases
- genders
- plural
- article types
- pronouns
- adjective endings
- sentence patterns

Avoid unnatural textbook German.

Sentences should sound like something a German speaker could realistically say or write.

Avoid duplicates and near-duplicates.

---

# 13. Data validation

Because the final corpus will contain thousands of records, create a very small validation script.

For every exercise verify:

- `id` exists
- IDs are unique
- `level` is A, B or C
- `sentence` contains exactly one `___`
- `options` is a non-empty array
- `answer` exists inside `options`
- `explanation` exists
- no exact duplicate sentence exists

The validator should print clear errors including the exercise ID.

Do not create a complicated backend validation system.

A simple development-time script is enough.

---

# 14. Technical stack

Use:

- Vite
- React
- TypeScript
- plain CSS

Avoid unnecessary libraries.

Do NOT use a UI component framework.

Do NOT add Redux.

Do NOT add a backend.

Do NOT add a database.

Do NOT require authentication.

Keep state management local and simple.

Suggested components:

App
LevelSelector
ReferenceTables
QuestionCard
AnswerOptions
AnswerExplanation

This structure is only a suggestion.

If an even simpler structure is cleaner, use it.

---

# 15. Visual design

The design must be extremely minimal.

Think:

clean study tool,
not SaaS dashboard.

Use:

- lots of whitespace
- readable typography
- subtle borders
- small border radius
- strong readability
- restrained visual feedback
- responsive layout

Avoid:

- gradients
- illustrations
- unnecessary icons
- heavy shadows
- animations everywhere
- sidebars
- navigation menus
- dashboards
- charts
- progress rings
- gamification graphics

The German sentence should be the visual focus.

Reference tables should remain useful but visually secondary.

---

# 16. Mobile behaviour

The app must work well on phone and desktop.

On smaller screens:

- reference tables may stack
- option buttons may wrap
- sentence must remain easy to read
- sticky reference section must not consume the entire screen
- if necessary, make the reference area compact while preserving visibility

Do not create a separate mobile design.

Use responsive CSS.

---

# 17. Accessibility

Use real buttons.

Provide visible keyboard focus states.

Do not communicate correct/incorrect purely through colour.

Include text such as:

✓ Correct
✗ Incorrect

Maintain readable contrast.

---

# 18. Features that must NOT be added

Do not add:

- login
- account system
- backend
- database
- AI chatbot
- runtime LLM calls
- streak system
- XP
- badges
- leaderboard
- timer
- daily goals
- achievements
- analytics dashboard
- social features
- translations for every sentence
- audio
- speech recognition
- lesson pages
- long grammar tutorials
- complex settings
- admin dashboard
- fancy animations

These can be considered in the future.

They are explicitly outside the current scope.

---

# 19. Important UX principle

The primary loop must always stay this simple:

Sentence
→ choose answer
→ correct/incorrect
→ see correct answer
→ understand why
→ press N
→ next sentence.

A learner should be able to sit for an hour and answer hundreds of questions with almost no mouse movement or cognitive overhead outside the German grammar itself.

---

# 20. Initial seed data

Create a small but varied seed dataset sufficient to test the application.

Include examples covering:

- Nominativ
- Akkusativ
- Dativ
- Genitiv
- masculine
- feminine
- neuter
- plural
- articles
- pronouns
- adjective endings
- common case-governing prepositions

Include records from A, B and C.

Do not generate thousands of records during the application-building task.

Quality is more important than quantity.

---

# 21. Code quality

Keep the implementation understandable.

Prefer boring, readable code over clever abstractions.

Do not build a generic grammar framework.

Do not over-normalize the JSON.

Do not introduce architectural complexity unless the current requirements actually need it.

The sentence JSON should remain human-editable.

Add comments only where they genuinely clarify non-obvious behaviour.

---

# 22. Acceptance criteria

The project is complete when:

1. I can open the app.
2. I can choose A, B or C.
3. A sentence from that level appears.
4. All answer options are visible.
5. I can select one answer.
6. I immediately see Correct or Incorrect.
7. I always see the correct answer.
8. I always see a short explanation of why it is correct.
9. The reference tables remain visible at the top.
10. I can click Next Sentence.
11. I can press N to go to the next sentence.
12. I can enable Random mode.
13. Random mode cycles through a shuffled set without excessive repetition.
14. Changing levels loads the appropriate static JSON data.
15. There are no runtime AI/API calls.
16. The UI remains minimal and distraction-free.
17. It works well on desktop and mobile.
18. The codebase can later support approximately 4,000–5,000 JSON exercises without architectural changes.

---

# 23. Deliverables

Produce the complete runnable project.

Include:

- project folder structure
- all source files
- sample JSON datasets
- reference table data
- responsive CSS
- keyboard shortcut implementation
- random/shuffle behaviour
- JSON validation script
- README with simple run instructions

After writing the implementation, review the project once specifically for unnecessary complexity.

Remove anything that does not directly support the core practice loop.

Do not merely explain how to build it.

Build the actual implementation.
