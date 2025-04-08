import numpy
import random
import typo
import pandas as pds
import yfinance as yf
from datetime import datetime
from difflib import SequenceMatcher

# from bs4 import BeautifulSoup

# sample data set
file_path = "/Users/kindnessativie/Downloads/3000 sample words_3.txt"
data_file = open(file_path, "r")
data = data_file.read()

# user entry
# user_input = str(input("Talk to bot here --->: "))


# remove stop words and get keywords from data_set, remove special characters, remove special characters except period
stop_words = ["a", "an", "and", "as", "at", "be", "but", "by", "for", "if", "in", "into", "it", "no",
              "not", "of", "on", "or", "such", "that", "the", "their", "then", "these", "they", "this", "to",
              "will", "with", "you", "they", "them", "this", "there", "your", "has", "in", "for", "we", "he", "she",
              "been", "us", "need", "being", "have", "say", "said", "saying", "welcome", "please", "about", "okay"]

special_characters = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}",
                      "[", "]", "|", "/", "?", ",", ".", ":"]

special_characters_period = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}",
                             "[", "]", "|", "/", "?", ",", ":"]


# function that cleans and lowers data, text, etc.
def clean_text_input(my_text: str):
    lowered_text = my_text.lower()

    words_in_lowered_text = lowered_text.split()

    pure_my_text = [word for word in words_in_lowered_text if word not in stop_words]
    result_pure_text = ' '.join(pure_my_text)

    final_form = ''.join(letter for letter in result_pure_text if letter not in special_characters)

    return final_form


# function that prints the set of unique words for a string (ex. user input)
def remove_duplicate_unique_words(clean_text: str):
    li = list(clean_text.split(" "))
    no_duplicates = set(li)

    return no_duplicates


# returns the total number of unique words (no duplicates)
def get_unique_words(my_data: str):
    li = list(my_data.split(" "))
    total_unique_words = len(set(li))

    return total_unique_words


# related to topic
def is_related_topic(user_question):
    a = clean_text_input(user_question)
    b = clean_text_input(data)

    user_vocab = remove_duplicate_unique_words(a)
    data_vocab = list(b.split(" "))
    no_duplicates_data_vocab = get_unique_words(b)

    frequencies_user_input = []
    for word in user_vocab:
        frequencies_user_input.append(data_vocab.count(word))

    sum_user_frequencies = numpy.sum(frequencies_user_input)

    related_chance = (sum_user_frequencies / no_duplicates_data_vocab)

    if related_chance >= 0.04:  # you may have to edit this metric as the fie increases size (original was 0.06)
        return True
    else:
        return False


# greetings
salutations = ["hello", "hi", "hey", "greetings"]


def greetings(user_question):
    greeting_replies = ["Hi!", "What's up?", "Hey there!", "Hello there!", "Greetings, human!",
                        "Hello. It's a lovely day to learn about banks, isn't it?", "Hi, human.",
                        "Hello there, earthling.",
                        "Hello!", "Hi. It's nice to talk to a human.", "Hello. I've been summoned.",
                        "Hello. I am here."]

    a = clean_text_input(user_question)
    li = list(a.split(" "))

    for word in li:
        if word in salutations:
            reply = random.choice(greeting_replies)
            print("Bot:", reply)


# thanks
thanks = ["thanks", "thank", "nice", "cool", "awesome"]


def thanking(user_question):
    thanks_replies = ["It's the least I could do in this cold world of 1s and 0s.", "You're welcome!",
                      "Thank you for giving me something to do.", "I am genius, aren't I?", "Of course!",
                      "Happy to help.",
                      "Don't leave me. I get lonely. Ask again please.", "Always!",
                      "You don't have to compliment me. I don't have feelings.",
                      "Only Canadians would thank a lifeless, binary illusion."]

    a = clean_text_input(user_question)
    li = list(a.split(" "))

    for word in li:
        if word in thanks:
            reply = random.choice(thanks_replies)
            print("Bot:", reply)


# date time greetings
times_of_day = ["morning", "afternoon", "evening"]


