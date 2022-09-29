type_flowers = input()
count_flowers = int(input())
budget = int(input())

expenses = 0
if type_flowers == "Roses":
    expenses = 5 * count_flowers
    if count_flowers > 80:
        expenses = expenses * 0.90
elif type_flowers == "Dahlias":
    expenses = 3.80 * count_flowers
    if count_flowers > 90:
        expenses = expenses * 0.85
elif type_flowers == "Tulips":
    expenses = 2.80 * count_flowers
    if count_flowers > 80:
        expenses = expenses * 0.85
elif type_flowers == "Narcissus":
    expenses = 3 * count_flowers
    if count_flowers < 120:
        expenses = expenses * 1.15
elif type_flowers == "Gladiolus":
    expenses = 2.50 * count_flowers
    if count_flowers < 80:
        expenses = expenses * 1.20

diff = abs(budget - expenses)
if budget >= expenses:
    print (f"Hey, you have a great garden with {count_flowers} {type_flowers} and {diff:.2f} leva left.")
else:
    print (f"Not enough money, you need {diff:.2f} leva more.")
