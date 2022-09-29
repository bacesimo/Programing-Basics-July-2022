ticket_type = input()
rows = int(input())
columns = int(input())

all_seats = rows * columns

price = 0

if ticket_type == "Premiere":
    price = 12
elif ticket_type == "Normal":
    price = 7.50
elif ticket_type == "Discount":
    price = 5

income = all_seats * price

print(f"{income:.2f} leva")
