budget = float(input())
number_video_cards = int(input())
number_cpu = int(input())
number_ram = int(input())

price_video_card = number_video_cards * 250
price_cpu = price_video_card * 0.35
sum_cpu = price_cpu * number_cpu
price_ram = price_video_card * 0.10
sum_ram = price_ram * number_ram


sum_price = price_video_card + sum_cpu + sum_ram
if number_video_cards > number_cpu:
    sum_price = sum_price - (sum_price * 0.15)

total_sum = abs(sum_price - budget)

if budget >= sum_price:
    print(f"You have {total_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_sum:.2f} leva more!")



