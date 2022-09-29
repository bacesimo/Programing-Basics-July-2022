width = int(input())
length = int(input())

total_count_pieces = width * length
no_more_pieces = False
input_line = input()

while input_line != "STOP":
    current_pieces = int(input_line)
    total_count_pieces -= current_pieces
    if total_count_pieces <= 0:
        no_more_pieces = True
        break

    input_line = input()
diff = abs(total_count_pieces)
if no_more_pieces:
    print(f"No more cake left! You need {diff} pieces more.")
else:
    print(f"{diff} pieces are left.")