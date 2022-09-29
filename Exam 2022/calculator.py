count_people = int(input())
season = input()

price = 0

if season == "spring":
    if count_people <= 5:
        price = 50
    if count_people > 5:
        price = 48

if season == "summer":
    if count_people <= 5:
        price = 48.50 - (48.50 * 0.15)
    if count_people > 5:
        price = 45 - (45 * 0.15)

if season == "autumn":
    if count_people <= 5:
        price = 60
    if count_people > 5:
        price = 49.50


if season == "winter":
    if count_people <= 5:
        price = 86 + (86 * 0.08)
    if count_people > 5:
        price = 85 + (85 * 0.08)

total_sum = count_people * price

print(f"{total_sum:.2f} leva.")