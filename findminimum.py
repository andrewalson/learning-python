def findminimum(numlist):
    min = numlist[0]
    for i in numlist:
        if i < min:
            min = i
    return min