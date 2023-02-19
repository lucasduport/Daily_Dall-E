import openai
import creds

openai.api_key = creds.getCreds()['open_ai_key']

model = creds.getCreds()['model']


def use_chatGPT(prompt):
        response = openai.Completion.create(
        prompt=prompt,
        model=model,
        temperature=0.9,
        max_tokens=1000,
        n=1)
        return response.choices[0].text

def use_dallE(prompt):
    image = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return image['data'][0]['url']