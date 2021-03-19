choice = input("which one?\nChoose D E or F >> D")
if (choice == "D"):
    counter = 9
    for x in range(0, 3):
        for y in range(0, 3):
            print(str(counter),end=" ")
            counter = counter - 1
        print()
if (choice == "E"):
    counter = 0
    for x in range(0, 5):
        for y in range(x, 5):
            print(str(counter),end=" ")
            counter = counter + 1
        counter = 0
        print()