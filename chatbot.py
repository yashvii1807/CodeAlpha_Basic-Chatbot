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

