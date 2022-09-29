need_money = float(input())
available_money = float(input())

total_money = available_money
days_count = 0
count_spend_days = 0
while total_money < need_money:
    if count_spend_days == 5:
        break
    action = input()
    amount = float(input())

    days_count += 1
    if action == "spend":
        count_spend_days += 1
        total_money -= amount
        if total_money < 0:
            total_money = 0
    elif action == "save":
        count_spend_days = 0
        total_money += amount

if count_spend_days == 5:
    print("You can't save the money.")
    print(days_count)

else:
    print(f"You saved the money for {days_count} days.")
