def sorted_list(mylist):
    pluslist = []
    minuslist = []
    for numbers in mylist:
        if numbers > -1:
            pluslist.append(numbers)
        else:
            minuslist.append(numbers)
    pluslist = pluslist + minuslist
    return pluslist


print(sorted_list([12,-4,-8,10,13,2]))

def sorted_list2(mylist):
    goodlist = []
    for numbers in mylist:
        if numbers > -1:
            goodlist.insert(0, numbers)
        else:
            goodlist.append(numbers)
    return goodlist


print(sorted_list2([12,-4,-8,10,13,2]))