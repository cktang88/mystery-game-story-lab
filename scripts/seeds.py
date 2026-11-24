"""Draw random seed words for a writer, to break LLM mean collapse.

Why: in round 1, three writers with different starting points, the same model and
the same research all converged on one template (northern-European sea coast,
drowning, sound-based alien, ~19-year cycle). Instructions to "avoid the average"
do not help, because every copy of the model picks the same "non-obvious" choice.
Random external input does: each writer must build from a different, unchosen set.

Usage:
  python3 scripts/seeds.py                 # one seed set, cryptographically random
  python3 scripts/seeds.py --writers b c   # one set per writer, no repeats between them
  python3 scripts/seeds.py --exclude "Song dynasty" "beekeeper"

Rules for writers (also in BRIEF.md):
  - Every seed must visibly shape the story. Culture/era and terrain shape the
    setting and the naming logic; the profession seeds become main characters'
    jobs; the object, phenomenon and material seeds feed the pillars' mechanisms
    or the key recurring object; the relationship and ritual seeds feed a thread.
  - Record the seeds at the top of 01-options.md and, in 07-self-check.md, say
    where each one landed. A seed may be reinterpreted, never dropped silently.
  - The lists are deliberately broad. Add to them; never remove an entry because
    it seems hard to use. Hard seeds are the point.
"""
import argparse
import secrets

