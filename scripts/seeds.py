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
  - Every seed must visibly shape the story. The galactic setting, intrigue,
    economic-system and technology seeds set the scale and the plot engine (the brief
    requires big futuristic sci-fi with spy/court intrigue, politics and economics).
    Culture/era is a naming and texture source for a future culture, not a
    historical setting; the profession seeds become main characters'
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
    "galactic_setting": [
        "a Dyson swarm half-built around a red dwarf", "a capital world that is one continuous city",
        "a neutral banking station at a wormhole junction", "a generation fleet that arrived to find colonists already there",
        "a tidally locked world whose day side is owned and night side rented", "a ringworld fragment used as a prison",
        "an embassy moon shared by five species", "a quarantined star system no ship may leave",
        "a shipyard orbiting a gas giant", "a court that moves between three systems each year",
        "a frontier mining belt in a gold-rush", "a dead alien homeworld turned into a museum and a tax haven",
        "an orbital elevator city whose floors are social classes", "a library planet where the archive is the government",
        "a war-front system under a fifty-year ceasefire", "a pleasure world run by an AGI landlord",
        "a terraforming project three centuries behind schedule", "a black-hole observatory with time-dilated staff",
        "a nomad fleet that is also a stock exchange", "a refugee world built inside a hollow asteroid",
        "a ring of habitats that vote as one", "a homeworld abandoned by its rich",
    ],
    "intrigue": [
        "a succession crisis with three claimants", "a double agent who no longer knows which side is real",
        "a regent ruling for a child heir", "an assassination disguised as an accident",
        "a spymaster who is also the court historian", "a defector who brings the wrong secret",
        "a forged treaty", "a hostage prince raised by the enemy", "a mole in the intelligence service",
        "a coup planned for coronation day", "a blackmail archive everyone pretends does not exist",
        "a show trial", "an ambassador with diplomatic immunity and a body in the embassy",
        "a sleeper cell activated by a phrase", "an election rigged by both sides",
        "a marriage alliance between enemy houses", "an honest bureaucrat who controls the seals",
        "a censor who rewrites the news", "a war-crimes tribunal", "a royal bastard with a valid claim",
    ],
    "economic_system": [
        "a currency backed by stored computation", "debt that is inherited across clones",
        "a monopoly on faster-than-light shipping lanes", "a futures market in predicted events",
        "a guild that owns all water", "taxation paid in years of life", "a reputation score as money",
        "sanctions that starve a world", "a speculative bubble in terraformed land",
        "an insurance cartel that profits from wars", "a universal basic income paid by an AGI",
        "a black market in memories", "a company town at planetary scale", "a tariff war between species",
        "a sovereign default that topples a dynasty", "a labour market of rented bodies",
        "a central bank run by an AI that cannot be audited", "trade in time-shifted information",
        "a commodity that only one alien species can produce", "a debt jubilee everyone fears",
    ],
    "technology": [
        "mind uploading with lossy copies", "tachyon messaging with a cost", "neural lace that can be subpoenaed",
        "clone vats with a licensing system", "an AGI bound by a constitution", "wormhole gates that degrade",
        "memory editing used by courts", "orbital weapons under treaty limits", "nanotech assemblers banned by law",
        "body swapping between frames", "predictive policing that is right too often",
        "suspended animation used to dodge debts", "a translation AI between species that edits as it goes",
        "time-dilation used as banking", "synthetic biology that writes into living people",
        "an AGI that is legally a citizen", "surveillance dust", "a causality detector", "a quantum vote",
    ],
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
    "galactic_setting": 1, "intrigue": 2, "economic_system": 1, "technology": 2,
    "culture_era": 1, "profession": 1, "object": 2, "phenomenon": 1,
    "relationship": 1, "ritual": 1,
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
