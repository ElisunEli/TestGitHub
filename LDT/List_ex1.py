mylist1 = [12, 35, 9, 56, 24]


def swap_list2(newList):
    newList[0], newList[-1] = newList[-1], newList[0]
    return newList


def swap_list(mylist):
    temp = mylist[0]
    mylist[0] = mylist[-1]
    mylist[-1] = temp
    return


swap_list2(mylist1)
print(swap_list2(mylist1))
swap_list(mylist1)
print(mylist1)

print(max(mylist1), min(mylist1))

mylist2 = [12, 35, -9, 23, -43, 56, 24]


def reorder_list(mylist):
    new_list = []
    for num in mylist:
        if num > 0:
            new_list.insert(0, num)
        else:
            new_list.append(num)
    mylist = new_list
    return mylist


def reverse_list(mylist):
    new_list = []
    for num in mylist:
        new_list.insert(0, num)

    return new_list


print(reorder_list(mylist2))
print(mylist2)
print(reverse_list(mylist2))
mylist2 = reverse_list(mylist2)
print(mylist2[::-1])
