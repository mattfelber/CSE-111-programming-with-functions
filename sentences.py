"""
main
make_sentence
get_determiner
get_noun
get_verb

"""
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
    

    print(f"{determiner} {noun} {verb}")


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
    





main()


