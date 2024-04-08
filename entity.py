import time
import openai
import os
import json
from dotenv import load_dotenv
from function import YouTubeAPI

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai_api_key)

def setup():
    assistant = client.beta.assistants.create(
        name="YouTube Trending Videos Assistant",
        instructions="You are a bot to search for trending videos based on user input.",
        model="gpt-4-turbo-preview",
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "fetch_videos",
                    "description": "Fetches trending videos from YouTube API based on user input.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "Keyword to search for trending videos"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }
        ]
    )
    return assistant.id

def create_thread():
    """Creates a thread for conversation."""
    thread = client.beta.threads.create()
    return thread.id

def start(thread_id, user_query):
    """Starts a conversation in the specified thread with the given user query."""
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_query
    )

def get_response(thread_id, assistant_id, user_query):
    """Retrieves the response from the OpenAI API."""
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id,
        instructions="Answer user questions using custom functions available to you."
    )
    
    while True:
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
        if run_status.status == "completed":
            break
        elif run_status.status == 'requires_action':
            submit_tool_outputs(thread_id, run.id, run_status, user_query)
        
        time.sleep(1)
    
    messages = client.beta.threads.messages.list(thread_id=thread_id)
    response = messages.data[0].content[0].text.value
    return response

def submit_tool_outputs(thread_id, run_id, run_status, user_query):
    """Submits tool outputs to the OpenAI API."""
    videos = YouTubeAPI.fetch_videos(query=user_query)
    output_str = ""
    if videos:
        for video in videos:
            title = video['snippet']['title']
            video_id = video['id']['videoId']
            statistics = video['statistics']
            view_count = statistics['viewCount']
            like_count = statistics['likeCount']
            dislike_count = statistics['dislikeCount']
            output_str += f"Title: {title}\n"
            output_str += f"Video ID: {video_id}\n"
            output_str += f"Views: {view_count}\n"
            output_str += f"Likes: {like_count}\n"
            output_str += f"Dislikes: {dislike_count}\n\n"
    else:
        output_str = "No videos found."

    tool_calls = run_status.required_action.submit_tool_outputs.tool_calls
    
    tool_outputs = []
    for tool_call in tool_calls:
        tool_outputs.append({
            "tool_call_id": tool_call.id,
            "output": output_str
        })
    
    client.beta.threads.runs.submit_tool_outputs(
        thread_id=thread_id,
        run_id=run_id,
        tool_outputs=tool_outputs
    )

def main():
    # Create a thread for conversation
    thread_id = create_thread()

    user_query_prompt = "Please provide a keyword to search for trending videos: "
    user_query = input(user_query_prompt)

    assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
    
    start(thread_id, user_query)

    response = get_response(thread_id, assistant_id, user_query)

    print("Trending Videos:", response)


if __name__ == "__main__":
    main()
