# Daily Dall-E
This tool allows you to automatically post to Instagram by generating captions and images using machine learning models.

## How it Works

The tool uses the Instagram API to schedule posts at specified times. Every time a post is scheduled, the tool generates a random caption using the Faker library, and sends the caption to ChatGPT, a large language model. ChatGPT then generates a prompt based on the caption, which is passed to DALL-E, an AI model developed by OpenAI that generates an image from textual prompts. Finally, the tool posts the generated image and caption to your Instagram account.

## Installation

To use this tool, you will need to have Python 3.x installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/).

To install the required libraries, run the following command:
`pip install openai`
`pip install fake`

You will also need to create a developer account with Instagram and obtain your `client_id`, `client_secret`, and `access_token`, as well as an API key to use OpenAI tools. For more information, see the [Instagram API documentation](https://developers.facebook.com/docs/instagram). 

## Usage

To use the tool, run the following command:
`python main.py`

This will start the tool and begin posting to your Instagram account.

## Contributing

If you find any issues with the tool or have ideas for improvements, feel free to open an issue or submit a pull request on GitHub.

## License

This tool is licensed under the [MIT License](LICENSE).
