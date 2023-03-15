def avg_num():
    num = int(input("Please, enter a positive number: "))
    while num < 1:
        print("Error")
        num = int(input("Please, enter a positive number: "))
    mylist = input("Please enter " + str(num) + " numbers by space : ").split(" ")
    print(mylist)
    count = 0
    for number in mylist:
        count += int(number)
    print(count / len(mylist))


# avg_num()


def rev_num():
    print(str(abs(int(input("Please enter a number: "))))[::-1])


# rev_num()


def perfect_num(num):
    mylist = []
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            mylist.append(i)
    if sum(mylist) == num:
        print("YES")
    else:
        print("NO")


perfect_num(6)
perfect_num(11)
perfect_num(33550336)
perfect_num(496)

def abot_nums():
    num = int(input("Please enter numbers (0 to stop): "))
    mymax = num
    mymin = num
    mysum = num
    count = 1
    while True:
        num = int(input("Please enter numbers (0 to stop): "))
        if num == 0:
            break
        if num > mymax:
            mymax = num
        if num < mymin:
            mymin = num
        mysum += num
        count += 1
    print(" Max number : " + str(mymax) + "\n" + "  Min number : " + str(mymin) + "\n" + " Avg : " + str(mysum / count))


# abot_nums()


def amstrong_num(num):
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i]) ** 3
    return num == sum


# print(amstrong_num(153))
# print(amstrong_num(187))


# def polindrom(str):
#     if len(str) == 1 or 0:
#         return True
#     if str[0] == str[-1] and len(str) > 2:
#         polindrom(str[1:-1])
#     else:
#         return False
#
#
# print(polindrom("abba"))
# # print(polindrom("abkjhhlba"))