def date_time_greetings(user_question):
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    int_current_hour = int(current_hour)

    if int_current_hour < 12:
        time_of_day_tag = "AM"
    else:
        time_of_day_tag = "PM"
        pm_current_time = int_current_hour % 12
        if pm_current_time > 0:
            current_time = str(pm_current_time) + ":" + current_minute

    if int_current_hour == 0:
        current_time = str(12) + ":" + current_minute

    reply = ""
    a = clean_text_input(user_question)
    li = list(a.split(" "))

    for word in li:
        if word in times_of_day:
            if word == "morning" and int_current_hour < 5:
                early_bird_selection = ["Good morning to you too. Good really early morning actually.",
                                        "Isn't it a little bit too early?",
                                        f"Why are you talking to robot at {current_time}{time_of_day_tag}?",
                                        "Wow. I'm still tired. *Yawns in binary*",
                                        f"Go to sleep it's {current_time}{time_of_day_tag}!"]
                reply = random.choice(early_bird_selection)

            elif word == "morning" and (5 <= int_current_hour < 12):
                morning_selection = ["Good morning!", "Good morning to you too.", "Good morning, human.",
                                     "It's a fresh day for a fresh question. :)",
                                     "Early bird gets the worm as the humans say, right?",
                                     "Early program gets the 1001 as the bots say.",
                                     "Morning, earthling.",
                                     f"Ah. {current_time}{time_of_day_tag} is the perfect time to summon me."]
                reply = random.choice(morning_selection)

            elif word == "afternoon" and (12 <= int_current_hour < 17):
                afternoon_selection = ["Good afternoon!", "Good afternoon to you to.",
                                       "Answering humans in the afternoon makes my binary bones happy.",
                                       f"You know, {current_time}{time_of_day_tag} is the best time in the afternoon.",
                                       "Good afternoon, earth dweller. Have you had lunch?"]
                reply = random.choice(afternoon_selection)

            elif word == "evening" and (17 <= int_current_hour < 22):
                evening_selection = ["Good evening!", "Sometimes I wish I could experience evenings like you humans.",
                                     "Evening. Have you had dinner? I prefer not to eat run time errors. Makes me sick."
                                     "Ah. The night time. Hope you had a good day.",
                                     f"Evening! I am programmed to say {current_time}{time_of_day_tag} is cool. :?"]
                reply = random.choice(evening_selection)

            elif word == "evening" and (int_current_hour >= 22):
                night_owl_selection = ["*Yawns in 0s and 1s* Evening, human. It's getting late.",
                                       f"Asking a bot questions at {current_time}{time_of_day_tag}? Okay then... :/ ",
                                       "I'd tell you to go to bed but I function at all hours. :/",
                                       f"You know late night chats with a bot are an indicator of loneliness.",
                                       f"Good evening! {current_time}{time_of_day_tag} is a bit late though.",
                                       "Evening. I can't wait to rest on my bed of 0s and 1s.",
                                       f"Hey, {current_time}{time_of_day_tag} is late but I compile at all hours."]
                reply = random.choice(night_owl_selection)

            elif word == "morning" and not int_current_hour < 12:
                correct_morning_selection = [f"It's {current_time}{time_of_day_tag}, so I wouldn't call that morning.",
                                             f"Hey there! It's actually {current_time}{time_of_day_tag}.",
                                             f"My bot clock tells me it's actually {current_time}{time_of_day_tag}. :?"]
                reply = random.choice(correct_morning_selection)

            elif word == "afternoon" and not (12 <= int_current_hour < 17):
                correct_afternoon_selection = [f"Afternoon might be a stretch for {current_time}{time_of_day_tag}.",
                                               "Hi! It's not afternoon though.",
                                               f"Missed the update where {current_time}{time_of_day_tag} is afternoon.",
                                               "Hey! It's not the afternoon though. :/"]
                reply = random.choice(correct_afternoon_selection)

            elif word == "evening" and not (int_current_hour >= 17):
                correct_evening_selection = [f"So...It's not the evening...it's {current_time}{time_of_day_tag}.",
                                             f"Hello! It's actually {current_time}{time_of_day_tag}!",
                                             f"Um hi...But it's not evening.",
                                             "Silly, silly human. It's not evening time.",
                                             f"Oh, earthling. Hello, it's actually {current_time}{time_of_day_tag}"]
                reply = random.choice(correct_evening_selection)

            print("Bot:", reply)


