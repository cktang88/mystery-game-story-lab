# Handoff: where this project stands and what to do next

Read this first when continuing in a new session. The full conversation is in `CONVERSATION.md`, the owner's requirements in `BRIEF.md`.

## What the owner wants

A mystery video game story that is **not point-and-click and not text-heavy**, built on **AGI, aliens, cloning and time travel**, as deep and memorable as Code Geass, NieR and Steins;Gate, with Game of Thrones–style interwoven character threads, but never confusing. All the rules are in `BRIEF.md`; it is the scoring standard for everything below.

The deliverable the owner asked for:

1. Research on great complex stories, what makes stories gripping, mystery design, worldbuilding, professional story planning, growing scale, and fresh premises, compiled in a repo (**done**).
2. **Three writer subagents**, each producing a giant (2,000+ words; aim higher) story outline with scene sketches at key points (**not started**).
3. **A judge subagent running the Fable model** (`model: "fable"` on the Agent tool) that compares and contrasts the three outlines (**not started**).
4. **Small, frequent commits** throughout, pushed to `cktang88/mystery-game-story-lab`.

## Status

| Stage | State | Where |
|---|---|---|
| Brief | Done; grew with each owner message | `BRIEF.md` |
| Research notes (14) | Done, ~82k words | `research/notes/` |
| Compiled report | Done, ~13.8k words; ends with 16 principles, checklist, trope table, 13-step development process | `research/REPORT.md` |
| Research index and grep cheatsheet | Done | `research/INDEX.md` |
| Three writer outlines, round 1 | Done. A, B and C all converged on one template (northern-European sea coast, drowning, sound-based alien, ~19-year cycle) | A kept in `outlines/writer-a/`; B and C v1 in `outlines/archive/` |
| Graders' reviews, round 1 | Done. A 7.5, B 7, C 6.6 out of 10 | `judging/review-writer-a.md`; B and C v1 reviews in `judging/archive/` |
| Writer A revision | In progress (adds `08-revision-log.md`) | `outlines/writer-a/` |
| Writers B and C, round 2 | In progress. The owner chose to redo both under a banned list of the converged elements. B must use a dense non-European city (world first); C must be off-world or mobile (ending first) | `outlines/writer-b/`, `writer-c/` |
| Graders for B and C v2, then their revisions | After round 2 | `judging/` |
| Fable judge's comparison | Last | `judging/` |

## Repo conventions

- Commit with `scripts/commit.sh "subject" path [path ...]`. It commits only the given paths, retries on the git index lock (safe for parallel subagents), and adds the attribution trailer. Then `git push origin main`. The owner said to always work on and push to the default branch (`main`).
- A harmless `push negotiation failed` / `expected 'acknowledgments'` warning appears on push; the push still succeeds.
- Research notes start with `topic:` / `tags:` / `works:` front matter. New notes get it from `scripts/add_front_matter.py`, whose `META` dict needs an entry per new file.
- Each note's questions have `### Takeaway`, `### Cited Findings`, `### Inferences` and `### Gaps` subsections.
- **Subagent quirk:** a subagent running the deep-research report-writer instructions refused to write `REPORT.md` and returned the text instead. If that happens, save the text yourself. Writer and grader subagents not using that skill should write files normally.

## Planned writing pipeline

This design came from the owner's messages: three writers, the generate-three-and-grade rule against LLM mean collapse, separate graders, and a Fable judge.

**Stage 1: three writers in parallel.** Each gets a different professional starting point, so the three don't converge on the same average story (per `research/notes/where_writers_start.md`):
- **Writer A, question first:** begins from a central question that AGI, aliens, cloning and time travel each test differently.
- **Writer B, world first:** begins from an ancient crime or founding lie beneath the world (Halo-style iceberg), deriving factions from it.
- **Writer C, ending first:** begins from the final emotional image and key anchor scenes, building backward (Yoko Taro / Uchikoshi style).

Each writer follows the 13-step "Development process for the writers" in `research/REPORT.md`, generating at least three genuinely different options at every step marked "(three options)", and commits after each file.

**Stage 2: three graders in parallel, one per outline.** Each grader has not seen the other outlines. It reviews against `BRIEF.md` and the report's checklist and trope table, flags generic, confusing, trope-default or unearned elements, and writes concrete required revisions to `judging/review-writer-X.md`.

**Stage 3: writers revise.** Continue each writer subagent with its review (SendMessage keeps its context), or start a fresh agent with the review plus its files. The writer applies the revisions and logs what changed and why.

**Stage 4: the Fable judge** (`model: "fable"`). It reads the brief, the report's principles and checklist, and the three final outlines; scores each against the brief; compares and contrasts them; and picks a winner or the best combination, with what to take from each. It writes `judging/verdict.md`.

Commit and push after each stage. Then give the owner a short summary of the verdict and the outlines.

**Seeds (added after round 1 converged).** Before launching writers, run `python3 scripts/seeds.py --writers <names>` and save the output under `outlines/seeds/`. Paste each writer's set into its prompt with the rules from the script's docstring. Round-2 seeds are in `outlines/seeds/round-2.md`.

### Writer prompt template

Fill in `{X}` (a, b or c) and `{STARTING POINT}`:

