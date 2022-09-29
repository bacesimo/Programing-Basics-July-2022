# първия вариант

pen_count = int(input())
marker_count = int(input())
detergent_liters = int(input())
discount_percent = int(input())

price_pen = pen_count * 5.80
price_markers = marker_count * 7.20
price_detergent = detergent_liters * 1.20

total_price = price_pen + price_markers + price_detergent
discount = total_price * (discount_percent / 100)
result = total_price - discount

print(result)

# втория вариант


pen_count = int(input())
marker_count = int(input())
detergent_liters = int(input())
discount_percent = int(input())

total_price = (pen_count * 5.80) + (marker_count * 7.20) + (detergent_liters * 1.20)
discount = total_price * (discount_percent / 100)
result = total_price - discount
print(result)

# трети вариант

pen_count = int(input())
marker_count = int(input())
detergent_liters = int(input())
discount_percent = int(input())
total_price = (pen_count * 5.80) + (marker_count * 7.20) + (detergent_liters * 1.20) * (discount_percent / 100)
discount = total_price * (discount_percent / 100)
print(total_price - discount)  # грешно смятане в принт #иначе си работи нема му нищо

# четвърти вариант

pen_count = int(input()) * 5.80  # грешно смятане във входа и па си работи.
marker_count = int(input()) * 7.20
detergent_liters = int(input()) * 1.20
discount_percent = int(input())
total_price = pen_count + marker_count + detergent_liters
discount = total_price * (discount_percent / 100)
print(total_price - discount)  # грешно смятане в принт #иначе си работи нема му нищо.