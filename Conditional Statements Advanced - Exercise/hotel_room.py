month = input()
spending_the_night = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if spending_the_night > 14:
        studio_price = studio_price * 0.70
    if 14 > spending_the_night > 7:
        studio_price = studio_price * 0.95
    if spending_the_night > 14:
        apartment_price = apartment_price * 0.90

if month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if spending_the_night > 14:
        studio_price = studio_price * 0.80
    if spending_the_night > 14:
        apartment_price = apartment_price * 0.90

if month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if spending_the_night > 14:
        apartment_price = apartment_price * 0.90

apartment_total = spending_the_night * apartment_price
studio_total = spending_the_night * studio_price

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
