#import random module

import random

#define a welcome function to welcome user by name

def welcome():
    user_name=input("What is your game name?: ").capitalize()

    if user_name.isalpha():
        print("Hi", user_name,"! We're glad to have you here today :) \n You will have 6 attempts to correctly guess letters in the word, which will be generated by a computer.")

    else:
        print("Please enter a name using only letters.")
        user_name=input("What is your game name?: ").capitalize()
        print("Hi", user_name,"! We're glad to have you here today :) \n You will have 6 attempts to correctly guess letters in the word, which will be generated by a computer.")

#define function asking the user if the want to play again

def play_again():
    user_response = input("Would you like to play the game again? Enter \"y\" or \"n\" : ").lower()

    if user_response == "y":
        run_game()
    elif user_response == "n":
        print("See you next time!")
    else:
        print("invalid input")
        user_response = input("Would you like to play the game again? Enter \"y\" or \"n\" : ").lower()

#Define function for generating the random word that will be guessed by the user

def random_word():
    words = ["boat","dog","house","store","snake","apple","peanut"]
    return random.choice(words).lower()

#define function to run the game

def run_game():
    welcome()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    game_word= random_word()
    user_guesses=[]
    user_tries = 7
    guess = False
    print("")
    print("There are", len(game_word),"in the word")