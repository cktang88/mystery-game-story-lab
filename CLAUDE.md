# mystery-game-story-lab

Story development for an original mystery video game (AGI, aliens, cloning, time travel; not point-and-click, not text-heavy).

When starting a session, read these first:
1. `HANDOFF.md`: current status, next steps, and ready-to-use subagent prompts for the writers, graders and Fable judge.
2. `BRIEF.md`: the owner's requirements, which are the scoring standard for all work.
3. `CONVERSATION.md`: the full conversation so far, if you need the owner's exact words.

Conventions:
- Commit small and often with `scripts/commit.sh "subject" path ...`, then `git push origin main`.
- Research is in `research/` (see `research/INDEX.md` for grep tips). Outlines go in `outlines/writer-{a,b,c}/`; reviews and the verdict go in `judging/`.
- Never plagiarize: borrow techniques, never content. Tropes are a review prompt, not a ban. Generate three options for every important element and have a separate grader pick.
