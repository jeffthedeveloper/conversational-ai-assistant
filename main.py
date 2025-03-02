from chatbot import respond_to_user
from chatbot_model import get_gpt_response
from word_counter import count_characters
from text_to_speech import text_to_speech

def main():
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['bye', 'goodbye']:
            print("AI: Goodbye!")
            break
        
        character_count = count_characters(user_input)
        print(f"Character count: {character_count}")
        
        chatbot_response = respond_to_user(user_input)
        
        if chatbot_response:
            print("AI:", chatbot_response)
            text_to_speech(chatbot_response)
        else:
            gpt_response = get_gpt_response(user_input)
            print("AI:", gpt_response)
            text_to_speech(gpt_response)

if __name__ == "__main__":
    main()