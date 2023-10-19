from mimetypes import guess_all_extensions
import random

answer = random.randint(0, 200)
correct = False

for guess in range(5):
    user_input = input("Guess a number between 0 and 200.") 
    user_input = int(user_input)
    if user_input < answer:
        print("Incorrect, guess again higher.")
    elif user_input > answer:
        print('Incorrect, guess again lower.')
    else:
        print ('Congratulations, correct answer! Game over. Byee!')
        correct = True
        break

if correct == False:
    print('Sorry, you lose. The correct answer is ', answer)
