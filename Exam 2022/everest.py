command = input()
days = 1
height_meters = 1000
start_meters = 0
while command != "END":
    meters_to_hike = int(input())

    if command == "Yes":
        days += 1
        if days > 5:
            print("Failed!")
            print(f"{start_meters}")
            break
        start_meters += meters_to_hike
    else:
        start_meters += meters_to_hike
    if start_meters >= height_meters:
        print(f"Goal reached for {days} days!")
        break

    command = input()

if command == "END":
    if start_meters >= height_meters:
        print(f"Goal reached for {days} days!")
    else:
        print("Failed!")
        print(f"{start_meters}")