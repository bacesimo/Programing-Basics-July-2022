price_for_one_page = float(input())
price_for_cover = float(input())
discount_percent = int(input())
designer_sum = float(input())
percent_all_sum = int(input())

book_pages = 899
book_cover = 2

sum_for_print = price_for_one_page * book_pages + price_for_cover * book_cover
with_discount = sum_for_print - (sum_for_print * discount_percent / 100)
designer = with_discount + designer_sum
total_sum = designer - (designer * percent_all_sum / 100)

print(f"Avtonom should pay {total_sum:.2f} BGN.")
