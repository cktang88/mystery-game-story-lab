"""Add a grep-friendly front-matter header to each research note.

Usage: python3 scripts/add_front_matter.py
Skips files that already start with '---'.
"""
import pathlib

NOTES = pathlib.Path(__file__).resolve().parent.parent / "research" / "notes"

META = {
    "complex_anime_and_japanese_games.md": (
        "How complex anime and Japanese games structure and stage their reveals",
        "anime, jrpg, reveal-ladder, twists, endings, routes, replay, foreshadowing, knowledge-locks, us-them-collapse, setting-as-lie, backward-design, failures",
        "Code Geass, NieR Replicant, NieR Automata, Steins;Gate, Evangelion, Attack on Titan, Monster, Madoka Magica, Legend of the Galactic Heroes, Fullmetal Alchemist Brotherhood, Death Note, Higurashi, Umineko, From the New World, 13 Sentinels, Zero Escape, Virtue's Last Reward, Xenogears, Xenoblade",
    ),
    "complex_scifi_and_fantasy.md": (
        "Western sci-fi and fantasy reveal structure; AGI, aliens, cloning, time travel; mystery-box failure",
        "scifi, fantasy, multi-thread, pov, time-travel-models, agi, aliens, cloning, identity, mystery-box, failure, season-8",
        "A Song of Ice and Fire, Game of Thrones, Hyperion, Three-Body Problem, Book of the New Sun, Malazan, Blindsight, Never Let Me Go, Story of Your Life, Arrival, Dark, Westworld, Primer, Lost, Battlestar Galactica, Severance, Outer Wilds, SOMA, BioShock, Disco Elysium",
    ),
    "game_of_thrones_thread_structure.md": (
        "How A Song of Ice and Fire / Game of Thrones keeps many threads clear and makes shocks fair",
        "multi-thread, pov, convergence, information-asymmetry, shocks, fair-surprise, thread-budget, map, meereenese-knot, season-8, failure",
        "A Song of Ice and Fire, Game of Thrones",
    ),
    "mystery_stories_and_mystery_games.md": (
        "Fair-play mystery craft and deduction-by-mechanics game design",
        "mystery, fair-play, clues, red-herrings, twists, whodunit, inverted, deduction, knowledge-gating, metroidbrainia, low-text, mechanics, batch-validation",
        "Knox, Van Dine, Agatha Christie, Roger Ackroyd, Devotion of Suspect X, Decagon House, Knives Out, Twin Peaks, True Detective, Return of the Obra Dinn, Outer Wilds, Case of the Golden Idol, Her Story, Unheard, Lacuna, Paradise Killer, Forgotten City, Deathloop, Sexy Brutale",
    ),
    "overused_tropes_to_avoid.md": (
        "Overused tropes and predictable twists in AGI, alien, clone, time-travel and mystery stories, with fresher directions",
        "tropes, cliches, predictable-twists, subversion, agi, aliens, cloning, time-travel, mystery, jrpg, plagiarism, originality",
        "TV Tropes, Strange Horizons, Clarkesworld, Outer Wilds",
    ),
    "steins_gate_case_study.md": (
        "Steins;Gate as a case study in deep but understandable time-travel storytelling",
        "time-travel, rules, teaching-rules, pacing, midpoint, wishes-and-costs, foreshadowing, ending, loophole, convergence, phone-trigger, blueprint",
        "Steins;Gate, Steins;Gate 0",
    ),
    "story_development_methods.md": (
        "Step-by-step methods for growing a story from one sentence to a full outline",
        "process, outlining, snowflake, logline, premise, beat-sheet, save-the-cat, story-circle, seven-point, truby, kishotenketsu, discovery-writing, backward-design, plot-grid, therefore-but",
        "Snowflake Method, Save the Cat, Dan Harmon, Dan Wells, John Truby, Lisa Cron, Brandon Sanderson, Stephen King, George R.R. Martin, Agatha Christie, Kotaro Uchikoshi, Edgar Allan Poe, J.K. Rowling",
    ),
    "what_makes_stories_gripping.md": (
        "Psychology and craft research on curiosity, suspense, twists, characters, pacing and endings",
        "curiosity, information-gap, suspense, surprise, transportation, cliffhangers, spoilers, twists, characters, pacing, endings, peak-end, player-guilt, games",
        "Loewenstein, Brewer and Lichtenstein, Green and Brock, Vera Tobin, McKee, Truby, Storr, Cron, Sanderson, Pixar, Parker and Stone, Aristotle, Spec Ops, Outer Wilds",
    ),
    "where_writers_start.md": (
        "Where professional writers start a story (character, world, theme, premise, ending, image) and how it shapes the work",
        "process, starting-point, character-first, world-first, theme-first, premise-first, ending-first, image-first, reveal-order",
        "Stephen King, Ray Bradbury, Lisa Cron, Pixar, Tolkien, Frank Herbert, N.K. Jemisin, Le Guin, Bungie, Ted Chiang, Yoko Taro, Kotaro Uchikoshi, Philip K. Dick, Poe, J.K. Rowling, Dark, Christopher Nolan, C.S. Lewis, Faulkner",
    ),
    "worldbuilding_and_lore.md": (
        "Worldbuilding and iceberg lore, with Halo as the central case study",
        "worldbuilding, lore, iceberg, deep-history, ancient-crime, founding-lie, factions, hard-magic, rules, environmental-storytelling, low-text, lore-dump, failures",
        "Halo, Forerunners, Flood, Covenant, Tolkien, Hemingway, M. John Harrison, Frank Herbert, Iain M. Banks, N.K. Jemisin, Le Guin, Sanderson, Dark Souls, Elden Ring, Bloodborne, Elder Scrolls, Mass Effect, Destiny",
    ),
    "escalating_scale_epics.md": (
        "How The Expanse, The Lord of the Rings and Interstellar grow in scale, and their most loved moments",
        "scale, escalation, growing-larger, convergence, human-anchor, beloved-moments, quotable, endings",
        "The Expanse, The Lord of the Rings, Interstellar",
    ),
    "character_growth_stories.md": (
        "How Ted Lasso, The Martian and Gladiator grow their characters and stakes, and their most loved moments",
        "character-growth, side-characters, escalation, growing-larger, beloved-moments, quotable, payoffs",
        "Ted Lasso, The Martian, Gladiator",
    ),
    "fresh_premises_and_rehash_sequels.md": (
        "What makes a premise genuinely new (Pacific Rim, Avatar) and why the Avatar sequels feel rehashed",
        "premise, originality, something-new, high-concept, worldbuilding, sequels, rehash, escalation-without-ideas",
        "Pacific Rim, Avatar, Avatar The Way of Water, Avatar Fire and Ash, Aliens, Terminator 2, Empire Strikes Back, Mad Max Fury Road, Dune Part Two",
    ),
    "epic_and_game_story_planning.md": (
        "How TV rooms, animation studios, game studios and epic authors plan long multi-thread stories",
        "process, writers-room, season-arc, series-bible, storyboarding, pixar, game-narrative-pipeline, flowcharts, clue-matrix, three-clue-rule, knowledge-gates, continuity, planning-documents",
        "Breaking Bad, Dark, Lost, Battlestar Galactica, Severance, The Wire, Babylon 5, Pixar, Hayao Miyazaki, Naughty Dog, Bungie, Remedy, Outer Wilds, Zero Escape, 13 Sentinels, Return of the Obra Dinn, J.K. Rowling, Sanderson, One Piece",
    ),
}


def main():
    for path in sorted(NOTES.glob("*.md")):
        text = path.read_text()
        if text.startswith("---"):
            continue
        if path.name not in META:
            print(f"no metadata for {path.name}, skipped")
            continue
        topic, tags, works = META[path.name]
        header = f"---\ntopic: {topic}\ntags: {tags}\nworks: {works}\n---\n\n"
        path.write_text(header + text)
        print(f"added front matter: {path.name}")


if __name__ == "__main__":
    main()