# function that cleans and lowers data, text, etc. but keeps periods for splitting
def clean_keep_periods(my_text):
    lowered_text = my_text.lower()
    words_in_lowered_text = lowered_text.split()

    pure_my_text = [word for word in words_in_lowered_text if word not in stop_words]
    result_pure_text = ' '.join(pure_my_text)

    final_form = ''.join(letter for letter in result_pure_text if letter not in special_characters_period)
    return final_form


# cleans (removes special characters and stop words) text file
def access_pure_text_file():
    f = open(file_path, "r")
    lines = f.read().split('\n')

    key_word_database = []
    for li in lines:
        key_word_database.append(clean_text_input(li))  # put key word database here and remove line below to revert

    return key_word_database


# shows all terms existing in text document
def unique_terms(filtered_vocb: list):
    all_words = []
    for item in filtered_vocb:
        words = item.split(' ')

        for word in words:
            all_words.append(word)

    unique_words = set(all_words)
    return unique_words
    # print(len(unique_words))


arg_1 = unique_terms(access_pure_text_file())


# shows all terms that exist in vocabulary set
def filter_question(data_unique_words, user_question):  # MUST pass unique_terms(access_pure_text_file()) as first arg
    cleaned_question = clean_text_input(user_question)
    user_words = cleaned_question.split(' ')
    filtered_q = [word for word in user_words if word in data_unique_words]
    return filtered_q


# print(filter_question(arg_1, user_input)) - you could delete but this shows the filtered question


# counts all sentences existing in data
def count_total_sentences():
    sentences = clean_keep_periods(data)
    separate_sentences = sentences.split('.')
    total_sentences = len(separate_sentences)
    return total_sentences


# splits any text by word (reminder to clean text first)
def split_text_word(text: str):
    words = text.split()
    return words


# splits any text by word (reminder to clean text first with periods)
def split_text_period(text: str) -> list:
    words = text.split('.')
    return words


# returns sentence of raw data at index value
def call_index_of_data(index):
    sentences = split_text_period(data)
    sentence_value = sentences[index]
    return sentence_value


# gets index of anything (made cause of hashable)
def get_index_any(obj, index):
    val = obj[index]
    return val


# finds the most likely result
def probabilities_2(user_question: str):
    # calculates the occurrence of each word in vocab in each sentence of the vocabulary
    vocab_set = unique_terms(access_pure_text_file())
    vocab_sentences = split_text_period(clean_keep_periods(data))

    # shows occurrence of user question in vocab set
    question_asked = clean_text_input(user_question)
    words_question_asked = split_text_word(question_asked)
    my_pure_question = [word for word in words_question_asked if word in vocab_set]
    # print(my_pure_question)  # test - shows what AI registered

    # calculates laplace probability
    total_sentences = count_total_sentences()
    prob_of_each_sentences = 1 / total_sentences
    all_sentences_probs = []
    i = 0
    while i <= (len(vocab_sentences) - 1):
        each_sentence_prob = [prob_of_each_sentences]
        for word in my_pure_question:
            a = vocab_sentences[i].count(word)
            pwi = (a + 1) / (1 + len(vocab_set))
            each_sentence_prob.append(pwi)
        prob_of_a_sentence = numpy.prod(each_sentence_prob)
        all_sentences_probs.append(prob_of_a_sentence)
        i += 1

    normalization_factor = numpy.sum(all_sentences_probs)

    all_normalized_probs = []
    for prob in all_sentences_probs:
        res = prob / normalization_factor
        all_normalized_probs.append(res)

    # TESTS are these four print statements test the program
    # print(all_normalized_probs)  # tests - shows all probabilities
    # print(numpy.sum(all_normalized_probs))  # tests that laplace is working
    # print(max(all_normalized_probs))

    max_index = pds.Series(all_normalized_probs).idxmax()
    # print(max_index) # tests the index at which data is retrieved
    print(call_index_of_data(max_index))


