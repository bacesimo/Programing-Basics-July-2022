days = int(input())
type_room = input()
rating = input()

price = 0
diff_days = days - 1

if type_room == "room for one person":
    price = diff_days * 18
elif type_room == "apartment":
    if days < 10:
        price = diff_days * 25 * 0.7
    elif 10 <= days <= 15:
        price = diff_days * 25 * 0.65
    else:
        price = diff_days * 25 * 0.5
elif type_room == "president apartment":
    if days < 10:
        price = diff_days * 35 * 0.9
    elif 10 <= days <= 15:
        price = diff_days * 35 * 0.85
    else:
        price = diff_days * 35 * 0.8

if rating == "positive":
    price = price * 1.25
else:
    price = price * 0.90

print(f"{price:.2f}")