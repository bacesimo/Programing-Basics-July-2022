nylon = int(input())
paint_litters = int(input())
thinner = int(input())
work_hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint_litters * 1.1) * 14.5
thinner_price = thinner * 5

materials_sum = nylon_price + paint_price + thinner_price + 0.40

sum_work_hours = (materials_sum * 0.30) * work_hours
total_price = materials_sum + sum_work_hours
print(total_price)