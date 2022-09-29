name_actor = input()
points_academy = float(input())
count_people = int(input())

total_points = points_academy

for i in range(1, count_people + 1):
    name = input()
    points = float(input())
    current_points = (len(name) * points) / 2
    total_points = total_points + current_points

    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = 1250.5 - total_points
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")