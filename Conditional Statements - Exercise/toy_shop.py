trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

total_sum = (puzzles * 2.6) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)
total_count = puzzles + dolls + bears + minions + trucks

if total_count >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (total_sum * 0.10)
total_price = abs(total_sum - trip_price)
if total_sum >= trip_price:
    print(f"Yes! {total_price:.2f} lv left.")
else:
    print(f"Not enough money! {total_price:.2f} lv needed.")

