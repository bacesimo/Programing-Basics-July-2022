import math

number_of_days = int(input())
kilometers = float(input())

day = 0
total_sum_km = kilometers

while day < number_of_days:
    percent_daily = int(input())
    kilometers = kilometers * (1 + percent_daily / 100)
    total_sum_km += kilometers
    day += 1

result_of_workout = math.ceil(total_sum_km - 1000)
diff = math.ceil(1000 - total_sum_km)

if total_sum_km >= 1000:
    print(f"You've done a great job running {result_of_workout} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {diff} more kilometers")