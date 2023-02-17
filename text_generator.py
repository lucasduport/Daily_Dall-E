
from faker import Faker

def words_generator():
    fake = Faker()
    words = ""
    for _ in range(10):
        words += fake.word() + " "
    return words[:-1]

def hashtags_generator(words):
    hashtags = ""
    for word in words.split():
        hashtags += " #" + word
    hashtags +=""" #art #artwork #artistic #dalle #ai #openai #chatgpt #words #inspiration #inspiring #beautiful"""
    return hashtags

def caption_generator(words, chatGPT_response):
    caption = """Hey there!

Look at this beautiful artwork created using these random words: """ + words.replace(" ", ", ")+ """.

From theses words, ChatGPT using text-davinci-003 generated the following sentence: """ + chatGPT_response + """

Dall-E then generated an image that best represents this sentence.

See you in a few hours.
(This post was totally automated.)
---------------------------------------------
""" + hashtags_generator(words)
    return caption

def generate_prompt(words):
    prompt = "Here are 10 random words: " + words + ". Compose a cohesive, well-written, artistic text that could inspire a beautiful work of art using these words. You can also specify the style of the artwork as well as the main colors that this sentence inspires you."
    return prompt

