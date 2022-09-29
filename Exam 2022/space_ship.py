import math

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
astronaut_height = float(input())

ship_volume = ship_width * ship_length * ship_height
room_volume = (astronaut_height + 0.40) * 2 * 2
count_astronauts = ship_volume / room_volume

diff = math.floor(count_astronauts)

if 3 <= count_astronauts <= 10:
    print(f"The spacecraft holds {diff} astronauts.")
elif count_astronauts < 3:
    print(f"The spacecraft is too small.")
elif count_astronauts > 10:
    print(f"The spacecraft is too big.")


