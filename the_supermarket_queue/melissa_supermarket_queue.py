def queue_time(customers, n):

    if not customers:
        return 0


    tills = [0] * n
    
    while customers: 
        min_index = tills.index(min(tills))
        tills[min_index] += customers.pop(0)


    return max(tills)