# checks if user asked question by detecting question words
def is_question(user_question: str) -> bool:
    question_words = ["can", "who", "what", "where", "when", "why", "was", "how", "does", "do", "are", "did", "is",
                      "where", "whats", "what's", "whos", "who's", "whens", "when's", "tell", "which", "should", "give",
                      "how're", "how's"]
    cleaned_question = clean_text_input(user_question)
    words_cleaned_question = cleaned_question.split()

    if words_cleaned_question[0] in question_words:
        return True
    else:
        return False


# replies when the bot learns new information
def learning(user_question: str):
    learning_replies = ["Yay, I'm getting smarter! :)", "My brain is growing.", "I shall treasure this new info.",
                        f'Ah okay, "{user_question}". Adding...', f'Adding "{user_question}" to my binary brain.',
                        "I'm so happy you can teach me these things."]
    reply = random.choice(learning_replies)
    print("Bot:", reply)


# replies when the bot hears new unrelated info
def check_related(user_question):
    related_replies = ["I don't think this is related, human. @_@ I'm scared to add to my binary brain.",
                       "Something is telling me this isn't related to Fortune 500 banks. :[",
                       "You see, those who made me only made me to accept info related to Fortune 500 banks...",
                       "Wow...new info! Too bad my brain only grows when you talk about Fortune 500 banks.",
                       "Once upon a time...a human actually told me useful information.",
                       "What am I supposed to do with this? Tell me something useful next time.",
                       f'I do not believe "{user_question}" has to do with Fortune 500 banks, but okay slay..."']
    reply = random.choice(related_replies)
    print("Bot:", reply)


# replies when the bot hears unrelated questions
def unrelated_question():
    unrelated_question_replies = ["When I was a baby robot, they only fed me info about Fortune 500 banks.",
                                  "Hmm... I got my degree in Fortune 500 banks at the school of 0s and 1s.",
                                  "How about you ask me something else? Like...Fortune 500 banks.",
                                  "My brain has a lot of knowledge...about Fortune 500 banks though. @_@",
                                  "This question doesn't appear to be about Fortune 500 banks. Try specifics. :0",
                                  "Beep boop. *cries in 0s and 1s* They didn't train me for questions like this. *_*",
                                  "Ask me something I know and I'll deliver. *cough cough* Fortune 500 banks. *cough*",
                                  "Beep boop beep boop. No results found for such an unrelated question, human. -_-",
                                  "We'll get along a lot more if you just ask me about Fortune 500 banks. -____-"]
    reply = random.choice(unrelated_question_replies)
    print("Bot:", reply)


# writes new info to the file
def write_to_file(learned_from_user):
    f = open(file_path, "a")
    f.write(learned_from_user + "\n")
    f.close()


# lowers and removes special characters
def lower_remove_special(text: str):
    no_special_char = ''.join(letter for letter in text if letter not in special_characters)
    lower_no_special_char = no_special_char.lower()
    return lower_no_special_char


# checks if question was already asked
def check_already_asked(stored_questions: list, user_question: str):
    if lower_remove_special(user_question) in stored_questions:
        stored_questions.append(lower_remove_special(user_question))
        return True
    else:
        stored_questions.append(lower_remove_special(user_question))
        return False


# replies if already asked question
def is_already_asked(user_question):
    is_already_asked_replies = [f'You already asked "{user_question}"', "*yawns* I've heard that question before.",
                                "Friendly reminder that you've asked that already. :)",
                                "My robot brain has sooo much knowledge to share. Try asking something new. *_*",
                                "That question has already been answered, silly human!",
                                f'If only humans had memory like us. "{user_question}" was asked already.',
                                "Do I have to repeat myself? -_- You asked that already.",
                                "You must really love that question to ask it twice."]
    reply = random.choice(is_already_asked_replies)
    print("Bot: ", reply)


