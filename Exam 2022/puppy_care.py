class StacksAndQueues:
    def main(args):
        kilos = int(input())
        ate = 0
        command = input()
        while (not command == "Adopted"):
            gr = int(command)
            ate += gr
            command = input()
        if (ate <= kilos * 1000):
            diff = kilos * 1000 - ate
            print("Food is enough! Leftovers: " + str(diff) + " grams.")
        else:
            diff = ate - (kilos * 1000)
            print("Food is not enough. You need %d grams more." % (diff), end="", sep="")


if __name__ == "__main__":
    StacksAndQueues.main([])