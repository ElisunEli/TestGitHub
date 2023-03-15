mylist = [i for i in range(1, 11)]

print(mylist)

mylist2 = [i ** 2 for i in range(1, 11)]

print(mylist2)

# map

mylist3 = []
for i in range(len(mylist)):
    mylist3.append(mylist[i] + 2)

print(mylist3)


def add2(num):
    return num + 2


mylist2 = list(map(add2, mylist3)) #you don't need to write () after the function, because it's pointer to func' Name.

print(mylist2)

def zip_num(num, num2):
    return [num, num2]

mylist4 = list(map(zip_num, mylist, mylist2))

print(mylist4)

mylist4 = list(map(zip_num, mylist, mylist2[1:]))

print(mylist4)

#lambda
#you need write function if want to use many times, but if it is disposable you need to use lambda

mylist5 = list(map(lambda num : num + 2 if num % 2 == 0 else num * 10, mylist2))

print(mylist5)

#filter

def isEven(num):
    return num % 2 == 0

print(list(filter(isEven, mylist)))

print(list(filter(lambda x : x % 3 == 0, mylist)))
