import openai

API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
openai.api_key = API_KEY
model = "text-davinci-003"

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
