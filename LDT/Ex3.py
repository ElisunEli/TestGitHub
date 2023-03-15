# Python program to find second-largest number in a list

lst = [2, 3, 44, 33, 22, -1, -22, 77]


def biggestNum(mylist):
    big = mylist[0]
    for i in mylist:
        if i > big:
            big = i
    return big


def secondBig(mylist):
    mylist.remove(biggestNum(mylist))
    return biggestNum(mylist)


def secondBig2(mylist):
    # Removing duplicates from the list
    list2 = list(set(mylist))
    # Sorting the  list
    list2.sort()
    # Printing the second last element
    print("The second largest element is:", list2[-2])


secondBig2(lst)

list2 = list(lst)
list3 = lst
list2.remove(44)
print(lst)
list3.remove(44)
print(list2)
print(list3)
print(lst)

a = [1]
b = a
a += [1]
a = a + [1]

a.append(4)
print(a)
print(b)
