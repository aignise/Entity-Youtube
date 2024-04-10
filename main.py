from dotenv import load_dotenv
import os
from entity import create_thread, start, get_response

load_dotenv()

def main():
    while True:
        # Create a thread for conversation
        thread_id = create_thread()

        user_query_prompt = "Please provide a keyword to search for trending videos: "
        user_query = input(user_query_prompt)

        assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
        
        start(thread_id, user_query)

        response = get_response(thread_id, assistant_id, user_query)

        print("Trending Videos:", response)

        while True:
            further_assistance = input("Do you require further assistance? (yes/no): ").lower()
            if further_assistance == "yes":
                assistance_type = input("What type of assistance do you require? (general/youtube): ").lower()
                if assistance_type == "general":
                    next_query = input("Please enter your next query: ")
                    start(thread_id, next_query)
                    response = get_response(thread_id, assistant_id, next_query)
                    print("Response:", response)
                    continue
                elif assistance_type == "youtube":
                    
                    user_query_prompt = "Please provide a keyword to search for trending videos: "
                    user_query = input(user_query_prompt)

                    assistant_id = os.getenv("OPENAI_ASSISTANT_ID")
                    
                    start(thread_id, user_query)

                    response = get_response(thread_id, assistant_id, user_query)

                    print("Trending Videos:", response)
                    continue
                else:
                    print("Invalid input. Please enter 'general' or 'youtube'.")
            elif further_assistance == "no":
                print("Thanks for using our service. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        break

if __name__ == "__main__":
    main()
