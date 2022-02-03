from csv import reader
from random import randint

# Opens our list of possible answers
# List starts as a CSV file and is converted to one list of word strings (in uppercase)
file = open('C:/Users/0996516/Downloads/wordle-answers-alphabetical.csv', 'r')
csv_reader = reader(file)
lists_from_csv = []
for row in csv_reader:
    word_string = ""
    for letter in row:
        word_string += letter.upper()
    lists_from_csv.append(word_string)

# Picks a random Word from our newly created Word-List
word = lists_from_csv[randint(0, 2314)]

# Initializes Guess to an empty string and starts on Guess #1
guess = ""
guess_count = 1
good_hint = ["_", "_", "_", "_", "_"]
okay_hint = []
bad_hint = []

# A loop that continues to ask the user for a new 5-letter word (or a "Guess")
# You win after guessing the Word, you lose after 6 wrong Guesses
# Guesses are automatically converted to uppercase so that they can be compared to our Word-List, which is all uppercase
while guess != word:
    if guess_count > 6:
        print("You used all six guesses. You lose. The word was " + word + ".")
        break
    guess = input(f"Guess #{guess_count}: ").upper()
    # The following 2 loops verify that the user's Guess is both a 5-letter word AND in the Word-List
    # If either or both of these qualifications are not met, the program asks the user for a new Guess
    # Since these Guesses are not possible answers, they don't count against the Guess-Count
    while len(guess) != 5:
        print("Guess must be 5 characters.")
        print()
        guess = input(f"Still Guess #{guess_count}: ").upper()
    while guess not in lists_from_csv:
        print("Word not in word list.")
        print()
        guess = input(f"Still Guess #{guess_count}: ").upper()
    # Now that we've verified the current Guess is valid, the Guess-Counter is incremented
    guess_count += 1

    # Compares a valid Guess to the actual Word and prints indicators next to each Guess letter
    # + means the letter is in the Word and in the right place
    # o means the letter is in the Word, but in a different place
    # x means the letter is not in the Word at all
    index_counter = 0
    for i in guess:
        if i == word[index_counter]:
            print(f"{i}(+) ", end="  ")
            good_hint.pop(index_counter)
            good_hint.insert(index_counter, i)
            if i in okay_hint:
                okay_hint.remove(i)
        elif i in word:
            if i != word[index_counter]:
                print(f"{i}(o) ", end="  ")
                if i not in okay_hint:
                    okay_hint += i
        else:
            print(f"{i}(x) ", end="  ")
            if i not in bad_hint:
                bad_hint += i
        index_counter += 1
    print()
    print()

    clean_good_hint = ""
    for i in good_hint:
        clean_good_hint += i

    clean_okay_hint = ""
    okay_hint.sort()
    for i in okay_hint:
        clean_okay_hint += i

    bad_hint.sort()
    clean_bad_hint = ""
    for i in bad_hint:
        clean_bad_hint += i

    print(f"Word: {clean_good_hint}")
    if guess != word:
        print(f"Contains: {clean_okay_hint}")
        print(f"Does not contain: {clean_bad_hint}")
    print()

if guess == word:
    print("You win!")
