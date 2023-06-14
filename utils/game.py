
import random
import sys


class Hangman:

    POSSIBLE_WORDS = ['becode', 'learning', 'mathematics', 'sessions']

    lives = 10
    turn_count = 0
    error_count = 0

    def __init__(self):

        self.word_to_find = list(random.choice(self.POSSIBLE_WORDS).upper())
        self.correctly_guessed_letters = "_ " * len(self.word_to_find)
        self.wrongly_guessed_letters = ""

    def play(self):
        while True:

            input_guess = input("Enter a letter: ").upper()

            while not input_guess.isalpha() or not len(input_guess) == 1:
                input_guess = input(
                    "Invalid input, only enter a single letter: ").upper()

            if input_guess in self.word_to_find:
                print("Well done! You found a letter!")

                indexes = [i for i, x in enumerate(self.word_to_find) if x == input_guess]
                correctly_guessed_letters_list = list(self.correctly_guessed_letters)
                for i in indexes:
                    correctly_guessed_letters_list[i*2] = input_guess

                self.correctly_guessed_letters = "".join(correctly_guessed_letters_list)

            elif input_guess not in self.word_to_find:
                self.wrongly_guessed_letters += input_guess + " "
                self.lives -= 1
                self.error_count += 1
                if self.lives > 0:
                    print(f"{input_guess} is not part of the word. Try again!")

            self.turn_count += 1

            print(
                f"Correctly guessed letters: {self.correctly_guessed_letters}\nWrongly guessed letter: {self.wrongly_guessed_letters}\nLife remaining: {self.lives}\nError count: {self.error_count}\nTurn count: {self.turn_count}")

            if self.lives == 0:
                self.game_over()

            if self.correctly_guessed_letters.find("_") == -1:
                self.well_played()

    def game_over(self):
        print("Game over...")
        sys.exit()

    def well_played(self):
        print(f"You found the word: {''.join(self.word_to_find)} in {self.turn_count} turns with {self.error_count} errors!")
        sys.exit()


game = Hangman()

game.play()
