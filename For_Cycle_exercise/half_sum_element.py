import sys
n = int(input())

sum_numbers = 0
max_num = -sys.maxsize

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num

    sum_numbers += num
if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {sum_numbers // 2}")
else:
    print("No")
    sum_numbers = sum_numbers - max_num
    print(f"Diff = {abs(max_num - sum_numbers)}")
