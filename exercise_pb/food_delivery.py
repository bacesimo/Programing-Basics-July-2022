chicken_menu = int(input())
fish_menu = int(input())
vege_menu = int(input())

chicken_price_menu = chicken_menu * 10.35
fish_price_menu = fish_menu * 12.40
vege_price_menu = vege_menu * 8.15

all_menus_price = chicken_price_menu + fish_price_menu + vege_price_menu
dessert = all_menus_price * 0.20
total_sum = all_menus_price + dessert + 2.50
print(total_sum)






