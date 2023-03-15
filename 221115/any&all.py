from functools import reduce

mylist = [i for i in range(1, 14)]
print(mylist)


boolMyList = list(map(lambda x : x < 50, mylist))

print(boolMyList)
print(all(boolMyList))
boolMyList = list(map(lambda x : x % 2 == 0, mylist))
print(boolMyList)
print(any(boolMyList))

#reduce
print( reduce(lambda x, y : x * y, mylist))
