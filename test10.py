while True:
    chislo = int(input())
    if chislo == 7:
        print("Goodbye")
        break

string = input().split(" ")
numbers = []
start_time = datetime.today()
for i in range(int(string[0]), int(string[1])):
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        if count > 2:
            break
        j += 1
    if count == 2:
        numbers.append(i)

end_time = datetime.today()

print("простые числа: ",numbers)




