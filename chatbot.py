import random
from datetime import datetime


# Function to generate chatbot responses
def chatbot_response(user_input, user_name):

    # Greeting
    if user_input in ["hello", "hi", "hey"]:
        return random.choice([
            "Hi! Nice to meet you!",
            "Hello! How can I help you?",
            "Hey! What can I do for you?"
        ])

    # How are you
    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    # User feeling good
    elif user_input in ["i am fine", "i am good", "good", "fine"]:
        return "That's great to hear! 😊"

    # User feeling bad
    elif user_input in ["sad", "i am sad", "not good", "bad"]:
        return "I'm sorry to hear that. I hope your day gets better! ❤️"

    # Bot name
    elif user_input in ["what is your name", "your name"]:
        return "My name is PyBot. I am a simple Python chatbot."

    # User name
    elif user_input == "my name":
        if user_name:
            return f"Nice to meet you, {user_name}!"
        else:
            return "I don't know your name yet."

    # Thank you
    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! 😊"

    # Joke
    elif user_input in ["tell me a joke", "joke"]:
        return random.choice([
            "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
            "Why did the Python programmer wear glasses? Because he couldn't C! 😄",
            "There are 10 kinds of people: those who understand binary and those who don't! 😂"
        ])

    # Current date
    elif user_input == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}."

    # Current time
    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"The current time is {current_time}."

    # Weather
    elif user_input == "weather":
        return "I cannot check live weather, but you can check your local weather app."

    # Study
    elif user_input in ["study", "how to study"]:
        return "Make a study plan, practice regularly, and take short breaks."

    # Python
    elif user_input in ["python", "what is python"]:
        return "Python is a popular high-level programming language known for its simple syntax."

    # Internship
    elif user_input == "internship":
        return "Internships are a great way to gain practical experience and improve your skills."

    # Help
    elif user_input in ["help", "commands"]:
        return """You can try:
- hello
- how are you
- what is your name
- my name
- joke
- date
- time
- weather
- python
- study
- internship
- thank you
- bye"""

    # Goodbye
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    # Unknown input
    else:
        return "Sorry, I don't understand that. Type 'help' to see available commands."


# ========================================
# Main Program
# ========================================

print("========================================")
print("       🤖 WELCOME TO PYBOT")
print("========================================")

print("I am a simple rule-based Python chatbot.")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.")
print()


# Ask user's name
user_name = input("Bot: What is your name? ").strip()

print(f"Bot: Nice to meet you, {user_name}! 😊")
print()


# Main chatbot loop
while True:

    # Get user input
    user_input = input(f"{user_name}: ").lower().strip()

    # Get chatbot response
    response = chatbot_response(user_input, user_name)

    # Display response
    print("Bot:", response)

    # Stop chatbot
    if user_input in ["bye", "exit", "quit"]:
        break


print("\n========================================")
print("       🤖 CHATBOT ENDED")
print("========================================")
print(f"Goodbye {user_name}! Thanks for chatting with PyBot.")