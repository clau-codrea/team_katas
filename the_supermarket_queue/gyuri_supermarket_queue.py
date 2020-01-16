from functools import reduce

def queueTime(customers, n):
    return max(reduce(updateTills, customers, [0] * n))

def updateTills(acc, customer):
    value = min(acc)
    index = acc.index(value)
    return acc[:index] + [value + customer] + acc[index:][1:]
