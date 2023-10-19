from operator import inv
import random

#list letters in alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#list to hold 10 letters
game_letters = []

#populate empty list with 10 letters from alphabet
def populate_letters():
    for i in range(10):
        letter = random.randint(0, 25)
        game_letters.append(alphabet[letter])

#prompt user for four words
def prompt_user():
    user_words = []
    for i in range(4):
        word = input('')
        user_words.append(word)
    return user_words

def check_words(user_words):
    valid_words = []
    invalid_words = []
    for word in user_words:
        valid = True
        for letter in word:
            letter = letter.lower()
            if letter not in game_letters:
                valid = False
                #strikeout whole word
        if valid == False or word == "" or word.isspace():
            invalid_words.append('\u0336'.join(word) + '\u0336')
        else:
            valid_words.append(word)
    print_results(valid_words, invalid_words)

def print_results(valid_words, invalid_words):
    print("These are the valid words.")
    for word in valid_words:
        print(word)
    print("These are the invalid words.")
    for word in (invalid_words):
        print(word)
    print("Total point scored: ", str(len(valid_words)))

populate_letters()
print(game_letters)
words = prompt_user()
check_words(words)

#start game
    #print 10 letters
    #loop 4 times 
        #ask user to enter words built from 10 letters
#print user entered words
