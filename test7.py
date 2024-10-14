import re
string = input("введите число")

if float(string) > 0:
    print("положительное")
elif float(string) < 0:
    print("отрицательное")
string = input().split(" ")

if int(string[0]) == int(string[0]):
    print("Числа равные", string[0])
else:
    if int(string[0]) > int(string[1]):
        print("2 число: ", int(string[1]))
        print("1 число: ", int(string[0]))
    else:
        print("1 число: ", int)



        








