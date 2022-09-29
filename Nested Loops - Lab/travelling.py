destination = input()

while destination != "End":
    needed_money = float(input())
    money_i_have = 0
    while money_i_have < needed_money:
        current_money = float(input())
        money_i_have += current_money
    print(f"Going to {destination}!")

    destination = input()



