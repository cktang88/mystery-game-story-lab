# mystery-game-story-lab

Research and story development for a mystery game that is **not** point-and-click and **not** a wall of text, with a story aiming for Code Geass / NieR levels of layered complexity (AGI, aliens, cloning, time travel, multiple interwoven threads).

## Layout

- `HANDOFF.md` – status, next steps and subagent prompts (start here in a new session)
- `CONVERSATION.md` – the full conversation that produced this repo
- `BRIEF.md` – the owner's requirements for the story
- `research/INDEX.md` – index of all research, with a grep cheatsheet
- `research/notes/` – one note per topic, each with `topic:`, `tags:` and `works:` header lines
- `research/REPORT.md` – compiled synthesis, ending with the writers' principles, checklist and trope table
- `outlines/` – three independent story outlines with key scene sketches
- `judging/` – comparison and verdict on the outlines

Quick search: `grep -l "^tags:.*lore" research/notes/*.md` or `grep -n -A3 "^### Takeaway" research/notes/*.md`. More in `research/INDEX.md`.