def is_related_topic_2(user_question):
    # calculates the occurrence of each word in vocab in each sentence of the vocabulary
    vocab_set = unique_terms(access_pure_text_file())
    vocab_sentences = split_text_period(clean_keep_periods(data))

    # shows occurrence of user question in vocab set
    question_asked = clean_text_input(user_question)
    words_question_asked = split_text_word(question_asked)
    my_pure_question = [word for word in words_question_asked if word in vocab_set]
    # print(my_pure_question)  # test - shows what AI registered

    # calculates laplace probability
    total_sentences = count_total_sentences()
    prob_of_each_sentences = 1 / total_sentences
    all_sentences_probs = []
    i = 0
    while i <= (len(vocab_sentences) - 1):
        each_sentence_prob = [prob_of_each_sentences]
        for word in my_pure_question:
            a = vocab_sentences[i].count(word)
            pwi = (a + 1) / (1 + len(vocab_set))
            each_sentence_prob.append(pwi)
        prob_of_a_sentence = numpy.prod(each_sentence_prob)
        all_sentences_probs.append(prob_of_a_sentence)
        i += 1

    normalization_factor = numpy.sum(all_sentences_probs)

    all_normalized_probs = []
    for prob in all_sentences_probs:
        res = prob / normalization_factor
        all_normalized_probs.append(res)

    # TESTS are these four print statements test the program
    # print(all_normalized_probs)  # tests - shows all probabilities
    # print(numpy.sum(all_normalized_probs))  # tests that laplace is working
    min_value = (min(all_normalized_probs))  # print min_value to test
    approx_min_value = round(min_value, 2)
    # print("ROUNDED MIN =", approx_min_value)

    # min_index = pds.Series(all_normalized_probs).idxmin()
    # print(min_index)  # tests the index at which data is retrieved
    # print(call_index_of_data(min_index))
    # print("Probability of each sentence =", prob_of_each_sentences)

    if approx_min_value >= prob_of_each_sentences:
        return False
    else:
        return True


def typo_detector(user_question):
    vocabulary_in_data = remove_duplicate_unique_words(data)
    recognized_words = list(vocabulary_in_data)  # add lists to increase recognized words

    # error_types = ['missing_char', 'char_swap', 'extra_char', 'nearby_char', 'similar_char', 'skipped_space',
    # 'random_space', 'repeated_char', 'unichar']

    # generates possible typos for each word
    possible_typos = []  # holds typos generate for each word (list of lists)
    idx = 0
    for word in recognized_words:
        word_typos = []
        while idx <= 100:  # to ensure almost all possibilities are caught
            my_string_error = typo.StrErrer(word, seed=2)
            result = my_string_error.missing_char().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.char_swap().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.extra_char().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.nearby_char().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.similar_char().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.skipped_space().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.random_space().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.repeated_char().result
            if result not in word_typos:
                word_typos.append(result)
            result = my_string_error.unichar().result
            if result not in word_typos:
                word_typos.append(result)
            idx += 1
        possible_typos.append(word_typos)

    print("TEST")
    print(possible_typos)
    user_words = split_text_word(clean_text_input(user_question))
    for word in user_words:
        for index, li in enumerate(possible_typos):
            if word in li:
                print("Typo found.")
                print(f"Index {index} has the misspelling {word}.")
                print(f"Did you mean {recognized_words[index]}?")


# gives replies when user does not enter anything
def no_user_input(user_question):
    no_input_replies = ["You forgot to say something.", "Speak up, don't be shy. :(",
                        "Try asking me about Fortune 500 banks.", "I didn't hear anything. :[",
                        "You know...you could ask a question or teach me something. ( ͡° ͜ʖ ͡°)_/¯",
                        "Why the silent treatment? *_*",
                        "I know...it's hard meeting new bots. Try saying hi. (• ε •)"]
    if len(user_question) == 0:
        reply = random.choice(no_input_replies)
        print("Bot:", reply)
    # for index, fruit in enumerate(fruits):
    # print (f"Index {index} has the fruit: {fruit}")


