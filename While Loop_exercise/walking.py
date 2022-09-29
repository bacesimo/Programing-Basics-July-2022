input_line = input()

sum_steps = 0
steps_goal = 10000
while input_line != "Going home":
    steps = int(input_line)
    sum_steps += steps

    if sum_steps >= steps_goal:
        break

    input_line = input()

if input_line == "Going home":
    steps_home = int(input())
    sum_steps += steps_home

diff = abs(steps_goal - sum_steps)
if sum_steps >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")

