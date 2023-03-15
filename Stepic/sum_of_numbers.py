
# number = int(input("Enter the number of the nums"))
# sum = 0
# while( number > 0):
#     num = int(input("Enter the number"))
#     sum += num
#     number -=1
# print(sum)

# print(42/(4+2*(-2)))

# print(9**19 - int(float(9**19)))

# X = int(input())
# Y = int(input())
# print(X * 60 + Y)


# x = int(input())
# print(x // 60)
# print(x % 60)

# x = int(input())
# h = int(input())
# m = int(input())
# if m + (x % 60) > 60:
#     print(x // 60 + 1 + h)
# else:
#     print(x // 60 + h)
# print((m + x % 60) % 60)

# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)

# a = int(input())
# b = int(input())
# h = int(input())
# if a <= h <= b:
#     print("Это нормально")
# elif h < a:
#     print("Недосып")
# else:
#     print("Пересып")

# a = int(input())
# if a % 400 == 0:
#     print("Високосный")
# elif a % 4 == 0 and not (a % 100 == 0):
#     print("Високосный")
# else:
#     print("Обычный")

# a = int(input())
# b = int(input())
# c = int(input())
# p = (a + b + c)/2
# print((p * (p - a) * (p - b) * (p - c)) ** 0.5)

# a = int(input())
# if -15 < a <= 12 or 14 < a < 17 or a >= 19:
#     print(True)
# else:
#     print(False)

# A = float (input())
# B = float (input())
# C = str (input())
# if C =='+':
#     print(A+B)
# elif C=='-':
#     print(A-B)
# elif C=='*':
#     print(A*B)
# elif C=='/' and B==0:
#     print("Деление на 0!")
# elif C=='/' and B!=0:
#     print(A/B)
# elif C=='mod' and B==0:
#     print('Деление на 0!')
# elif C=='mod' and B!=0:
#     print(A%B)
# elif C=='pow':
#     print(A**B)
# elif C=='div' and B==0:
#     print('Деление на 0!')
# elif C=='div' and B!=0:
#     print(A//B)

# n = int(input())
# if n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or n % 100 == 11 or n % 100 == 12 or n % 100 == 13 or n % 100 == 14:
#     print(str(n) + " программистов")
# elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
#     print(str(n) + " программиста")
# else:
#     print(str(n) + " программист")

# a = int(input())
# b = 'программист'
# if a%10==1 and not a%100==11:
#     print(a, b)
# elif 1<a%10<5 and not 10<a%100<15:
#     print(a, b + 'а')
# else:
#     print(a, b + 'ов')


# n = int(input())
# if (n % 10 == 1 and n%100 != 11):
#     print(n, 'программист')
# elif (n % 10 in [2, 3, 4] and not n % 100 in [12, 13, 14] ):
#     print(n, 'программиста')
# else:
#     print(n, 'программистов')

# ticket = input()
# s1 = 0
# s2 = 0
# for i in ticket[0:3]:
#     s1 += int(i)
# for i in ticket[3:7]:
#     s2 += int(i)
# print("Счастливый" if s1 == s2 else "Обычный")
#
#
# a, b, c, d, e, f = input()
# n= int(a)+int (b)+int(c)
# m= int(d)+int (e)+int(f)
# if n==m:
#     print ('Счастливый')
# else:
#     print ('Обычный')
#
# n=int(input())
# print("Счастливый" if n//100000+n//10000%10+n//1000%10==n//100%10+n//10%10+n%10 else "Обычный")


# num = int(input())
# sum = 0
# while num != 0:
#     sum += num
#     num = int(input())
# print(sum)

# while True:
#     num = int(input())
#     if num > 100:
#         break
#     elif num < 10:
#         continue
#     print(num)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for j in range(c, d + 1):
#     print('\t' + str(j), end="")
# print()
# for i in range(a, b +1):
#     print(i, end="")
#     for k in range(c, d+1):
#         print('\t' + str(i * k), end="")
#     print()

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
#
# print('', *range(c, d+1), sep='\t')
# for i in range(a,b+1):
#     print(i, *range(i*c,(i*d)+1, i), sep='\t')



# Generator expression
# print((x*2 for x in range(256)))

# List comprehension
# print([x*2 for x in range(256)])#save the result to list(return list with result

# a = int(input())
# b = int(input())
# for i in range(a, b):
#     if a % 3 == 0:
#         break
#     else:
#         a += 1
# count, sum = 0, 0
# for i in range(a, b + 1, 3):
#     sum += i
#     count += 1
# print(sum / count)
#
# x = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
# print(sum(x)/len(x))
#
#
# a,b = int(input()), int(input())
# a += -a%3
# b -= b%3
# print((a+b)/2)

# a = input()
# print(((a.upper().count("C") + a.upper().count("G")) / len(a)) * 100)
#
# [print((n.count('c') + n.count('g')) / len(n) * 100) for n in [input().lower()]]