# def seder_list(mylist):
#     list1 = []
#     list2 = []
#     for i in mylist:
#         if i < 0:
#             list1.append(i)
#         else:
#             list2.append(i)
#     return list2 + list1
#
# mylist = [12,-4,-8,10,13,2]
# print(seder_list(mylist))

def default_parameters1(x=1, y=2, z=3):
    print(x, y, z)


def default_parameters2(x, y=2, z=3):
    print(x, y, z)


# def defaultParameters3(x=1, y=3, z):
#     print(x, y, z)


# defaultParameters1()			#1
# defaultParameters1(10)			#2
# defaultParameters1(10, 20)		#3
# defaultParameters1(10, 20, 30)	#4

# defaultParameters2()			#5
# defaultParameters2(10)			#6
# defaultParameters2(10, 20)		#7
# defaultParameters2(10, 20, 30)	#8
#
# defaultParameters3()			#9
# defaultParameters3(10)			#10
# defaultParameters3(10, 20) 		#11
# defaultParameters3(10, 20, 30)	#12

def magic(num):
    numbers = [i for i in range(2, num)]
    i = 0
    while i < len(numbers):

        currentNumber = numbers[i]
        if num % currentNumber != 0:
            for value in numbers[i:]:
                if value % currentNumber == 0:
                    numbers.remove(value)
        else:
            i += 1

    return numbers

print(magic(15))
