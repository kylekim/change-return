import decimal
from decimal import Decimal


def find_change():
    cost = input("Enter cost: ")

    try:
        cost = Decimal(cost)
    except decimal.InvalidOperation:
        print("Invalid input.")
        quit()

    cost = round(cost, 2)
    cost = cost * 100

    give = input("Enter amount given: ")

    try:
        give = Decimal(give)
    except decimal.InvalidOperation:
        print("Invalid input.")
        quit()

    give = round(give, 2)
    give = give * 100

    total_change = give - cost
    change = total_change

    if change <= 0:
        print("\nNo change.")
        quit()

    q = 0
    d = 0
    n = 0
    p = 0

    while change > 0:
        if change >= 25:
            change -= 25
            q += 1
        elif change >= 10:
            change -= 10
            d += 1
        elif change >= 5:
            change -= 5
            n += 1
        elif change >= 1:
            change -= 1
            p += 1

    print(f"\nTotal change: {total_change / 100}\n"
          f"    Quarters: {q}\n"
          f"    Dimes: {d}\n"
          f"    Nickels: {n}\n"
          f"    Pennies: {p}")


find_change()
