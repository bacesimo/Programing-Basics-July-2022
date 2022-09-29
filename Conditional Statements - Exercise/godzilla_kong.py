budget = float(input())
count_statist = int(input())
price_clothing = float(input())

decor_sum = budget * 0.1
clothes_price = count_statist * price_clothing

if count_statist > 150:
    clothes_price = clothes_price - (clothes_price * 0.1)

total_money = decor_sum + clothes_price

checks = abs(total_money - budget)
if budget >= total_money:
    print("Action!")
    print(f"Wingard starts filming with {checks:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {checks:.2f} leva more.")