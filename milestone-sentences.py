### EXTRA MILE: Adding {adjective} and {adverb} to the phrase structure, creating two new functions
### Before: {determiner} {noun} {verb} {prepositional}
### After:  {determiner} {adjective} {noun} {adverb} {verb} {prepositional}

import random

past = 'past'
present = 'present'
future = 'future'


def main():
    make_sentence(1, past)
    make_sentence(1, present)
    make_sentence(1, future)
    make_sentence(2, past)
    make_sentence(2, present)
    make_sentence(2, future)


def make_sentence(quantity, tense):
    determiner = get_determiner(quantity).title()
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional = get_prepositional_phrase()
    adjective = get_adjective()
    adverb = get_adverb()
    
    print(f"{determiner} {adjective} {noun} {adverb} {verb} {prepositional}.") ###Extra Mile: Added {adjective} and {adverb} to the phrase structure


def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    
    return random.choice(words)


def get_noun(quantity):

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    
    return random.choice(words)


def get_verb(quantity, tense):

    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == 'present' and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    else: #future
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    return random.choice(words)
    

def get_preposition():
    words = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]

    word = random.choice(words)

    return word


def get_prepositional_phrase():
    quantity = random.randint(1,2)

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return preposition + " " + determiner + " " + noun 


def get_adjective():
    adjectives= ['Curious', 'Innocent', 'Bright', 'Vibrant', 'Stinky', 'Generous', 'Addicted', 'Ancient', 'Giggly', 'Peculiar', 
                 'Bizarre', 'Suspicious', 'Jovial', 'Colorful', 'Lazy']

    adjective = random.choice(adjectives).lower()

    return adjective


def get_adverb():
    adverbs = ["quickly", "quietly", "suddenly", "carefully", "always", 
                         "never", "happily", "sadly", "excitedly", "calmly", "surprisingly", 
                         "honestly", "unexpectedly", "silently", "anxiously", "clearly", 
                         "easily", "frequently", "joyfully", "nervously"]
    
    adverb = random.choice(adverbs).lower()

    return adverb


main()


