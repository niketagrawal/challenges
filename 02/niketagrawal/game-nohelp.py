#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
from typing import Dict
from data import DICTIONARY, LETTER_SCORES, Letter, POUCH

NUM_LETTERS = 7


def draw_letters():
    drawn_letters = []
    for i in range(NUM_LETTERS):
        drawn_letters.append(random.choice(POUCH))
    return drawn_letters


def input_word():
    return(input("Enter your word "))


def validate_input(word: str, drawn_letters: list):
    if word in DICTIONARY and (True for letter in word if letter in drawn_letters):
        print("input is valid")
    else:
        print("input is invalid")


def load_words():
    """
    Load words from the dictionary into a list and return the list
    Returns
    -------
    words: list
        list of words
    """
    with open(DICTIONARY) as d:
        word_list = []
        word_list = d.read().splitlines()
    return word_list


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    """
    Calculates the value of the word entered into function
    using imported constant mapping LETTER_SCORES
    Parameters
    ----------
    word : str
        A word from the dictionary
    Returns
    -------
    value: int
        The scrabble value for the word received as argument
    """
    value = 0
    word_upper = word.upper()
    for letter in word_upper:
        if ((ord(letter) >= 65 and ord(letter) <= 90) or (ord(letter) >= 97 and ord(letter) <= 122)):
            value += LETTER_SCORES[letter]
    return value
    #return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(list_of_words=None):
    """
    Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY
    Returns
    -------
    max_value_word : str
        The word with the max value on Scrabble
    """
    value_list = []
    value_to_word = {}
    if not list_of_words:
        list_of_words = load_words()

    for word in list_of_words:
        word_value = calc_word_value(word)
        value_list.append(word_value)
        value_to_word[word_value] = word
    value_list.sort()
    max_value = value_list[-1]
    max_value_word = value_to_word[max_value]
    return max_value_word
    #return max(words, key=calc_word_value)


def find_optimal_word(drawn_letters: list):
    pass


def main():
    # Draw 7 random letters from POUCH
    drawn_letters: list = draw_letters()

    print(f"The letters drawn are {drawn_letters}")

    word_created = input_word()

    # Validate input for: 1) all letters of word are in draw; 2) word is in DICTIONARY. 
    validate_input(word_created, drawn_letters)

    # Calculate the word value and show it to the player
     
    value = calc_word_value(word_created)
    print(f"The value for your created word is {value}")

    # Calculate the optimal word (= max word value) checking all permutations of the 7 letters of the draw, cross-checking the DICTIONARY set for valid ones. This is a bit more advanced, but allows you to score the player (next).
    
    # Show the player what the optimal word and its value is.
    optimal_word = find_optimal_word(drawn_letters)
    print(f"Optimal word that can be formed from your drawn set of letters is {optimal_word}")

    # Give the player a score based on the previous steps, basically: player_score / optimal_score.


def trial():
    word = "abAc"
    if word in DICTIONARY:
        print("word found")
    else:
        print("word not found")


if __name__ == "__main__":
    main()
