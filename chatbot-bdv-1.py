
import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']

questions = ['How are you?', 'How are you doing?']

response = ['Okay', 'I`m fine']

#

low_greetings = list()
for word in greetings:
    low_greetings.append(word.lower())

    # using lambda
    # low_greetings = [x.lower() for x in questions]

low_questions = list()
for word in questions:
    low_questions.append(word.lower())

    # using lambda
    # low_questions = [x.lower() for x in questions]



while True:
    userInput = raw_input(">>> ")
    userInput = userInput.lower()

    if userInput in low_greetings:
        random_greeting = random.choice(greetings)
        print random_greeting

    elif userInput in low_questions:
        random_response = random.choice(response)
        print random_response

    else:
        print "I did not understand what you said"