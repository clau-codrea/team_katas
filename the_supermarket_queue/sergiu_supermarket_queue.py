def queue_time(customers, n):
    if not customers:
        return 0
    tills = [0 for _ in range(n)]
    total_time = 0
    current_index = 0
    customers_count = len(customers)
    while current_index < customers_count:
        for index, till in enumerate(tills):
            if till == 0 and current_index < customers_count:
                tills[index] = customers[current_index] - 1
                current_index += 1
            else:
                tills[index] = till - 1
        total_time += 1
    return total_time + max(tills)
