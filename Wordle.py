from csv import reader
from random import randint


# Takes the file path of the answer csv file and outputs a list of possible answer strings (all in uppercase)
def answers_list_maker(file_path):
    file = open(file_path, 'r')
    csv_reader = reader(file)
    lists_from_csv = []
    for row in csv_reader:
        word_string = ""
        for letter in row:
            word_string += letter.upper()
        lists_from_csv.append(word_string)
    return lists_from_csv


# Takes the file path of the allowed guesses csv file and outputs a list of answer strings (all in uppercase)
# These are words that aren't possible answers, but are still allowed as guesses
def guesses_list_maker(file_path):
    file = open(file_path, 'r')
    csv_reader = reader(file)
    lists_from_csv = []
    for row in csv_reader:
        word_string = ""
        for letter in row:
            word_string += letter.upper()
        lists_from_csv.append(word_string)
    return lists_from_csv


# Compares a valid Guess to the actual Word and prints indicators next to each Guess letter
# + means the letter is in the Word and in the right place
# o means the letter is in the Word, but in a different place
# x means the letter is not in the Word at all
def guess_handler(guess, word, good_hint, bad_hint, okay_hint):
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

    # Convert hints from lists into strings, to print them cleaner
    clean_good_hint = ""
    for i in good_hint:
        clean_good_hint += i

    clean_okay_hint = ""
    okay_hint.sort()
    for i in okay_hint:
        clean_okay_hint += i

    clean_bad_hint = ""
    bad_hint.sort()
    for i in bad_hint:
        clean_bad_hint += i

    print(f"Word: {clean_good_hint}")
    if guess != word:
        print(f"Contains: {clean_okay_hint}")
        print(f"Does not contain: {clean_bad_hint}")
    print()

    return good_hint, bad_hint, okay_hint


def main():
    guess = ""
    guess_count = 1
    guesses_list = guesses_list_maker('C:/wordle-allowed-guesses.csv')
    answers_list = answers_list_maker('C:/wordle-answers-alphabetical.csv')
    word = answers_list[randint(0, 2314)]
    good_hint = ["_", "_", "_", "_", "_"]
    okay_hint = []
    bad_hint = []

    # A loop that continues to ask the user for a new 5-letter word (or a "Guess")
    # You win after guessing the Word, you lose after 6 wrong Guesses
    # Guesses are automatically converted to uppercase so that they can be compared to our uppercase Word-List
    while guess != word:
        if guess_count > 6:
            print("You used all six guesses. You lose. The word was " + word + ".")
            break
        guess = input(f"Guess #{guess_count}: ").upper()

        # 2 loops to verify the (Guess is both a 5-letter word) AND (in either the Guess-List or the Answer-List)
        # If either or both of these qualifications are not met, the program asks the user for a new Guess
        # Since these Guesses are not possible answers, they don't count against the Guess-Count
        while len(guess) != 5:
            print("Guess must be 5 characters.")
            print()
            guess = input(f"Still Guess #{guess_count}: ").upper()
        while (guess not in answers_list) and (guess not in guesses_list):
            print("Word not in word list.")
            print()
            guess = input(f"Still Guess #{guess_count}: ").upper()

        # Now that we've verified the current Guess is valid, the Guess-Counter is incremented
        guess_count += 1

        guess_handler(guess, word, good_hint, bad_hint, okay_hint)

    if guess == word:
        print("You win!")


if __name__ == "__main__":
    main()
