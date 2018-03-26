from difflib import SequenceMatcher
import datetime
import markov
import os
from nltk.tokenize import word_tokenize

morning_message = 'Full many a glorious morning have I seen, \n ' \
                  'but never this happy have I been,  \n' \
                  'Seeing sunrises are my greatest pleasure, \n' \
                  'my feelings of joy are beyond measure'

afternoon_message = 'The day is in its finest hour, \n ' \
                  'Afternoons always give me power'


night_message = 'Even in the darkest night \n' \
                'shinest one stars with its light \n' \
                'Soon I shall be blessed with pleasant dreams \n' \
                'But first I will chat with you, or so it seems'

greeting_keystrings = ['hello', 'hey', 'hi', 'hallo', 'hoi', 'greetings', 'good day', 'morning', 'afternoon', 'evening']
howreyou_keystrings = ['how are you', 'it going', 'what\'s up', 'sup']
help_keystrings = ['help', '']
poem_keystrings = ['poem', 'shakespeare', 'write']
love_keystrings = ['love', 'heart']
nature_keystrings = ['nature', 'tree', 'flower']
mythology_keystrings = ['mythology']


all_keystrings = [greeting_keystrings, howreyou_keystrings, help_keystrings, poem_keystrings, love_keystrings, nature_keystrings, mythology_keystrings]


def calc_part_of_day():
    now = datetime.datetime.now()
    hour = now.hour

    if (hour>5 and hour<12):
        return "morning"
    elif (hour>=12 and hour<18):
        return "afternoon"
    else:
        return "night"

def response_howre_you(part_of_day):
    if (part_of_day == "morning"):
        return morning_message
    elif (part_of_day == "afternoon"):
        return afternoon_message
    else:
        return night_message

def generate_poem(subject):
    m = markov.Markov(order=1)
    root = "./shakespeare/"
    path = os.path.join(root, subject)
    m.walk_directory(path)
    poem = m.generate_output(max_words=100)
    return poem

#
def bring_to_poem_style(poem):
    end_of_line_characters = [',', '.', '!', '?', ':', ';']
    words = word_tokenize(poem)
    poem_right_style = words[0] + ' '

    for i in range(1, len(words) - 1):
        if words[i] not in end_of_line_characters:
            poem_right_style += words[i].lower() + ' '
        else:
            i+=1
            poem_right_style += '\n' + words[i].capitalize() + ' '

    return poem_right_style


def determine_text_type(message, keystrings):
    similarities = []

    for keystring in keystrings:
        s = SequenceMatcher(None, message, keystring)
        print(keystring + " similarity: " + str(s.ratio()))
        similarities.append(s.ratio())

    return max(similarities)

