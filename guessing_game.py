"""
Project 1 - Number Guessing Game
--------------------------------
"""

import random
from statistics import mean, median, mode

guess_list = []
previous_scores = []


def add_guess(attempt):
  global guess_list # FOR REVIEWER: I included the 'global' keyword because I couldn't access the guess_list global keyword otherwise. I never could figure out why this was the case.
  guess_list.append(attempt)

def start_game():

  end_game = False
  correct_guess = False

  print("Welcome to the Number Guessing Game!")

  while not end_game:
    answer = random.choice(range(0, 100))

    if(len(previous_scores) != 0):
      print(f'The current best score is {min(previous_scores)}')

    while not correct_guess:
      try:

        player_guess = input("Please guess an integer between 1-100: ")
        player_guess = int(player_guess)
        
        if player_guess < 1 or player_guess > 100:
          print('The number you provided is not between 1-100.')
          continue

        if player_guess < answer:
          print('It\'s higher.')
          add_guess(player_guess)
        elif player_guess > answer:
          print('It\'s lower.')
          add_guess(player_guess)
        else: 
          print('That\'s correct!')
          add_guess(player_guess)
          previous_scores.append(len(guess_list))
          correct_guess = True

        # print(guess_list) 
        # print(len(guess_list))

      except Exception as e:
        print('The value you provided is not an integer.')  
        # print(e) 

    print(f'You made {len(guess_list)} guesses before getting the correct number.')
    print(f'The mean of your attempts is {mean(guess_list)}.\nThe median of your attempts is {median(guess_list)}.\nThe mode of your attempts is {mode(guess_list)}.')

    play_again = input('Would you like to play again? [Y/N] ').upper()
    if play_again == 'Y':
      correct_guess = False
      guess_list.clear()
    elif play_again == 'N':
      end_game = True
      print('Thanks for playing!')
      continue
    

# Kick off the program by calling the start_game function.
start_game()