```
You are Writer {X} on an original mystery video game story. Work in /home/claude/mystery-game-story-lab/outlines/writer-{X}/ only.

Read first, in full:
- /home/claude/mystery-game-story-lab/BRIEF.md (the owner's requirements; they are the scoring standard)
- /home/claude/mystery-game-story-lab/research/REPORT.md (especially "Sixteen working principles", "Checklist to run on every draft", "Tropes to avoid, and what to do instead", and "Development process for the writers")
- Grep research/notes/ for anything you need in more depth (see research/INDEX.md for a cheatsheet).

Your starting point: {STARTING POINT}. The other two writers start elsewhere, so lean fully into yours.

Follow the 13-step development process in REPORT.md. At every step marked "(three options)", write at least three genuinely different options (not variations of one idea), judge them against the brief, pick one, and say why. LLMs collapse to the average: reject the first idea that comes to mind if it is the obvious one, and never use the generic sci-fi name pool (Elara, Kael, Nexus, Aether, Project Genesis and so on). Derive names from a specific culture, era and logic inside your world.

Rules:
- Original: borrow techniques, never plots, characters, names, settings or signature twists from existing works.
- Deep but never confusing: at any moment the player knows what each character wants and what the current question is.
- Many unpredictable moments, each fair in hindsight via planted clues.
- Tropes are a review prompt, not a ban: when a beat matches a common trope, log it and ask whether there is a better opportunity; keep it only if it is still the best choice.
- Something genuinely new: each pillar (AGI, aliens, cloning, time travel) must generate a kind of scene or investigative verb the others cannot, and the four must collide.
- Iceberg lore with a founding crime or lie; a self-sufficient main path.
- The story and its characters grow larger, around one fixed human anchor.
- Gameplay is solving by doing (reconstruction, loops, audio, identity attribution, etc.), not point-and-click or reading.

Write these files, committing after each one with:
  /home/claude/mystery-game-story-lab/scripts/commit.sh "Writer {X}: <what>" outlines/writer-{X}/<file>
1. 01-options.md: the three-option rounds for the central question, hidden history, ending, world rules per pillar, founding crime, main characters and names, premise sentence, and key scenes, with the pick and the reason for each.
2. 02-hidden-history.md: the sealed true chronology and ending (the solution document).
3. 03-world-and-factions.md: world rules with limits and costs, factions, iceberg lore tagged promised or texture.
4. 04-characters.md: characters with wants, false beliefs, secrets, growth paths, trap doors; the human anchor.
5. 05-outline.md: the main deliverable. A single sentence, a paragraph, then the full outline act by act and thread by thread, with the reveal order, the thread grid summary, and how gameplay delivers each revelation. At least 2,000 words; more is welcome.
6. 06-key-scenes.md: scene sketches at key points (the opening, the major reveals, the midpoint, the climax, the ending, and the most memorable moments), each showing what the player does and sees, with little or no reading.
7. 07-self-check.md: run the report's checklist and trope table against your story; list what passes, what fails and what you fixed.

Do not run git commands other than commit.sh, and do not push. Reply with a 150-word summary of your story and the file list.
```

### Grader prompt template

```
You are an independent grader. You did not write this story and have not seen the other writers' work. Review /home/claude/mystery-game-story-lab/outlines/writer-{X}/ (all files) against /home/claude/mystery-game-story-lab/BRIEF.md and the principles, checklist and trope table in /home/claude/mystery-game-story-lab/research/REPORT.md.

Be demanding. Look specifically for:
- generic or averaged choices (names, premise, factions, twists);
- options in 01-options.md that are variations of one idea rather than genuinely different;
- anything confusing, or any point where the player wouldn't know the current question;
- unfair or unearned twists;
- tropes used by default rather than chosen;
- pillars that decorate rather than generate scenes;
- payoffs without setups;
- text-heavy delivery;
- season-8-style rushed convergence;
- missing growth or a missing human anchor.

Write /home/claude/mystery-game-story-lab/judging/review-writer-{X}.md with: a score out of 10 per brief section, the top strengths, and a numbered list of concrete required revisions (what to change and a suggested direction). Where you would pick a different option from 01-options.md, say which and why.

Commit it with:
  /home/claude/mystery-game-story-lab/scripts/commit.sh "Grade writer {X}" judging/review-writer-{X}.md
Do not run other git commands.
```

### Judge prompt (run with `model: "fable"`)

```
You are the judge. Read /home/claude/mystery-game-story-lab/BRIEF.md, the principles, checklist and trope table in /home/claude/mystery-game-story-lab/research/REPORT.md, the three graders' reviews in judging/, and all files in outlines/writer-a/, writer-b/ and writer-c/ (the revised versions).

Compare and contrast the three stories:
- premise freshness;
- depth without confusion;
- unpredictability and fairness;
- thread structure;
- iceberg lore;
- growth;
- originality;
- how well each pillar generates gameplay;
- the strength of the key scenes and ending;
- any risk of a season-8 ending.

Score each against every section of the brief, then pick a winner or recommend a specific combination (what to take from each, and why the pieces fit). End with the five biggest open problems in the winning direction.

Write /home/claude/mystery-game-story-lab/judging/verdict.md and commit it with:
  /home/claude/mystery-game-story-lab/scripts/commit.sh "Judge's verdict" judging/verdict.md
Do not run other git commands.
```

## Open questions for the owner (none blocking)

- Platform, scope and length of the game are unspecified. The report's mechanics evidence comes from short games (around 3 to 10 hours), and whether deduction-by-doing scales to a long game is the main unproven risk.
- Photography, stealth tailing and hands-on forensics mechanics have no sourced precedent in the research.
