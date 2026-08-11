# CodeAlpha Task 4
# Basic Chatbot


# Function to generate chatbot responses
def chatbot_response(user_input):

    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

# Welcome message
print("================================")
print("        BASIC CHATBOT")
print("================================")
print("Type 'bye' to exit the chatbot.")
print()

# Main chatbot loop
while True:

    # Get input from the user
    user_input = input("You: ").lower()

    # Get chatbot response
    response = chatbot_response(user_input)

    # Display chatbot response
    print("Bot:", response)

    # Exit the chatbot
    if user_input == "bye":
        break

print("\nChatbot ended. Goodbye!")