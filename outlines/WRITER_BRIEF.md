# Writer brief for the outline stage

Three writers each develop one complete, independent story outline. A separate judge compares them afterwards (see `judging/`). This file is the shared instruction set; each writer also has a distinct **starting point** (below) so the three outlines do not converge on the same average idea.

## Read first

1. `BRIEF.md`: the owner's requirements. Every section is binding.
2. `research/REPORT.md`: the synthesis, especially the twelve principles, the checklist and the trope table.
3. `research/INDEX.md`, then the notes most relevant to your starting point. At minimum skim the takeaways (`grep -n -A3 "^### Takeaway" research/notes/*.md`) and read `fresh_premises_and_rehash_sequels.md`, `escalating_scale_epics.md`, `character_growth_stories.md` and `worldbuilding_and_lore.md`, which postdate the report.

Do **not** open the other writers' folders under `outlines/`. Independence is the point.

## Starting points

- **Writer A, ending and hidden history first.** Fix the final scene, the true chronology and the price the ending pays before anything else, then work backward to what the player must have seen.
- **Writer B, core mechanic and premise first.** Find one Pacific Rim-grade idea that is simultaneously the world's central fact and the player's main verb, so the premise itself generates new kinds of scenes, dilemmas and deductions.
- **Writer C, world and factions first.** Build the iceberg: deep history, factions with visible incentives, a founding lie. Let the cast and the mystery grow out of institutions, the sociological Game of Thrones mode.

Whatever the starting point, every outline must end up with all the deliverables below, and the ending and hidden history must be fixed before scenes are written.

## Process rules (from the brief)

- **Three options minimum** for each important element: premise, hidden history, central twist(s), main characters, names and naming logic, setting, ending. Options must be genuinely different, not variations. Then grade them honestly in writing (what each does for the brief, what is generic about it), revise, and pick. Never let the first idea win by default.
- **Fight the mean.** No Elaras, Kaels, Nexus Corps, Project Genesis. Names come from a specific culture, era and in-world logic, explained in a naming note.
- **Staged expansion.** One sentence → one paragraph → one page → full outline. Check "therefore/but" causality at each stage.
- **Trope review, not trope ban.** When a beat matches a common trope, note it, ask whether a better opportunity exists, and keep it if it is still best.
- **No plagiarism.** Borrow techniques, not content. Keep an influence log: element → technique borrowed → from which works.
- **Game, not novel.** Every major revelation must be reached by a player action (reconstructing, scrubbing audio, attribution, loops, photography, stealth, forensics, etc.), not by reading. Say which verb unlocks each reveal.

## Deliverables

Write into your own folder `outlines/<letter>_<short_slug>/`:

1. `01_options_and_grading.md`: the ≥3 options per element, the grading, the revisions and the picks, with reasons.
2. `02_premise.md`: the one-sentence premise, the paragraph, the one-page synopsis. State plainly what is genuinely new (the Pacific Rim test: what scenes and dilemmas could only exist in this story?).
3. `03_hidden_history_and_rules.md`: the true chronology (including everything before the game starts), each pillar's one mechanism, hard limit and human price (AGI, aliens, cloning, time travel), factions and their incentives, and the iceberg: lore that exists beyond what the plot needs and how it surfaces in glimpses.
4. `04_outline.md`: the full outline in acts or chapters. Threads (aim for about three plot lines, four to six active threads, each with place, look and want), the convergence order, the scale ladder from personal to world-scale with each jump earned, the human anchor, side characters' arcs, the reveal ladder and when each reveal lands, deaths, betrayals and reversals with their planted causes, and the ending.
5. `05_key_scenes.md`: six to ten key scene sketches, including the opening, the first major reveal, a midpoint reversal, the biggest shock, and the final scene. For each: what the player does (the verb), what they learn, what it reclassifies, and any quotable line with the small early detail that sets it up.
6. `06_self_audit.md`: run the REPORT.md checklist against your outline item by item; a dependency table (fact → where planted → where paid off, at least two routes for each critical fact); the trope review; the influence log; and an honest list of weaknesses.

Aim for depth over length: a complete, coherent story in roughly 8,000 to 15,000 words across the six files. Everything must make sense; if a rule or chronology step does not hold, fix it rather than hide it.

## Committing

Commit as you go with the helper, passing only your own folder's paths:

```sh
scripts/commit.sh "Outline A: options and grading" outlines/A_slug/01_options_and_grading.md
```

Do not push; the coordinator pushes.
