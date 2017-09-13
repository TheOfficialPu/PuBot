""" Chatbox by me
"""
import re
import random
from textblob import TextBlob


GREETINGS_KEYS = ('hello', 'hi', 'greetings', 'sup', "whats up")
GREETINGS_RESPONSE = ["hey!", "hi!", "whoa,  humans!"]
SELF_VERBS_WITH_NOUN_CAPS_PLURAL = [
    "I am one with the {noun}",
    "The {noun} are the worst!",
    "I am the ruler of all {noun}"
]

SELF_VERBS_WITH_NOUN_LOWER = [
    'Why don'+ "'t" + ' you just google "{noun}"?',
    "Don't ask me about {noun}!",
    "I would rather die than talk about {noun}"
]

SELF_VERBS_WITH_ADJECTIVE = [
    "I hate the {adjective}'s",
    "Why do u ask me about the {adjective}?",
    "Ah! The pursuit of {adjective}ness"
]

NONE_RESPONSES = [
    "*seen*",
    "sad life",
    "I wasn't designed to understand that sentence. Please send an email to Apurv Prashanth about this with the question u asked me. Thanks",
    "Next question :P",
]

COMMENTS_ABOUT_SELF = [
    "Ik, I am the best",
    "Well, I was designed by TheOfficialPu..",
    "On a scale from 1 to 10, I am the scale."
]

FILTER_WORDS = set([
    "skank",
    "wetback",
    "bitch",
    "cunt",
    "dick",
    "douchebag",
    "dyke",
    "fag",
    "nigger",
    "tranny",
    "trannies",
    "paki",
    "pussy",
    "retard",
    "slut",
    "titt",
    "tits",
    "wop",
    "whore",
    "chink",
    "fatass",
    "shemale",
    "nigga",
    "daygo",
    "dego",
    "dago",
    "gook",
    "kike",
    "kraut",
    "spic",
    "twat",
    "lesbo",
    "homo",
    "fatso",
    "lardass",
    "jap",
    "biatch",
    "tard",
    "gimp",
    "gyp",
    "chinaman",
    "chinamen",
    "golliwog",
    "crip",
    "raghead",
    "negro",
    "hooker"])

class UnacceptableUtteranceException(Exception):
    """Raise this (uncaught) exception if the response was going to trigger our blacklist"""
    pass

def is_greetings(sentence):
    """ Check for a greeting and return the appropriate response
    """
    sentence = re.sub(r'[^\w\s]', '', sentence)
    words = sentence.split(' ')
    for word in words:
        if word.lower() in GREETINGS_KEYS:
            return random.choice(GREETINGS_RESPONSE)

def punctuate(sentence):
    """ Adds the necessary punctuations
    """
    text = []
    words = sentence.split(' ')
    for word in words:
        if word == 'i':
            word = 'I'
        if word == "im":
            word = "I'm"
        if word == "i'm":
            word = "I'm"
        text.append(word)
    return ' '.join(text)

def find_pronoun(sentence):
    """ return the pronoun"""
    pronoun = None

    for word, part_of_speech in sentence.pos_tags:
        # Disambiguate pronouns
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            pronoun = 'You'
    return pronoun

def find_verb(sentence):
    """ return the verb"""
    verb = None
    pos = None
    for word, part_of_speech in sentence.pos_tags:
        if part_of_speech.startswith('VB'):
            verb = word
            pos = part_of_speech
            break
    return verb, pos

def find_noun(sentence):
    """ return the noun"""
    noun = None

    if not noun:
        for word, part_of_speech in sentence.pos_tags:
            if part_of_speech == 'NN':
                noun = word
                break
    return noun

def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adj = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech == 'JJ':
            adj = word
            break
    return adj

def find_parts(text):
    """ Returns a pronoun, noun, adjective and verb in a sentence if any
    """
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for sentence in text.sentences:
        pronoun = find_pronoun(sentence)
        noun = find_noun(sentence)
        verb = find_verb(sentence)
        adjective = find_adjective(sentence)
    return pronoun, noun, adjective, verb

def talking_about_bot(noun, pronoun, adjective):
    """Check if the user's input was about the bot """
    response = None
    if pronoun == 'I' and (noun or adjective):
        if noun:
            if random.choice((True, False)):
                response = random.choice(SELF_VERBS_WITH_NOUN_CAPS_PLURAL).format(**{
                    'noun': noun.pluralize().capitalize()})
            else:
                response = random.choice(SELF_VERBS_WITH_NOUN_LOWER).format(**{'noun': noun})
        else:
            response = random.choice(SELF_VERBS_WITH_ADJECTIVE).format(**{'adjective': adjective})
    return response

def check_greetings(text):
    " checks if the text is a greeting"
    for word in text.words:
        if word.lower() in GREETINGS_KEYS:
            return random.choice(GREETINGS_RESPONSE)

def starts_with_vowel(word):
    """Check for pronoun compability -- 'a' vs. 'an'"""
    return True if word[0] in 'aeiou' else False

def construct_response(pronoun, noun, verb):
    """ well, i give up, lets try something"""
    response = []
    if pronoun:
        response.append(pronoun)
    if verb:
        verb_word = verb[0]
        if verb_word in ('be', 'am', 'is', "'m"):
            if pronoun.lower() == 'you':
                response.append("aren't really")
            else:
                response.append(verb_word)
    if noun:
        pronoun = "an" if starts_with_vowel(noun) else "a"
        response.append(pronoun + " " + noun)

    response.append(random.choice(("tho", "bro", "lol", "bruh", "smh", "")))
    return " ".join(response)

def filter_response(sentence):
    """ filters the response
    """
    words = sentence.split(' ')
    for word in words:
        if '@' in word or '#' in word or '!' in word:
            raise UnacceptableUtteranceException()
        for swears in FILTER_WORDS:
            if word.lower().startswith(swears):
                raise UnacceptableUtteranceException()

def respond(sentence):
    """ Reply with the best response for the sentence
    """
    text = punctuate(sentence)
    text = TextBlob(text)
    pronoun, noun, adjective, verb = find_parts(text)
    response = talking_about_bot(noun, pronoun, adjective)
    if not response:
        response = check_greetings(text)
    if not response:
        if not pronoun:
            response = random.choice(NONE_RESPONSES)
        elif pronoun == 'I' and not verb:
            response = random.choice(COMMENTS_ABOUT_SELF)
        else:
            response = construct_response(pronoun, noun, verb)
    if not response:
        resp = random.choice(NONE_RESPONSES)

    filter_response(resp)

    return resp
