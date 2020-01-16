def add_time(till_times, customer):
    quickest_till = till_times.index(min(till_times))
    till_times[quickest_till] += customer
    return till_times


def queue_time(customers, n):
    till_times = [0] * n
        
    for customer in customers:
        till_times = add_time(till_times, customer)
        
    return max(till_times) 
