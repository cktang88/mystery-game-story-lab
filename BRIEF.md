# Story brief

Constraints from the project owner, in priority order.

## The game

- A mystery game that is **not** point-and-click and **not** text-reading spam.
- The player solves things by doing (reconstructing scenes, loops, stealth, forensics, audio, photography), not by reading walls of dialogue.

## The story

- As complex and interesting as Code Geass or NieR, and then more so.
- Built around AGI, aliens, cloning and time travel.
- Insane and memorable underneath, but **everything must make sense**.
- Layered like Game of Thrones: multiple character threads that run in parallel and converge.
- Unveiled bit by bit over time.

## Scope and genre

- Big, futuristic science fiction, not folk or rustic fantasy. AGI, aliens and time travel are front and centre as advanced technology and civilisations, not as folklore, relics or a creature under a village.
- Wide scale: interstellar or galactic reach, multiple worlds, polities and species in play.
- Spy and court intrigue: agents, double agents, factions at court, succession and power struggles, in the Code Geass mode.
- Politics and economic systems that drive the plot: who controls what resource, how markets, debt, trade and power work, and how the mystery moves them.
- It can still start small and personal (see "Growing larger"), but the world it opens onto must be this big from the start, and the small hook should already sit inside it.

## Tone: cool, not spooky

- No spooky, horror, gothic, occult or morbid material: no ghosts or hauntings, no death omens or shadows of the dead, no funerals, pyres, corpse rites, crypts, graves or bodies as ritual objects, no ordeals or trials by superstition.
- The tone is cool: sleek, thrilling and awe-inspiring. Think spy craft, heists, chases, high-tech investigation, court duels of wits, starships, megastructures, alien civilisations and big reveals.
- Crime is fine (an assassination, sabotage, a heist, a disappearance), played as a thriller, not dwelt on morbidly.
- Nothing horror or gross. No body horror: no mutation, flesh merging, grafting tissue, parasites, rot, decay, gore or creatures growing out of people. The owner found the film Annihilation too gross; that is the line. Biotech, clones and aliens should look clean, elegant and high-tech (sleek vats, not wet flesh), and alien life should inspire awe, not disgust.

## Something new

- It must add something genuinely new, not be yet another entry in the genre.
- Aim for a premise as striking as Pacific Rim's or the first Avatar's, where the core idea itself generates new kinds of scenes and dilemmas.
- Anti-model: the Avatar sequels, seen by the owner as rehashing and extending the first film without adding to the story. Spectacle, new locations and higher scale are not new ideas.

## Growing larger

- The story and its characters should keep getting bigger, in the way The Expanse, Ted Lasso, The Martian, Interstellar, Gladiator and The Lord of the Rings do.
- Start small and personal, then widen to a world-scale stake, with every jump earned and a small human anchor kept throughout.
- Side characters grow into full arcs.
- Build in moments worth remembering and quoting, set up by small details planted early.

## Worldbuilding and lore

- A good story rests on good worldbuilding.
- Iceberg model, as in Halo: what the player explores is only the tip of a much larger, crazier lore, and sensing the rest beneath is what makes it fun to play.
- The world should have deep history, factions and rules that exist beyond what the plot needs, revealed in glimpses.

## Process

- Develop the story the way professionals do, with no shortcuts.
- Expand in stages, from a one-sentence premise to a paragraph, a page and a full outline, checking cause and effect at each stage.
- Fix the ending and the true hidden history first, then plant forward.

## Fighting the average

- LLM writing collapses to the mean: generic plots, settings, twists and names (the Elaras, Kaels, Nexus Corps and Project Genesis of the world).
- For every important element (premise, hidden history, twists, characters, names, setting, ending), generate at least three genuinely different options.
- A separate grader reviews and revises the options, then picks one, instead of the first idea standing by default.
- Names in particular should come from a specific culture, era and logic in the world, never from the generic sci-fi name pool.
- Random seeds are mandatory. Before writing, every writer draws a seed set with `python3 scripts/seeds.py` (culture/era, terrain, professions, objects, phenomena, material, relationship, ritual, creature or plant), with no seed shared between writers in a round. Every seed must visibly shape the story and may be reinterpreted but never silently dropped. Round 1 showed why: three writers with different starting points still converged on the same northern-sea template, because instructions to avoid the average make every copy of the model pick the same "non-obvious" choice.

## Original

- Never plagiarize. Be inspired by the great stories, but copy no plots, characters, names, settings, signature twists or lines from them.
- Borrow techniques (how reveals are paced, how threads converge), not content.
- Tropes are a review prompt, not a ban. When a beat matches a common trope (see TV Tropes), stop and ask whether a better story opportunity exists there.
- If the trope is still the best choice for the story, keep it. Never bend a good story backwards just to dodge a trope.

## Unpredictable

- Lots of moments the player does not see coming: deaths, betrayals, reversals, reveals.
- Each one must be fair in hindsight, set up by things the player already saw.

## Deep, not confusing

- The model is Game of Thrones before season 8: many people follow it easily, yet it is deep because of the many character threads.
- Depth comes from characters, motives and consequences, not from being hard to follow.
- At any moment the player should know what each character wants and what the current question is.
- The ending must be earned and paced. Season 8 is the anti-model: rushed, with payoffs that the setup did not support.
