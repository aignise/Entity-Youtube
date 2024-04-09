# YouTube Trending Videos Assistant

The YouTube Trending Videos Assistant is a Python script that utilizes the OpenAI API to fetch and display trending videos from YouTube based on user input. It integrates with the YouTube Data API to retrieve trending videos and with the OpenAI Assistants API to provide conversational interaction for users.

# YouTube Data API Integration

This Python script integrates with the YouTube Data API to search for trending videos based on user input.

## Setup

- The `os` module is imported to access environment variables.
- The `googleapiclient.discovery` module is imported to build and execute requests to the YouTube Data API.
- The `dotenv` module is imported to load environment variables from the `.env` file.

## Function: `search_videos`

This function searches for videos on YouTube based on a user-provided query.

### Parameters

- `query` (str): The keyword(s) used for searching videos.

### Returns

A list of video items containing their metadata.

## Function: `fetch_video_statistics`

This function fetches statistics for a specific video identified by its ID.

### Parameters

- `video_id` (str): The unique ID of the video.

### Returns

A tuple containing the view count, like count, and dislike count of the video.

## Function: `fetch_videos`

This function combines the search and statistics retrieval process to fetch videos and their statistics.

### Parameters

- `query` (str): The keyword(s) used for searching videos.

### Returns

A list of videos with their metadata and statistics.

## Main Program

The `main` function:
1. Creates a thread for conversation.
2. Prompts the user to provide a keyword for searching trending videos.
3. Retrieves the OpenAI assistant ID from environment variables.
4. Starts the conversation with the user and retrieves the response containing trending videos.
5. Prints the trending videos with their metadata and statistics.

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

# Setting Up OpenAI Assistant Using OpenAI API

Follow these steps to set up your OpenAI assistant using the OpenAI API:

1. **Sign Up for OpenAI API**:
   - Visit the OpenAI website and sign up for an account if you haven't already.
   - Subscribe to the OpenAI API plan that suits your needs.

2. **Get API Key**:
   - Once subscribed, you'll receive an API key. This key is essential for authenticating your requests.

3. **Install OpenAI Python Library**:
   - Use pip to install the OpenAI Python library:
     ```
     pip install openai
     ```

4. **Import OpenAI Library**:
   - In your Python script or environment, import the OpenAI library:
     ```python
     import openai
     ```

5. **Set API Key**:
   - Set your API key using the `openai.api_key` attribute:
     ```python
     openai.api_key = 'YOUR_API_KEY'
     ```

6. **Invoke OpenAI API**:
   - Use the OpenAI API to interact with the language model. For example:
     ```python
     response = openai.Completion.create(
         engine="text-davinci-003",
         prompt="Once upon a time",
         max_tokens=50
     )
     print(response.choices[0].text.strip())
     ```

7. **Explore API Documentation**:
   - Refer to the official OpenAI API documentation for detailed information on endpoints, parameters, and usage examples.

8. **Understand API Usage and Billing**:
   - Familiarize yourself with usage limits and billing details to avoid exceeding quotas and unexpected charges.

9. **Experiment and Develop**:
   - Start experimenting with the OpenAI models, explore prompts, and develop your applications.

10. **Handle Errors and Exceptions**:
    - Implement error handling mechanisms in your code to gracefully handle any errors during API requests.

By following these steps, you can set up and start using the OpenAI API to interact with powerful language models and build innovative applications leveraging artificial intelligence capabilities.

## Usage

Run the script `main.py` and follow the prompts to interact with the assistant:

The assistant will prompt you to enter a keyword to search for trending videos on YouTube. After entering the keyword, it will fetch and display the trending videos based on your input.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




