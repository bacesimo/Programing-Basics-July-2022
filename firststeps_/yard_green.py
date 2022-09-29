square_meters = float(input())
one_square_meter = 7.61
discount_percent = 0.18
final_price = square_meters * one_square_meter
discount = final_price * discount_percent
final_price_with_discount = final_price - discount
print(f"The final price is: {final_price_with_discount} lv.")
print(f"The discount is: {discount} lv.")