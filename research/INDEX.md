# Research index

Every note lives in `research/notes/` and starts with a header like this:

```
---
topic: one-line description
tags: comma, separated, kebab-case, tags
works: Titles, Authors, Games named in the note
---
```

Every note is split into numbered questions (`## 1. ...`), and every question has the same four subsections:

- `### Takeaway`: the answer in two or three sentences
- `### Cited Findings`: sourced facts, each with a link
- `### Inferences`: the researcher's own reasoning, not sourced
- `### Gaps`: what could not be sourced or verified

`REPORT.md` is the compiled synthesis, with the writers' principles, checklist and trope table at the end.

## Grep cheatsheet

```sh
# Which notes cover a tag or a work?
grep -l "^tags:.*time-travel" research/notes/*.md
grep -l "^works:.*Halo" research/notes/*.md

# One-line topic of every note
grep -h "^topic:" research/notes/*.md

# All takeaways (the fastest skim of everything)
grep -n -A3 "^### Takeaway" research/notes/*.md

# Everything unverified, to know what not to lean on
grep -n -A6 "^### Gaps" research/notes/*.md

# Every question asked, across all notes
grep -n "^## " research/notes/*.md

# Any keyword, case-insensitive, with context
grep -rni -C2 "foreshadow" research/

# Writers' checklist and trope table in the report
grep -n -A80 "^### Checklist" research/REPORT.md
grep -n -A30 "^### Tropes to avoid" research/REPORT.md
```

## Notes

| File | Topic |
|---|---|
| `complex_anime_and_japanese_games.md` | How complex anime and Japanese games structure and stage their reveals (Code Geass, NieR, Evangelion, Attack on Titan, Madoka, 13 Sentinels, Zero Escape) |
| `complex_scifi_and_fantasy.md` | Western sci-fi and fantasy reveal structure; AGI, aliens, cloning and time-travel treatments; why mystery boxes fail |
| `game_of_thrones_thread_structure.md` | How Game of Thrones keeps many threads clear, makes shocks fair, and why season 8 failed |
| `steins_gate_case_study.md` | Steins;Gate: teaching time-travel rules, wishes and costs, the ending's loophole |
| `mystery_stories_and_mystery_games.md` | Fair-play mystery craft and deduction-by-mechanics game design (Obra Dinn, Outer Wilds, Golden Idol) |
| `what_makes_stories_gripping.md` | Psychology and craft research on curiosity, suspense, twists, characters, pacing and endings |
| `overused_tropes_to_avoid.md` | Worn-out tropes and predictable twists per theme, with fresher directions |
| `worldbuilding_and_lore.md` | Iceberg lore and worldbuilding, with Halo as the case study |
| `story_development_methods.md` | Step-by-step methods from one sentence to a full outline (Snowflake, beat sheets, backward design) |
| `where_writers_start.md` | Where pros start (character, world, theme, premise, ending, image) and what each produces |
| `epic_and_game_story_planning.md` | How TV rooms, Pixar, game studios and epic authors plan long multi-thread stories, and the documents they use |
| `escalating_scale_epics.md` | The Expanse, The Lord of the Rings, Interstellar: growing scale and most loved moments |
| `character_growth_stories.md` | Ted Lasso, The Martian, Gladiator: growing characters and most loved moments |
| `fresh_premises_and_rehash_sequels.md` | What makes a premise new (Pacific Rim, Avatar) and why the Avatar sequels feel rehashed |
