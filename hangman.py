import random

print("#" * 80)
print("#" * 30 + "  HANGMAN GAME  " + "#" * 29)
print("#" * 80)

hangman = ["""
+---+
   |   |
       |
       |
       |
       |
--------
""", """"
   +---+
   |   |
   O   |
       |
       |
       |
--------
""", """
   +---+
   |   |
   O   |
   |   |
       |
       |
--------
""", """
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------
""", """
   +---+
   |   |
   O   |
  /|\  |
       |
       |
--------
""", """
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------
""", """
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------
"""]

easy_categories = {
    "countries": ["america", "turkey", "italy", "spain", "portugal", "poland", "azerbaijan", "england", "russia",
                  "syria", "denmark", "austria", "hungary", "bulgaria", "serbia", "thailand", "china", "japan"],
    "animals": ["chicken", "cow", "lion", "tiger", "turtle", "fish", "cat", "dog", "monkey", "gorilla", "whale",
                "hedgehog", "squirrel"],
    "items": ["faucet", "hammer", "lighter", "hose", "bulb", "scarf", "antenna", "lampshade", "pillow", "bed", "sofa",
              "couch", "armchair", "table"],
}

hard_categories = {
    "countries": ["abhazya", "andorra", "angola", "burundi", "eritrea", "gabon", "kiribati", "comoros", "mauritius",
                  "rwanda", "sealand", "zimbabwe"],
    "animals": ["octopus", "hyena", "tarantula", "frog", "tertiary", "goeduck", "ukari", "axolotl", "mantis", "shrimp",
                "jellyfish", "squid"],
    "items": ["girder", "wrench", "dynamo", "strapless", "clip", "plane", "saxophone","Zephyrometer","Hypsometer","Abaculus"],
}


def select_word(category, level):
    if level == "1":
        return random.choice(easy_categories[category])
    elif level == "2":
        return random.choice(hard_categories[category])
    else:
        return None


def play_hangman(category, level):
    chosen_word = select_word(category, level)

    if chosen_word is None:
        print("Invalid level selection.")
        return

    max_guesses = 6
    correct_letters = []
    incorrect_letters = []
    word_length = len(chosen_word)
    word_display = list('_' * word_length)
    print(hangman[0])

    if category == "countries":
        print("Hint: Your word is a country.")
    elif category == "animals":
        print("Hint: Your word is an animal.")
    elif category == "items":
        print("Hint: Your word is an item.")

    print(' '.join(word_display), end='\n')

    while max_guesses > 0:
        if word_display == list(chosen_word):
            print("You Win!")
            return

        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1:
            if guess in correct_letters:
                print(hangman[6 - max_guesses])
                print(' '.join(word_display), end='\n')
                print("Incorrect guesses: {}".format(incorrect_letters))
                print("You already guessed this letter!")

            elif guess not in chosen_word:
                max_guesses -= 1
                print(hangman[6 - max_guesses])
                print(' '.join(word_display), end='\n')
                incorrect_letters.append(guess)
                print("Incorrect guesses: {}".format(incorrect_letters))
                print("\nWRONG GUESS! Guesses left: {}".format(max_guesses))

            else:
                for i in range(len(chosen_word)):
                    if guess == chosen_word[i]:
                        print(hangman[6 - max_guesses])
                        word_display[i] = guess
                        correct_letters.append(guess)
                print(' '.join(word_display), end='\n')
                print("Incorrect guesses: {}".format(incorrect_letters))
                print("\nCORRECT GUESS! Guesses left: {}".format(max_guesses))

        elif len(guess) > 0:
            if guess == chosen_word:
                print("\nCONGRATULATIONS!!! You guessed the word.")
                return
            else:
                max_guesses -= 1
                print(hangman[6 - max_guesses])
                print(' '.join(word_display), end='\n')
                print("Incorrect guesses: {}".format(incorrect_letters))
                print("\nWRONG GUESS! Guesses left: {}".format(max_guesses))

    print("\nYou've run out of guesses. \nYou lose! The hangman is hanged.")
    print(f"Correct Word: {chosen_word}")


while True:
    level = input("""Please select the level 
            1. Easy Level
            2. Hard Level
            >>>""")

    category = random.choice(["countries", "animals", "items"])

    if level not in ["1", "2"]:
        print("Invalid input. Please use 1 or 2.")
        continue

    play_hangman(category, level)
