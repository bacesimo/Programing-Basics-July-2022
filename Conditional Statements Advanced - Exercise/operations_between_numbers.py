num_1 = int(input())
num_2 = int(input())
operator = input()

result = 0

if operator == "+":
    result = num_1 + num_2
    if result % 2 == 0:
        print(f"{num_1} + {num_2} = {result} - even ")
    else:
        print(f"{num_1}  + {num_2} = {result} - odd")
elif operator == "-":
    result = num_1 - num_2
    if result % 2 == 0:
        print(f"{num_1} - {num_2} = {result} - even ")
    else:
        print(f"{num_1} - {num_2} = {result} - odd")
elif operator == "*":
    result = num_1 * num_2
    if result % 2 == 0:
        print(f"{num_1} * {num_2} = {result} - even ")
    else:
        print(f"{num_1} * {num_2} = {result} - odd")

elif operator == "/" and num_2 != 0:
    result = num_1 / num_2
    print(f"{num_1} / {num_2} = {result:.2f}")

elif operator == "%" and num_2 != 0:
    result = num_1 % num_2
    print(f"{num_1} % {num_2} = {result}")

if num_2 == 0 and (operator == "/" or operator == "%"):
    print(f"Cannot divide {num_1} by zero")