hour = int(input())
minutes = int(input())
minutes = minutes + 15
if minutes > 59:
    hour = hour + 1
    minutes = minutes - 60
if hour > 23:
    hour = 0
if minutes > 9:
    print(f"{hour}:{minutes}")
else:
    print(f"{hour}:0{minutes}")
