year_price_tax = int(input())

basketball_sneakers = year_price_tax - (year_price_tax * 0.40)
basketball_team = basketball_sneakers - (basketball_sneakers * 0.20)
basketball_ball = 1/4 * basketball_team
basketball_accessories = 1/5 * basketball_ball

total_price = year_price_tax + basketball_sneakers + basketball_team + basketball_ball + basketball_accessories
print(total_price)
