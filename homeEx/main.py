number = int(input("Please enter a number"))
mylist = []
if number < 0:
    print("wrong number")
elif number == 1:
    mylist=[0]
elif number == 2:
    mylist = [0, 1]
elif number > 2:
    mylist = [0, 1]
    for i in range(number):
    mylist.append(mylist[len(mylist)-1]+mylist[len(mylist)-2])
print(mylist)
