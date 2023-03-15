def pyramida(num):
    for i in range(1, num + 1):
        for y in range(i):
            print(i, end="")
        print()


pyramida(5)

def pyramida2(num):
    for i in range(1, num + 1):
        for y in range(1, i+1):
            print(y, end="")
        print()


pyramida2(5)

def pyramida3(num):
    space = num
    for i in range(1, num + 1):
        for k in range(1,space):
            print(" ", end="")
        space = space - 1
        for y in range(i):
            print(i, end="")
        print()

pyramida3(5)


def list_dict(mylist):
    mydict = {}
    for number in mylist:
        if number in mydict:
            mydict[number] = mydict[number] + 1
        else:
            mydict[number] = 1

    return mydict

print(list_dict([10, 20,10, 50, 30,18, 30,100]))


def kefel(num):
    for i in range(1, 11):
        print(str(num) + "*" + str(i) + " = " + str(num * i))


kefel(15)
