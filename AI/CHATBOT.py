import re

def cb():
    print("Hello! I'm your friendly cb. Type 'quit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ").lower()
        
        # Exit condition
        if user_input == "quit":
            print("Cb: Goodbye! Have a great day!")
            break
        elif re.match(r'hi|hello|hey', user_input):
            print("Cb: Hello! How are you?")
        
        elif re.match(r'how are you', user_input):
            print("Cb: I'm fine! How about you?")
        
        elif re.match(r'what is your name', user_input):
            print("Cb: I'm cb")
        
        elif re.match(r'help', user_input):
            print("Cb: Sure! You can ask me things like 'hello', 'how are you', or 'what is your name'.")
        
        elif re.match(r'(.*)', user_input):
            print("Cb: I'm sorry, I didn't quite understand that. Can you rephrase?")
cb()
