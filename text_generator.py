import creds
"""
from faker import Faker
def words_generator():
    fake = Faker()
    words = ""
    for _ in range(5):
        words += fake.word() + " "
    return words[:-1]
"""
def hashtags_generator(words):
    hashtags = ""
    nb_hashtags = 20
    for word in words.split():
        if (nb_hashtags == 29):
            break
        if len(word) < 3:
            continue
        hashtags += " #" + word
        nb_hashtags += 1
    hashtags +=""" #art #artwork #artistic #dalle #ai #openai #chatgpt #words #inspiration #inspiring #beautiful #api #code #dev #iart #aiart #dalleart #artificial #intelligence"""
    return hashtags[1:]

def caption_generator(chatGPT_response):
    caption = """ChatGPT using """ + creds.getCreds()['model'] + """ generated this short paragraph: """ + chatGPT_response + """

Dall-E then generated an image from this text.

See you in a few hours.
(This post was totally automated.)
---------------------------------------------
""" + hashtags_generator(chatGPT_response)
    return caption

def generate_prompt():
    prompt = """Créé un prompt d'environ 40 mots en anglais pour que Dall-E génère une photographie très originale et super réaliste. Ta réponse va être copiée collée en entrée pour Dall-E 2. Ta réponse doit commencer par "A realistic photography of"."""
    return prompt