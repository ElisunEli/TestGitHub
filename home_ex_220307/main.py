num = int(input("Please enter a number:\n"))

while num < 0 and not isinstance(num, int):
    print("ERROR")
    num = int(input("Please enter a number:\n"))
num_of_digits = 0
sum_of_digits = 0
copy_num = num
#for i in str(num)
    #sum_of += sum_of[i]
#num_of_digits = len(str(num))
#print(num_of_digits)
while copy_num > 0:
    sum_of_digits = sum_of_digits + (copy_num % 10)
    copy_num = copy_num // 10

copy_num = num

while copy_num > 0:
    copy_num = copy_num//10
    num_of_digits += 1
print(num_of_digits, sum_of_digits)

#txt = input("Please enter a number:\n")[::-1]
#print(int(txt))

#for i in str(num)
    #num_over+=str[len(str)-1-i]
mylist = []
copy_num = num
while copy_num > 0:
    if copy_num % 10 != 0:
        mylist.append(copy_num % 10)
    copy_num = copy_num//10
for i in range(len(mylist)):
    print(mylist[i], end="")

str1 = input("Enter string1")
str2 = input("Enter string2")
if len(str1) > len(str2):
    for i in range(len(str2)-1):
        if str2(i) == str1(i):
            print(False)
    else:
        print(True)
if len(str2) > len(str1):
    for i in range(len(str1)-1):
        if str2[i] == str1[i]:
            print(False)
    else:
        print(True)