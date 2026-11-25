# Round 3 writer instructions

Shared instructions for the three round-3 writers. Each writer's prompt adds its starting point and its seeds (from `outlines/seeds/round-3.md`).

## Why there is a round 3

- **Round 1:** all three writers converged on one template: a northern-European sea coast, a drowning, an alien tied to sound, and a roughly 19-year cycle.
- **Round 2:** random seeds broke that convergence, but the stories came out small and folk-scale: an island, a single city, a buffalo-drawn caravan.
- **Owner's clarification:** the story must be big, futuristic science fiction, with galactic reach, spy and court intrigue, politics and economic systems. This is now in `BRIEF.md`, "Scope and genre".

Rounds 1 and 2 are in `outlines/archive/` with their reviews in `judging/archive/`. The owner wants totally new stories: do not open or draw on anything in the archive, including mechanics.

## Read first, in full

1. `BRIEF.md`, especially the new "Scope and genre" section. It is the scoring standard.
2. `research/REPORT.md`, especially "Sixteen working principles", "Checklist to run on every draft", "Tropes to avoid, and what to do instead" and "Development process for the writers".
3. As needed, `research/notes/` (see `research/INDEX.md`). For this round, `complex_scifi_and_fantasy.md`, `complex_anime_and_japanese_games.md` (Code Geass) and `game_of_thrones_thread_structure.md` matter most.

Do not open the other round-3 writers' folders.

## Scope requirements (all mandatory)

- **Big, futuristic science fiction.** AGI, aliens and time travel appear as advanced technology and civilisations. Cloning is included too.
- **Interstellar or galactic reach.** Several worlds, polities and at least one non-human species are in play.
- **Spy and court intrigue.** Agents, double agents, factions at court, succession and power struggles.
- **Politics and economic systems that drive the plot.** Who controls which resource, and how markets, debt, trade and power work. The mystery must move these, and they must move the mystery.
- **Start small and personal, inside that big world.** One human anchor, then widen to a galaxy-scale stake, with every jump earned.

## Banned: the averages from rounds 1 and 2

- A society whose founding secret is a debt, pledge or promise to a bound, captive, buried or dying alien that it lives off, settled in person at the end. All four round-2 stories had this shape.
- A small village, island or single isolated community as the whole world.
- A drowning, or a body found in water, as the inciting death.
- An alien that communicates only through sound, song, echoes or the voices of the dead.
- Time travel tied to a fixed interval of years or a lunar cycle.

## Banned: space-opera averages

- A generic "Galactic Empire", "Federation", "Republic" or "Alliance", and the names Emperor Xyz, House Atreides-like dynasties, Spice-like commodities and Jedi-like orders.
- A precursor gate network built by a vanished race that explains everything.
- The AI uprising, the AI god as final boss, and the AI that was good all along.
- Lookalikes of Dune, Foundation, Star Wars, Mass Effect, The Expanse, Hyperion or Code Geass in setting, factions or signature beats. Borrow techniques only, and log the nearest works and how yours differs.

## Seeds (mandatory)

- Every seed must visibly shape the story.
- The galactic setting, intrigue, economic-system and technology seeds set the scale and the plot engine.
- Culture/era is a naming and texture source for a future culture, not a historical setting.
- A seed may be reinterpreted, but never silently dropped.
- Record your seeds at the top of `01-options.md`. In `07-self-check.md`, say where each one landed.

## Process

- Follow the 13-step development process in `REPORT.md`.
- At every step marked "(three options)", write at least three genuinely different options. They must not be variations of one idea or one-line strawmen set up to lose.
- Judge the options against the brief, pick one and say why.
- Reject the first idea that comes to mind if it is the obvious one.
- No generic sci-fi names (Elara, Kael, Nexus, Aether, Project Genesis and so on). Derive names from your seeded culture and its future evolution.

## Rules

- **Original:** borrow techniques, never content.
- **Deep but never confusing:** at any moment the player knows what each character wants and what the current question is. Hold yourself to the thread budget (about three plot lines, four to six active threads).
- **Unpredictable but fair:** many unforeseen deaths, betrayals and reversals, each planted. Betrayals should be the spy-thriller kind.
- **Tropes are a review prompt, not a ban:** log each match and say whether you kept it.
- **Each pillar generates its own scene type or investigative verb,** and the pillars collide. The pillars are AGI, aliens, cloning and time travel.
- **Iceberg lore** with a founding crime or lie, and a main path that stands on its own.
- **Solve by doing,** not point-and-click or reading.
- **Seal the hidden history so it is fully consistent.** Check every date and every application of every rule across all files.
- **At committed choices, refusal and inaction are respected outcomes.**

## Deliverables

Write these files in your folder, `outlines/writer-{a,b,c}/`. Commit after each one:

```sh
cd /home/user/mystery-game-story-lab && scripts/commit.sh "Writer X: <what>" outlines/writer-x/<file>
```

1. **`01-options.md`:** the seeds, then the three-option rounds, each with its pick and the reason. Rounds: setting and scale, central question, hidden history, ending, world rules per pillar, the political and economic system, founding crime, the intrigue structure (who spies on whom), main characters and names, premise sentence, key scenes.
2. **`02-hidden-history.md`:** the sealed true chronology and ending (the solution document).
3. **`03-world-and-factions.md`:** world rules with limits and costs; the polities, factions and courts; the economic system and how it works; iceberg lore tagged promised or texture.
4. **`04-characters.md`:** characters with wants, false beliefs, secrets, loyalties and double loyalties, growth paths and trap doors; the human anchor.
5. **`05-outline.md`:** the main deliverable. A single sentence, a paragraph, then the full outline act by act and thread by thread. Include the reveal order, the thread grid summary, and how gameplay delivers each revelation. At least 2,000 words; more is welcome.
6. **`06-key-scenes.md`:** scene sketches at key points: the opening, the major reveals, the midpoint, the climax, the ending and the most memorable moments. Each shows what the player does and sees, with little or no reading.
7. **`07-self-check.md`:** the report's checklist, the trope table, both banned lists, the scope requirements, and where each seed landed. Do not mark an item Pass unless it passes.

Run no git commands other than `commit.sh`, and do not push.
