def check(num):
    return check_help(num, True)


def check_help(num, acc):
    if num == 0 or not acc:
        return acc
    return check_help(num / 10, (num % 10 >= num / 10 % 10))


print(check(123456))
print(check(123436))

my_list = [1, 2, 3, 2, 3, 4, 5, 5]


def check_mlist(my_list):
    return check_mlist_help(my_list, 0)


def check_mlist_help(my_list, acc):
    if my_list == []:
        return acc
    return check_mlist_help(my_list[1:], acc + 1)

def big_num(my_list):
    return big_num_help(my_list[1:], my_list[0])


def big_num_help(my_list, acc):
    if my_list == []:
        return acc
    if acc < my_list[0]:
        acc = my_list[0]
    return big_num_help(my_list[1:], acc)


print(check_mlist(my_list))
print(big_num(my_list))



