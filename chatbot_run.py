from chatbot_algorirthims import *


def run_chatbot():

    print("Bot: I am here to answer your questions about fortune 500 banks. :)")
    # asked questions
    asked_questions = []
    # date time greetings
    times_of_day = ["morning", "afternoon", "evening"]
    # salutations
    salutations = ["hello", "hi", "hey", "greetings"]
    # thanks
    thanks = ["thanks", "thank", "nice", "cool", "awesome"]

    run = True

    while run:
        user_input = input(str("Talk to bot here --->: "))
        if user_input == "0":
            break

        cleaned_input = clean_text_input(user_input)
        user_words = cleaned_input.split()

        # determines type of greeting or thank you
        type_of_greeting = False
        for word in user_words:
            # times of day greeting
            if word in times_of_day:
                date_time_greetings(user_input)
                type_of_greeting = True
            # salutations
            elif word in salutations:
                greetings(user_input)
                type_of_greeting = True
            # thank you replies
            elif word in thanks:
                thanking(user_input)
                type_of_greeting = True

        # runs user input to determine type of ask/statement if not a greeting/thank you
        # checks if user said anything
        if len(user_input) == 0:
            no_user_input(user_input)
        # checks if user asked about stocks
        elif check_for_stock_ask(user_input) and is_question(user_input) and not check_already_asked(asked_questions, user_input):
            get_stock_price(user_input)
        # user asked question related to topic
        elif is_related_topic(user_input) and is_question(user_input):
            if check_already_asked(asked_questions, user_input):  # checks is user asked question previously
                is_already_asked(user_input)
            else:
                print("Bot: ", end="")
                probabilities_2(user_input)
        # user gave new related info
        elif is_related_topic(user_input) and not type_of_greeting and not is_question(user_input):
            learning(user_input)
            write_to_file(user_input)
        # user gave unrelated new info
        elif not is_related_topic(user_input) and not type_of_greeting and not is_question(user_input):
            check_related(user_input)
        # user asked an unrelated question
        elif not is_related_topic(user_input) and not type_of_greeting and is_question(user_input):
            if check_already_asked(asked_questions, user_input):  # checks is user asked question previously
                is_already_asked(user_input)
            elif how_are_you(user_input):
                how_are_you_replies()
            else:
                unrelated_question()

        # print(is_related_topic(user_input))
    print("Test ended.")


run_chatbot()
# so we take the user input and then pass it through cases
# the cases I want are hello and date time greeting, is question valid, and teach
