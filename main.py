import openai_api
import text_generator
import instagram_api

def main():
    words = text_generator.words_generator()
    prompt = text_generator.generate_prompt(words)
    print(prompt)
    chatGPT_response = openai_api.use_chatGPT(prompt)
    print(chatGPT_response)

    image_url = openai_api.use_dallE(chatGPT_response)
    caption = text_generator.caption_generator(words, chatGPT_response)

    instagram_api.postImage(image_url, caption)

if __name__ == "__main__":
    main()
