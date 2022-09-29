import math
name_serial = input()
episode_duration = int(input())
break_time = int(input())

lunch_break = break_time / 8
relax_time = break_time / 4

my_time = break_time - lunch_break - relax_time

diff = abs(episode_duration - my_time)
if my_time >= episode_duration:
    print(f"You have enough time to watch {name_serial} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_serial}, you need {math.ceil(diff)} more minutes.")