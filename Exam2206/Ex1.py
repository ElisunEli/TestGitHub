import math


def num_pyramid(num):
    num += 1
    s = ""
    for i in range(1, num):
        s += str(i)
        print(s)


num_pyramid(6)
print("###########################")


def num_pyramid2(num):
    num += 1
    for i in range(1, num):
        s = ""
        for y in range(i):
            s += str(i)
        print(s)


num_pyramid2(5)
print("###########################")


def num_pyramid3(num):
    space = num - 1
    num += 1
    for i in range(1, num):
        s = ""
        for y in range(space):
            s += " "
        for k in range(i):
            s += str(i)
        space -= 1
        print(s)


num_pyramid3(5)
print("###########################")


def list_to_dict(my_list):
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


gg = [1, 1, 1, 2, 44, 4444, 4, 3, 4]
hh = list_to_dict(gg)
print(hh)
print("###########################")


def first_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return True
    return False


print(first_number(3))
print(first_number(13))
print(first_number(9))
print(first_number(10))
print("###########################")


def multiplication_num():
    num = int(input("Please enter the number, that you wana now his basic multiplication table"))
    for i in range(1, 11):
        result = num * i
        print(str(num) + " * " + str(i) + " = " + str(result))


multiplication_num()
