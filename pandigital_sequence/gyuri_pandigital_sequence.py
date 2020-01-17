from functools import reduce
from itertools import permutations

def toNumber(digitlist):
    return sum(list(map(
            lambda t: (10 ** t[0]) * t[1],
            zip(range(len(digitlist)-1, -1, -1), digitlist)
            )))

def getSequence(offset, size):
    nrOfZeros = reduce(lambda x,y: x * y, range(1, 10))
    pandigitals = list(map(toNumber, permutations(range(10))))[nrOfZeros:]
    return pandigitals[offset : offset + size]
