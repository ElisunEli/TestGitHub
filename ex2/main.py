number = int(input("Please enter a number"))
if number <= 0:
    print("wrong number:/n")

for i in range(1, number+2, 1):
    print("")
    for y in range(1, i, 1):
        print(y, end="")
print("")
for i in range(1, number+1, 1):
    print("")
    for y in range(i):
        print(i, end="")
print("")
var = number
for i in range(1, number+1, 1):
    print("")
    var = var - 1
    for k in range(var):
        print(" ", end="")
    for y in range(i):
        print(i, end="")
