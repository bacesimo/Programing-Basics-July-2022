length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
liters = volume / 1000
total_liters = liters * (percent / 100)
total_lt = liters - total_liters
print(total_lt)

