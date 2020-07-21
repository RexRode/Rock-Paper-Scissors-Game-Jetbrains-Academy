# Write your code here
import random

user_move = input()
options = ['rock', 'paper', 'scissors']
computer_move = random.choice(options)
wins = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}


def game():
    if user_move == computer_move:
        print(f'There is a draw ({user_move})')
    elif user_move == wins[computer_move]:
        print(f'Well done. Computer chose {computer_move} and failed')
    elif computer_move == wins[user_move]:
        print(f'Sorry, but computer chose {computer_move}')


while True:
    if user_move == "!exit":
        print("Bye!")
        exit()
    elif user_move in options:
        game()
        user_move = input()
        computer_move = random.choice(options)
    else:
        print("Invalid input")
        user_move = input()
        computer_move = random.choice(options)