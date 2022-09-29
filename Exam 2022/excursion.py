count_people = int(input())
count_nights = int(input())
count_transport_cards = int(input())
count_museum_tickets = int(input())

price_for_one_person = count_nights * 20
price_for_transport = count_transport_cards * 1.60
price_for_tickets = count_museum_tickets * 6

total_sum_for_one_person = price_for_one_person + price_for_transport + price_for_tickets
total_sum_group = total_sum_for_one_person * count_people
diff = total_sum_group + (total_sum_group * 0.25)

print(f"{diff:.2f}")