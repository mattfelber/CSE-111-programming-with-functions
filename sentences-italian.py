import random
#from googletrans import Translator

def main():
    for _ in range(6):  # Generating sentences for different tenses and quantities
        make_sentence(1, "passato")
        make_sentence(1, "presente")
        make_sentence(1, "futuro")
        make_sentence(2, "passato")
        make_sentence(2, "presente")
        make_sentence(2, "futuro")

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity).capitalize()
    adjective = get_adjective().capitalize()
    noun = get_noun(quantity).capitalize()
    adverb = get_adverb().capitalize()
    verb = get_verb(quantity, tense)
    prepositional = get_prepositional_phrase().capitalize()

    print(f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional}.")

def get_determiner(quantity):
    if quantity == 1:
        words = ["un", "il", "la"]
    else:
        words = ["alcuni", "i", "le"]
    
    return random.choice(words)

def get_noun(quantity):
    if quantity == 1:
        words = ["gatto", "cane", "ragazzo", "ragazza", "libro", "casa", "fiore", "tempo", "amore", "giorno"]
    else:
        words = ["gatti", "cani", "ragazzi", "ragazze", "libri", "case", "fiori", "tempi", "amori", "giorni"]
    
    return random.choice(words)

def get_verb(quantity, tense):
    if tense == "passato":
        words = ["bevuto", "mangiato", "corso", "parlato", "vissuto", "pensato", "scritto", "ballato", "cantato", "lavorato"]
    elif tense == "presente" and quantity == 1:
        words = ["beve", "mangia", "corre", "parla", "vive", "pensa", "scrive", "balla", "canta", "lavora"]
    elif tense == "presente" and quantity != 1:
        words = ["bevono", "mangiano", "corrono", "parlano", "vivono", "pensano", "scrivono", "ballano", "cantano", "lavorano"]
    else: #futuro
        words = ["berrà", "mangerà", "correrà", "parlerà", "vivrà", "penserà", "scriverà", "ballerà", "canterà", "lavorerà"]
    
    return random.choice(words)

def get_prepositional_phrase():
    quantity = random.randint(1, 2)

    preposition = get_preposition().capitalize()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f"{preposition} {determiner} {noun}"

def get_preposition():
    words = ["su", "sotto", "vicino a", "dietro", "dentro", "fuori da", "presso", "tra", "con", "senza"]
    return random.choice(words)

def get_adjective():
    adjectives = ["curioso", "innocente", "brillante", "vibrante", "strano", "generoso", "antico", "giggly", "particolare", "sospetto",
                  "bizzarro", "colorato", "pigro"]
    return random.choice(adjectives)

def get_adverb():
    adverbs = ["velocemente", "quietamente", "improvvisamente", "cuidadosamente", "sempre", "mai", "felice", "tristemente", "eccitato", "calmamente"]
    return random.choice(adverbs)

main()
