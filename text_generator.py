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
    caption = """ChatGPT using text-davinci-003 generated this short paragraph: """ + chatGPT_response + """

Dall-E then generated an image from this text.

See you in a few hours.
(This post was totally automated.)
---------------------------------------------
""" + hashtags_generator(chatGPT_response)
    return caption

def generate_prompt():
    prompt = "Génère un court texte (4 phrases max) en anglais qui contient un être vivant (ou un mix de plusieurs) ainsi qu'une action et qui commence par 'A realistic photography of'. N'ajoute pas de texte supplémentaire car ta réponse va être copié collée pour Dall-E 2"
    return prompt