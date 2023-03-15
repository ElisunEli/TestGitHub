while True:
    my_list = list()

    num = int(input("Please enter a number:\n"))
    while num < 0:
        print("ERROR")
        num = int(input("Please enter a number:\n"))

    if num >= 1:
        my_list.append(0)

    if num >= 2:
        my_list.append(1)

    for i in range(2, num):
        my_list.append(my_list[-1] + my_list[-2])

    print(my_list)
