
import random


class Hangman:

    POSSIBLE_WORDS = ['becode', 'learning', 'mathematics', 'sessions']

    lives = 10
    turn_count = 0
    error_count = 0

    def __init__(self):
        # word_to_find is assigned a random word from POSSIBLE_WORDS and is split into a list
        self.word_to_find = list(random.choice(self.POSSIBLE_WORDS).upper())
        self.correctly_guessed_letters = "_ " * len(self.word_to_find)
        self.wrongly_guessed_letters = ""

    def play(self):

        while True:
            print(f"Hidden word: {self.correctly_guessed_letters}")
            input_guess = input("Enter a letter: ").upper()

            # checks if input is a single letter
            while not input_guess.isalpha() or not len(input_guess) == 1:
                input_guess = input(
                    "Invalid input, only enter a single letter: ").upper()

            # checks if the word contains the letter input
            if input_guess in self.word_to_find:
                print("Well done! You found a letter!")
                # indexe(s) of the letter found inside the word
                indexes = [i for i, x in enumerate(self.word_to_find) if x == input_guess]
                # split correctly_guessed_letters into a list
                correctly_guessed_letters_list = list(self.correctly_guessed_letters)
                # replace the underscore(s) inside the correctly_guessed_letters with the letter
                for i in indexes:
                    # the index has to be *2 as each underscore is separated by a space
                    correctly_guessed_letters_list[i*2] = input_guess
                # convert correctly_guessed_letters_list into a string and assign it to correctly_guessed_letters
                self.correctly_guessed_letters = "".join(correctly_guessed_letters_list)

            else:
                # appends the letter to wrongly_guessed_letters if not contained in the word and not already in added in wrongly_guessed_letters
                if input_guess not in self.wrongly_guessed_letters:
                    self.wrongly_guessed_letters += input_guess + " "
                self.lives -= 1
                self.error_count += 1
                if self.lives > 0:
                    print(f"{input_guess} is not part of the word. Try again!")

            self.turn_count += 1

            print(
                f"Wrongly guessed letter: {self.wrongly_guessed_letters}\nLife remaining: {self.lives}\nError count: {self.error_count}\nTurn count: {self.turn_count}")

            break

    def game_over(self):
        print("Game over...")
        exit()

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
        exit()

    def start_game(self):
        while True:
            if self.lives == 0:
                self.game_over()
            # checks if correctly_guessed_letters contains an underscore, if it doesn't all the letters have been discovered
            if self.correctly_guessed_letters.find("_") == -1:
                self.well_played()
            else:
                self.play()
