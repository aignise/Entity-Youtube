import time
from dotenv import load_dotenv
import openai
import os
from function import fetch_tiktok_data
import json 

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai_api_key)

def setup():
    assistant = client.beta.assistants.create(
        name="TikTok Trends Fetch",
        instructions="You are a bot to fetch TikTok trends based on user preferences.",
        model="gpt-4-turbo-preview",  # Assuming this is suitable for TikTok trends
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "fetch_tiktok_data",
                    "description": "Fetches TikTok trends based on user preferences.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "region": {
                                "type": "string",
                                "description": "Region code (e.g., us)"
                            },
                            "count": {
                                "type": "integer",
                                "description": "Number of trends to fetch"
                            }
                        },
                        "required": ["region", "count"]
                    }
                }
            }
        ]
    )

    return assistant.id

def create_thread():
    thread = client.beta.threads.create()
    return thread.id

def start(thread_id, user_query):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=user_query
    )
    
def get_response(thread_id, assistant_id, user_query):
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
    output = fetch_tiktok_data(region="us", count=10)
    output_str = json.dumps(output)
    
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

