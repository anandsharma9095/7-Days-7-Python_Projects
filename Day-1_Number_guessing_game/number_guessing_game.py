#Day 1 - Number Guessing Game

import random

print('Welcome to my Number Guessing Game !!')

#Checking the validity of the input

while True:
    level = input('Enter the size of your Game\nIn between 1 - ')
    print()
    
    if level.isdigit():
        level = int(level)
        break
    else:
        print('Enter a number and Enter it without spaces')
        continue
    

ans = random.randint(1,level)

print(f'I am thinking of a number between 1 to {level}... \n\nAnd you have to guess in as minimum attempts as possible\nEnter "q" to quit\n')

score = 0
while True:
    answer = input('Enter your guess : ')
    if answer.isdigit():
        answer = int(answer)
    else:
        print('Enter a number and Enter it without spaces')
        continue
    
    if answer == 'q' :
        print('You Quit!')
        score += 1
        quit()
    elif answer == ans:
        score += 1
        break
    elif answer < ans:
        print('Your guess was low guess it a little higher !!\n')
        score += 1
    else:
        print('Your guess was high guess it a little lower !!\n')
        score += 1

print(f'You guessed it in {score} attempts')