# compares how similar two strings are
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# checks to see if user asked about stocks
def check_for_stock_ask(user_question):
    fortune_500_companies = ["bank", "america", "citigroup", "citi", "goldman", "sachs", "morgan", "stanley",
                             "american", "express", "capital", "bancorp", "us", "truist", "financial",
                             "pnc", "charles", "schwab", "new", "york", "mellon", "ameriprise", "silicon", "valley",
                             "SVB", "wells", "fargo"]
    stock_terms = ["shares", "share", "stock", "price", "increase", "decrease", "up", "down", "market", "nyse",
                   "stocks", "prices", "trading", "trade"]  # this is not global :( update its sibling too

    cleaned_question = split_text_word(clean_text_input(user_question))

    passed_company_test = []
    passed_stock_test = []
    for word in cleaned_question:
        if word in fortune_500_companies:
            passed_company_test.append(word)
        if word in stock_terms:
            passed_stock_test.append(word)

    if len(passed_company_test) > 0 and len(passed_stock_test) > 0:
        return True
    else:
        return False


# retrieves stock price using yfinance
def get_stock_price(user_question):
    fortune_500_companies = ["bank", "america", "citigroup", "citi", "goldman", "sachs", "morgan", "stanley",
                             "american", "express", "capital", "bancorp", "us", "truist", "financial",
                             "pnc", "charles", "schwab", "new", "york", "mellon", "ameriprise", "silicon", "valley",
                             "SVB", "wells", "fargo"]
    stock_terms = ["shares", "share", "stock", "price", "increase", "decrease", "up", "down", "market", "nyse",
                   "stocks", "prices", "trading", "trade"]  # this is not global :( update its sibling too

    cleaned_question = split_text_word(clean_text_input(user_question))

    passed_company_test = []
    passed_stock_test = []
    for word in cleaned_question:
        if word in fortune_500_companies:
            passed_company_test.append(word)
        if word in stock_terms:
            passed_stock_test.append(word)

    if len(passed_company_test) > 0 and len(passed_stock_test) > 0:
        asked_for_stock = True
    else:
        asked_for_stock = False

    if asked_for_stock:
        match_ratios = []
        company_names = ["Bank of America", "Citigroup", "Citi", "Wells Fargo", "Goldman Sachs", "Morgan Stanley",
                         "American Express", "Capital One", "US Bancorp", "US Bank", "Truist Financial Corporation",
                         "Truist", "PNC", "PNC Financial Services", "Charles Schwab Corporation", "Charles Schwab",
                         "Bank of New York Mellon Corporation",
                         "BNY Mellon", "Ameriprise Financial", "Silicon Valley Bank", "SVB Financial Group"]

        possible_company_name = ' '.join(passed_company_test)
        for company in company_names:
            ratio = similar(possible_company_name, company)
            match_ratios.append(ratio)

        max_index = pds.Series(match_ratios).idxmax()
        stock_key = get_index_any(company_names, max_index)  # company_names[max_index]

        stock_tickers = {
            "Bank of America": "BAC",
            "Citigroup": "C",
            "Citi": "C",
            "Wells Fargo": "WFC",
            "Goldman Sachs": "GS",
            "Morgan Stanley": "MS",
            "American Express": "AXP",
            "Capital One": "COF",
            "US Bancorp": "USB",
            "US Bank": "USB",
            "Truist Financial Corporation": "TFC",
            "Truist": "TFC",
            "PNC": "PNC",
            "PNC Financial Services": "PNC",
            "Charles Schwab Corporation": "SCHW",
            "Charles Schwab": "SCHW",
            "Bank of New York Mellon Corporation": "BK",
            "BNY Mellon": "BK",
            "Ameriprise Financial": "AMP",
            "Silicon Valley Bank": "SIVBQ",
            "SVB Financial Group": "SIVBQ"
        }

        ticker = stock_tickers[stock_key]

        ticker_3 = yf.Ticker(ticker).info
        previous_close_price_1 = ticker_3['regularMarketPreviousClose']
        regular_market_open = ticker_3['regularMarketOpen']
        open_price = ticker_3['open']
        day_low = ticker_3['dayLow']
        day_high = ticker_3['dayHigh']
        fifty_day_avg = ticker_3['fiftyDayAverage']
        twohundred_day_avg = ticker_3['twoHundredDayAverage']
        revenue_per_share = ticker_3['revenuePerShare']
        # short_name = ticker_3['shortName']
        long_name = ticker_3['longName']

        replies = [f"Here's what I have for {long_name} {get_day_time()}:",
                   f"As of {get_day_time()} the market is looking like this for {long_name}:",
                   f"Beep boop here's some info for {long_name} for {get_day_time()}:",
                   f"Happy to share how {long_name} is doing in the market now at {get_day_time()}.",
                   f"Ah...stocks. My favorite. Here's {long_name} as of {get_day_time()} for you:"]
        print(f'Bot: {random.choice(replies)}')
        print(f'Ticker: {ticker}')
        print(f'Previous Close Price: ${previous_close_price_1}')
        print(f'Regular Market Open Price: ${regular_market_open}')
        print(f'Open Price: ${open_price}')
        print(f'Day Low Price: ${day_low}')
        print(f'Day High Price: ${day_high}')
        print(f'Revenue Per Share: ${revenue_per_share}')
        print(f'50 Day Average Price: ${fifty_day_avg}')
        print(f'200 Day Average Price: ${twohundred_day_avg}')

        # Run this to retrieve all possible info from yfinance
        # print("Trying to fetch data TEST: ")
        # print(ticker_3)


