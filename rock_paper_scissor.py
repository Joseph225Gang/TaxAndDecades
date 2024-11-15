import random

computer_choice = random.choice(['rock','paper','scissors'])
user_choice = input('Do you want rock, paper, or scissors?')

print('Computer choice:', computer_choice)

win_scenario1 =  user_choice == 'rock' and computer_choice == 'scissors'
win_scenario2 =  user_choice == 'paper' and computer_choice == 'rock'
win_scenario3 =  user_choice == 'scissors' and computer_choice == 'paper'

if computer_choice == user_choice:
    print('TIE')
elif win_scenario1 or win_scenario2 or win_scenario3:
    print('WIN')
else:
    print('You lose, computer wins :')