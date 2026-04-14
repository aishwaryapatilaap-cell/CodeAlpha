def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you?"
    
    elif user_input in ["how are you", "how are you?"]:
        return "I am fine. Thank you!"
    
    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple Python chatbot."
    
    elif user_input in ["help", "what can you do"]:
        return "I can respond to basic greetings and questions."
    
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print("Simple Chatbot (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break


# Run chatbot
run_chatbot()
