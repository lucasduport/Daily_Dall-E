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
    nb_hashtags = 19
    for word in words.split():
        if (nb_hashtags == 29):
            break
        if len(word) < 4:
            continue
        hashtags += " #" + word
        nb_hashtags += 1
    hashtags +=""" #art #artwork #artistic #dalle #ai #openai #chatgpt #nftart #nft #aiartist #beautiful #api #code #dev #iart #aiart #masterpiece #photography"""
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
    prompt = creds.getCreds()['magic_prompt']
    return prompt