def queue_time(customers, tills_count):
    tills = [0] * tills_count

    for customer in customers:
        tills = process_customer(customer, tills)

    return tills[-1]


def process_customer(customer, tills):
    tills[0] += customer

    index = 0
    while index < len(tills) - 1 and tills[index] > tills[index + 1]:
        aux = tills[index]
        tills[index] = tills[index + 1]
        tills[index + 1] = aux

        index += 1

    return tills
