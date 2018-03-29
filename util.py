from difflib import SequenceMatcher
import datetime
import markov
import os
from nltk.tokenize import word_tokenize

help_message = 'Ah, I see. Thee needeth my holp! Thither art a number of things I can do: \n\n' \
               'Thy can have some casual small talk with me, by giving me your greetings and asking how I ' \
               'art doing. If thy want to heareth a poem, thee can simply command me to do so and I shall try ' \
               'to write thee a poem about either love, nature or mythology. \n\n' \
               'I can also send thee memes if thou sendest me a sticker or if thy askest for memes. I desire thee ' \
               'findeth them amusing. \n\n' \
               'If thou want to end the conversation, thou can sayest "farwell" or "goodbye" and I will send thee a ' \
               'final farewell-sonnet. \n\n' \
               'Please forgiveth me if I do not understandeth everything'

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

farwell_message = 'Farewell, thou art too dear for my possessing \n' \
                  'And like enough thou know’st thy estimate \n ' \
                  'The charter of thy worth gives thee releasing; \n' \
                  'My bonds in thee are all determinate. \n' \
                  'For how do I hold thee but by thy granting, \n' \
                  'And for that riches where is my deserving? \n' \
                  'The cause of this fair gift in me is wanting, \n' \
                  'And so my patent back again is swerving. \n' \
                  'Thyself thou gav’st, thy own worth then not knowing, \n' \
                  'Or me, to whom thou gav’st it, else mistaking; \n' \
                  'So thy great gift, upon misprision growing, \n' \
                  'Comes home again, on better judgment making. \n' \
                  'Thus have I had thee as a dream doth flatter: \n' \
                  'In sleep a king, but waking no such matter.'

greeting_keystrings = ['hello', 'hey', 'hi', 'hallo', 'hoi', 'greetings', 'day', 'morning', 'afternoon', 'evening']
howreyou_keystrings = ['how', 'how are you doing', 'how is it going', 'what', 'up', 'sup']
help_keystrings = ['help']
poem_keystrings = ['poem', 'writer', 'write', 'sonnet', 'song']
love_keystrings = ['love', 'heart']
nature_keystrings = ['nature', 'tree', 'flower']
mythology_keystrings = ['mythology']
meme_keystrings = ['picture', 'image', 'meme', 'funny']
goodbye_keystrings = ['farewell', 'goodbye', 'later','bye', 'doei']


all_keystrings = [greeting_keystrings, howreyou_keystrings, help_keystrings, poem_keystrings, love_keystrings, nature_keystrings, mythology_keystrings, meme_keystrings, goodbye_keystrings]


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
    end_of_line_character = False
    words = word_tokenize(poem)
    poem_right_style = words[0] + ' '

    for i in range(1, len(words) - 1):
        if not end_of_line_character:
            poem_right_style += words[i].lower() + ' '
            if (words[i] in end_of_line_characters):
                end_of_line_character = True
        else:
            poem_right_style += '\n' + words[i].capitalize() + ' '
            end_of_line_character = False
    return poem_right_style


def determine_text_type(message, keystrings):
    similarities = []
    for keystring in keystrings:
        print(keystring)
        s = SequenceMatcher(None, message, keystring)
        similarities.append(s.ratio())
    return max(similarities)

