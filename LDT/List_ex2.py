test_list = [1, 4, 5, 7, 8]

# Printing test_list
print("The list is : " + str(test_list))

# Finding length of list
# using loop
# Initializing counter
counter = 0
for i in test_list:
    # incrementing counter
    counter += 1

# Printing length of list
print("Length of list using naive method is : " + str(counter))


def length_of_list(mylist):
    counter = 0
    for i in mylist:
        counter += 1
    return counter


print(length_of_list(test_list))


# Swaping position of elements in the  list
def enter_swap():
    counter = int(input("Please enter how much nums you want to put at List"))
    numList = []
    position = counter
    for i in range(counter):
        numList.append(input("Please enter you num. Left " + str(position) + " positions"))
    print(numList)
    one, two = int(input("Which position you want to change?")), int(input())
    numList[one], numList[two] = numList[two], numList[one]
    print(numList)


lst = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(lst)
lst2 = [x ** 2 for x in range(1, 11, 2)]
print(lst2)