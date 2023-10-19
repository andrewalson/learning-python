def reverseString(word):
    revword = ''
    for i in range(-1, -1 - len(word), -1):
        revword = revword + word[i]
    return revword

#palindrome function takes in a string
    #use reverseString(string) to determine if palindrome
def ispal(word):
    word = word.lower()
    revString = reverseString(word)
    if revString == word: 
        return True
    else:
        return False

#loops
# modulus gives you remainder
def isPrime(number): 
    for x in range(2, number):
        if number%x == 0:
            return False
    return True 

   # if number % (2, number, 1) != 0
    #return True