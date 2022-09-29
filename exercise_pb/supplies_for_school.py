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
