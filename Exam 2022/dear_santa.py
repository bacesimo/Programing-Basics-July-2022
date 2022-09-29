import math

count_days_santa = int(input())
kg_food = int(input())
first_deer_kg_food = float(input())
second_deer_kg_food = float(input())
third_deer_kg_food = float(input())

first_deer = count_days_santa * first_deer_kg_food
second_deer = count_days_santa * second_deer_kg_food
third_deer = count_days_santa * third_deer_kg_food

total_food = first_deer + second_deer + third_deer

if total_food < kg_food:
    left_food = (kg_food - total_food)
    diff = math.floor(left_food)
    print(f"{diff} kilos of food left.")
elif total_food > kg_food:
    needed_food = (total_food - kg_food)
    diff = math.ceil(needed_food)
    print(f"{diff} more kilos of food are needed.")