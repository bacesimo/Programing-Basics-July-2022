#минава в джъдж 90/100

number_of_cats = int(input())

group1 = 0
group2 = 0
group3 = 0
food_per_day = 0
price_food_per_day = 0

for cats in range(number_of_cats):
    grams_food = float(input())
    if 100 <= grams_food < 200:
        group1 += 1
        food_per_day += grams_food
    elif 200 <= grams_food < 300:
        group2 += 1
        food_per_day += grams_food
    elif 400 >= grams_food:
        group3 += 1
        food_per_day += grams_food

price_food_per_day = food_per_day * 12.45
diff = price_food_per_day / 1000
if price_food_per_day != 0:
   print(f"Group 1: {group1} cats.")
   print(f"Group 2: {group2} cats.")
   print(f"Group 3: {group3} cats.")
   print(f"Price for food per day: {diff:.2f} lv.")