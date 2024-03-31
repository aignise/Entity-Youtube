# YouTube Trending Videos Assistant

The YouTube Trending Videos Assistant is a Python script that utilizes the OpenAI API to fetch and display trending videos from YouTube based on user input. It integrates with the YouTube Data API to retrieve trending videos and with the OpenAI Assistants API to provide conversational interaction for users.

## Role of the Assistant

The role of the assistant is to provide users with trending videos on YouTube based on their keyword input. It interacts with the user in a conversational manner, prompting them to enter a keyword to search for trending videos. It then fetches the relevant videos using the YouTube Data API and presents the results to the user in a structured format.

## Prerequisites

Before using the YouTube Trending Videos Assistant, ensure you have the following installed:

- Python 3.x
- OpenAI Python client (`openai`): You can install it via pip (`pip install openai`)
- `dotenv` library: You can install it via pip (`pip install python-dotenv`)
- `google-api-python-client` library: You can install it via pip (`pip install google-api-python-client`)
- Access to the YouTube Data API and an API key
- Access to the OpenAI API and an API key
- Get the API KEY by reading this https://medium.com/geekculture/extracting-daily-youtube-trending-video-statistics-5de5f9fdc1b7 
## Setup

1. Clone this repository to your local machine.
2. Install the required Python libraries listed in the prerequisites.
3. Set up environment variables by creating a `.env` file in the project directory and adding the following:
Replace `your_openai_api_key` and `your_youtube_api_key` with your actual API keys.

4. Run the `setup()` function in the script to create the assistant in the OpenAI Assistants dashboard. This step is necessary for setting up the assistant in the dashboard.

5. You're ready to use the YouTube Trending Videos Assistant!

## Usage

Run the script `main.py` and follow the prompts to interact with the assistant:

The assistant will prompt you to enter a keyword to search for trending videos on YouTube. After entering the keyword, it will fetch and display the trending videos based on your input.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




