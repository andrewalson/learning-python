def findpezos(names):
    numpez = 0
    for item in names:
        if item == 'pezos':
            numpez = numpez + 1
    return numpez

def findindexofpezos(names):
    loop = 0
    for item in names:
        if item == 'pezos':
            return loop
        loop = loop + 1

#don't use built-in functions