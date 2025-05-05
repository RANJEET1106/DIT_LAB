responses={
    "hours":"Our business hours are 9 AM to 5 PM, Monday to Friday.",
    "location": "We are located at 1234 Elm Street, Springfield.",
    "products": "We sell electronics, furniture, and home appliances.",
    "support": "For support, please call us at 1-800-123-4567 or email support@company.com.",
    "goodbye": "Thank you for chatting with us! Have a great day!",
    "default": "I'm sorry, I don't understand that. Can you please rephrase your question?"
}

def handel_user_input(user_input):
    if user_input in responses:
        print(responses[user_input])
    else :
        print(responses["default"])

print("Welcome to our customer service chat! How can I assist you today?")
while(True):
    user_input=input("You: ")
    if(user_input.lower()=="goodbye"):
        print(responses["goodbye"])
        break

    handel_user_input(user_input.lower())