LISTS = {
    "culture_era": [
        "Kanem-Bornu Empire, 14th century", "Mughal Lahore, 1600s", "Song dynasty Hangzhou",
        "Edo-period Osaka merchant quarter", "Joseon Korea, 18th century", "Khmer Angkor, 12th century",
        "Majapahit Java", "Ottoman Aleppo caravanserais", "Safavid Isfahan", "Abbasid Baghdad, 9th century",
        "Aksumite Ethiopia", "Great Zimbabwe", "Swahili coast city-states", "Mali Empire Timbuktu",
        "Benin Kingdom bronze-casters", "Inca Cusco", "Moche Peru", "Classic Maya Tikal",
        "Aztec Tenochtitlan markets", "Mississippian Cahokia", "Haudenosaunee confederacy",
        "Polynesian Tonga, Tu'i Tonga era", "Hawaiian Kingdom, 1880s", "Yolngu Arnhem Land",
        "Mongol Karakorum", "Uyghur Turpan oasis", "Tibetan Lhasa, 1700s", "Bhutanese dzong culture",
        "Sri Lankan Anuradhapura", "Kerala spice ports, Zamorin era", "Chola Thanjavur",
        "Vijayanagara Hampi", "Armenian Ani, 11th century", "Georgian Tbilisi bathhouses",
        "Yemeni Shibam tower city", "Omani Nizwa falaj villages", "Nabataean Petra",
        "Sogdian Samarkand", "Bukhara emirate, 1800s", "Kazakh nomad hordes",
        "Sakha (Yakutia) reindeer herders", "Ainu Hokkaido", "Ryukyu Kingdom Shuri",
        "Philippine Sulu sultanate", "Malagasy Merina kingdom", "Zulu kingdom, 1820s",
        "Ashanti Kumasi goldweights", "Yoruba Ife", "Ethiopian Lalibela rock churches",
        "Coptic Egypt, 4th century", "Fatimid Cairo", "Berber Ghardaia (M'zab)",
        "Tuareg Saharan trade", "Brazilian quilombo Palmares", "Bolivian Potosí silver city",
        "Colonial Manila galleon trade", "Qing Guangzhou Thirteen Factories",
        "Meiji-era Tokyo", "1920s Shanghai", "1950s Bombay film studios", "1970s Lagos",
        "1960s Addis Ababa", "1980s Seoul", "Soviet Central Asian science towns",
        "Mexico City, 2080s", "Dhaka, 2070s", "Kinshasa, 2090s", "Jakarta, sinking 2060s",
        "Ulaanbaatar, 2100s", "far-future culture descended from Tamil diaspora",
        "far-future culture descended from Andean highlanders",
        "invented culture: river-barge clans with matrilineal debt law",
        "invented culture: salt-desert monastic accountants",
    ],
    "terrain": [
        "salt pan", "karst sinkhole field", "high-altitude plateau", "rainforest canopy",
        "mangrove-free river delta interior", "volcanic caldera", "glacier interior",
        "dune sea", "terraced rice mountains", "steppe grassland", "basalt columns",
        "underground aquifer city", "megacity rooftops", "abandoned mine galleries",
        "orbital ring habitat", "asteroid hollow", "gas-giant cloud platform",
        "generation ship hydroponics", "lunar lava tube", "tidally locked twilight band",
        "moving railway city", "nomad caravan route", "airship trade lane",
        "monsoon floodplain", "tea-estate hills", "bamboo forest", "cloud forest",
        "geothermal vents field", "open-pit mine", "cemetery city", "silk-road oasis",
        "arctic-free tundra plateau", "coral-free atoll lagoon (inland lake)",
        "spaceport sprawl", "data-centre desert", "flooded subway system",
    ],
    "profession": [
        "beekeeper", "translator of dead languages", "bonesetter", "court astrologer",
        "tax assessor", "perfumer", "glassblower", "kite maker", "puppeteer",
        "midwife", "embalmer", "cartographer", "locksmith", "bookbinder", "dye maker",
        "salt miner", "falconer", "tea taster", "calligrapher", "bell founder",
        "rice-paddy water warden", "insurance adjuster", "radio repairer",
        "elevator inspector", "stenographer", "court interpreter", "census taker",
        "pawnbroker", "funeral singer", "weather forecaster", "seed banker",
        "organ transplant coordinator", "tailor", "tattooist", "mapmaker of caves",
        "abacus teacher", "pharmacist", "clockmaker", "forger", "toy maker",
        "lighthouse-free signal-tower keeper", "railway switch operator",
        "hospice nurse", "notary of marriages", "sand mandala monk", "dentist",
        "museum restorer", "pigeon courier", "goat herder", "chess hustler",
    ],
    "object": [
        "abacus", "lacquered bento box", "brass astrolabe", "prayer wheel", "loom shuttle",
        "census ledger", "counterfeit coin", "porcelain teacup with a crack", "kite string",
        "hand fan", "wax seal", "embroidered sash", "seed packet", "dentures",
        "wind-up toy", "pressure cooker", "rubber stamp", "hourglass of black sand",
        "school uniform", "shadow puppet", "betel box", "a single chopstick",
        "x-ray film", "bus ticket", "tuning fork", "hearing aid", "dowry chest",
        "photograph with a face cut out", "leaky fountain pen", "beaded necklace",
        "ration card", "receipt", "insulin pen", "lottery ticket", "chess clock",
        "wedding henna stencil", "bicycle bell", "magnifying glass", "rosary of seeds",
        "skeleton key", "map with a hole", "glass eye", "scale weight", "padlock",
    ],
    "phenomenon": [
        "phantom limb", "echolocation", "bioluminescence", "mirage", "photosynthesis",
        "crystal growth", "fermentation", "metamorphosis", "magnetic north drift",
        "rust", "petrification", "pollination", "hibernation", "camouflage",
        "plate tectonics", "erosion", "carbon dating", "inflammation", "mold",
        "static electricity", "colour blindness", "synesthesia", "deja vu",
        "sleepwalking", "lucid dreaming", "language attrition", "inheritance law",
        "compound interest", "half-life", "superposition", "entropy", "contagion",
        "seed dormancy", "grafting", "lichen symbiosis", "murmuration of starlings",
        "ant colony division of labour", "fungal networks", "scar tissue", "fever",
    ],
    "material": [
        "lacquer", "jade", "obsidian", "indigo dye", "silk", "rubber", "copper wire",
        "terracotta", "paper", "beeswax", "salt", "iron filings", "amber", "ivory-free bone",
        "bamboo", "clay", "mercury", "gold leaf", "ink", "graphite", "felt", "tin",
        "rice straw", "cotton", "cinnabar", "pearl", "charcoal", "sandalwood", "glass",
    ],
    "relationship": [
        "debtor and creditor", "godparent and godchild", "rival apprentices",
        "landlord and tenant", "jailer and prisoner", "translator and client",
        "divorced couple", "twins raised apart", "teacher and failed student",
        "doctor and the patient who sued", "two widows of one man", "in-laws",
        "employer and maid", "co-conspirators", "blood brothers", "sworn sisters",
        "adoptive parent and the birth parent", "pen pals who never met",
        "informant and handler", "rival chess players", "neighbours sharing a wall",
        "estranged grandparent and grandchild", "guard and the person guarded",
    ],
    "ritual": [
        "naming ceremony", "funeral feast", "coming-of-age test", "harvest festival",
        "debt forgiveness day", "census day", "lantern festival", "fasting month",
        "dowry negotiation", "bone-cleaning reburial", "ancestor tablet offering",
        "wedding procession", "pilgrimage", "oath taking", "exam day",
        "first haircut", "tea ceremony", "the day of the dead", "inheritance reading",
        "election", "trial by ordeal", "silent day", "market day", "graduation",
    ],
    "creature_or_plant": [
        "silkworm", "cuttlefish-free octopus", "tardigrade", "slime mould", "cicada",
        "fig wasp", "honey badger", "axolotl", "lotus", "durian", "baobab",
        "mycelium", "pangolin", "naked mole rat", "orchid mantis", "yak",
        "camel", "water buffalo", "carrier pigeon", "crow", "vulture", "termite",
        "bamboo flowering", "rice blast fungus", "coffee plant", "opium poppy",
        "mangrove-free strangler fig", "date palm", "tea bush", "rubber tree",
    ],
}

# How many of each to draw per writer.
DRAW = {
    "culture_era": 2, "terrain": 1, "profession": 2, "object": 3, "phenomenon": 2,
    "material": 1, "relationship": 1, "ritual": 1, "creature_or_plant": 1,
}


def draw(exclude):
    out = {}
    for key, n in DRAW.items():
        pool = [w for w in LISTS[key] if w not in exclude]
        picks = []
        while len(picks) < n and pool:
            w = pool.pop(secrets.randbelow(len(pool)))
            picks.append(w)
            exclude.add(w)
        out[key] = picks
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--writers", nargs="*", default=["writer"])
    ap.add_argument("--exclude", nargs="*", default=[])
    args = ap.parse_args()
    used = set(args.exclude)
    for name in args.writers:
        print(f"## Seeds for {name}")
        for key, words in draw(used).items():
            print(f"- {key}: {'; '.join(words)}")
        print()


if __name__ == "__main__":
    main()
