def pos_neg(num1, num2, negative):
    '''Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both are negative.'''
    if negative:
        return (num1 < 0 and num2 < 0)
    else:
        if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
            return True

def makes10(a, b):
    '''# Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.'''
    return

def diff21(num):
    '''Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.'''
    if num - 21 > 21:
        return 2 * abs(num - 21)
    else:
        return abs(num - 21)


def front_back(word):
    ''' Given a string, return a new string where the first and last chars have been exchanged.'''
    pass
    #    if len(str) <= 1:
    #        return str
    #    mid = str[1:len(str) - 1]  #can be written as str[1:-1]

        #last + mid + first
    #    return str[len(str) - 1] + mid + str[0]

def front3(word):
    '''#Given a string, we'll say that the front is the first 3 chars of the string.
    If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.'''

    # Figure the end of the front
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front + front + front

    # Could omit the if logic, and write simply front = str[:3]
    # since the slice is silent about out-of-bounds conditions.