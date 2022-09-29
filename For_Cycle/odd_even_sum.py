n = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    element = int(input())
    if i % 2 == 0:
        even_sum += element
    else:
        odd_sum += element

sum = abs(odd_sum)
difference = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {difference}")