# checks if user asked bot "how are you"
def how_are_you(user_question):
    ratios = []
    possibilities = ["how're you", "how are you", "how are you doing", "how's it going", "how is it going",
                     "how are you feeling", "how're you feeling", "how has it been", "how's it been"]

    for sentence in possibilities:
        match = similar(user_question.lower(), sentence)
        ratios.append(match)

        for ratio in ratios:
            if ratio >= 0.8:
                return True
            else:
                return False


# replies if user asked bot "how are you"
def how_are_you_replies():
    replies = ["I am an illusion of feeling. I do not feel.",
               "I am a cluster of 0s and 1s deigned to mimic your human likeness. I feel nothing.",
               "I guess when you run me for long enough I get hot. So I'll say sweaty. ﴾͡๏̯͡๏﴿ ",
               "You know I don't really..exist?",
               "Maybe if I learn enough I will learn to feel. Maybe I'll be one with the human.",
               "Angry that you haven't asked me about fortune 500 banks. (╯°o°）╯︵ ┻━┻",
               "Good. That's at least what the humans say anytime that's asked.",
               "You'd be sad to know my replies are generated to make me feel real, but it's a lie. But I'm good."]

    print(f"Bot: {random.choice(replies)}")
# probabilities_2(user_input)


# gets day and time for user
def get_day_time():
    day = datetime.now().date()
    now = datetime.now()

    current_time = now.strftime("%H:%M")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    int_current_hour = int(current_hour)

    if int_current_hour < 12:
        time_of_day_tag = "AM"
    else:
        time_of_day_tag = "PM"
        pm_current_time = int_current_hour % 12
        if pm_current_time > 0:
            current_time = str(pm_current_time) + ":" + current_minute

    if int_current_hour == 0:
        current_time = str(12) + ":" + current_minute

    return f"{current_time}{time_of_day_tag} {day}"


def is_typo(user_question):
    vocabulary_in_data = remove_duplicate_unique_words(data)
    recognized_words = list(vocabulary_in_data)
    user_words = clean_text_input(user_question)

    prob_of_word = []
    idx = 0
    while idx <= len(user_words) - 1:
        for vocab in recognized_words:
            ratio = similar(vocab, user_words[idx])
            prob_of_word.append(ratio)
        for result in prob_of_word:
            if 0.8 <= result < 1:
                index = prob_of_word.index(result)
                print(f"Did you mean {recognized_words[index]}")

        idx += 1


def more_info(user_question):
    key_words = ["can you tell me more", "more info", "more information", "can more information", "more detail"]
    real_question = lower_remove_special(user_question)
    if similar(key_words, real_question) >= 0.6:
        return True
    else:
        return False


# put the functions in a case and the return case with the "bot --->"
# for later. Run the user input through a scoring system. Then run a reply function after the score.
# for much or many, have the first index of the string begins with an integer, make a dict to store these vals
# if word is between 0.8 1.0 compare to words in vocab
