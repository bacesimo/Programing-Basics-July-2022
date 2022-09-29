number = int(input())
for current_number in range(0, 9 + 1):
    number_special = True
    current_number_as_string = str(current_number)
    for current_digit in current_number_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_special = False
            break
    if number_special:
        print(current_number_as_string, end = ' ')
