import math

breed_cat = input()
gender_cat = input()

years_old = 0

if breed_cat == "British Shorthair":
    if gender_cat == "m":
        years_old = 13
    if gender_cat == "f":
        years_old = 14

elif breed_cat == "Siamese":
    if gender_cat == "m":
        years_old = 15
    if gender_cat == "f":
        years_old = 16

elif breed_cat == "Persian":
    if gender_cat == "m":
        years_old = 14
    if gender_cat == "f":
        years_old = 15

elif breed_cat == "Ragdoll":
    if gender_cat == "m":
        years_old = 16
    if gender_cat == "f":
        years_old = 17

elif breed_cat == "American Shorthair":
    if gender_cat == "m":
        years_old = 12
    if gender_cat == "f":
        years_old = 13

elif breed_cat == "Siberian":
    if gender_cat == "m":
        years_old = 11
    if gender_cat == "f":
        years_old = 12

else:
    print(f"{breed_cat} is invalid cat!")


human_months = years_old * 12
cat_months = human_months / 6
diff = math.floor(cat_months)

if diff > 0:
    print(f"{diff} cat months")

