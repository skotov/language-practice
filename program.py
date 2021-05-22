import random

# TODO adjectives of state
# TODO more complex posessives
# TODO more vocab

# generate posessives
    # his mom's house
    # the house's door
    # our dog's name

    # simple or complex

    # if simple
        # pos. pronoun or object + object -- my house, his house, their dog
    # if complex
        # pos. pronoun or object's object's object -- his wife's house

pronouns = ["I", "you (masc)", "you (fem)", "he", "she", "we", "you (pl)", "they (masc)", "they (fem)", "they (mixed)"]
posessivepronouns = ["my", "your (masc)", "your (fem)", "his", "her", "our", "your (pl)", "their (masc)", "their (fem)", "their (mixed)"]

family = ["mom", "dad", "sister", "brother", "aunt (f. line)", "aunt (m. line)", "uncle (f. line)", "uncle (m. line)", "grandma", "grandpa", "husband", "wife"]
animals = ["dog", "cat", "bunny"]
verbs = ["to be", "to want", "to travel", "to visit", "to learn", "to do", "to speak", "to teach"]
# adjectives of state = ["cold", "hungry", "upset", "drunk", "full after eating", "thirsty", "happy", "hot", "sleepy"]

subjects = pronouns + posessivepronouns + family
directobjects = subjects

vocabulary = animals + family

wildcards = ["numbers", "ordinal numbers", "idafa", "is *still*...", "...because...", "...in order to...", "past tense"]


def get_subject():
    idx = random.randint(0, len(subjects) - 1)
    return subjects[idx]

def get_object():
    idx = random.randint(0, len(directobjects) - 1)
    return directobjects[idx]

def get_verb():
    idx = random.randint(0, len(verbs) - 1)
    return verbs[idx]

# equal probability of having 0, 1, 2, or 3 vocab terms
def get_vocab():
    selections = []
    rand = random.random()
    while rand > 0.25:
        randidx = random.randint(0, len(vocabulary) - 1)
        selections.append(vocabulary[randidx])
        rand -= 0.25
    return selections


# equal probability of having 0 wildcards, 1 wildcard, or 2 wildcards
def get_wildcard():
    rand = random.random()
    selections = []
    while rand > 0.3333:
        randidx = random.randint(0, len(wildcards) - 1)
        selections.append(wildcards[randidx])
        rand -= 0.3333
    return selections

def print_prompt(subject, grammaticalobject, verb, vocab, wildcards):
    print "\t Write a sentence using..."
    print "\t", subject, "as the subject"
    print "\t", grammaticalobject, "as the direct object"
    print "\t...using", verb, "as the verb"
    if (len(vocab) > 0):
        print "\t...use the following vocabulary:", vocab
    if (len(wildcards) > 0):
        print "\t...use the following grammar constructs:", wildcards

def main():
    # generate the subject
    subject = get_subject()
    grammaticalobject = get_object()
    verb = get_verb()
    additionalvocab = get_vocab()
    wildcards = get_wildcard()

    # print prompt
    print_prompt(subject, grammaticalobject, verb, additionalvocab, wildcards)

if __name__ == "__main__":
    main()