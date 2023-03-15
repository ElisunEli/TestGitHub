mylist = []
mylist.append(10)
mylist +=[4,5,6]
mylist.append(20)#append only one value
print(mylist)

print("")
for item in mylist:
    print(item, ":", type(item))
print("")

secondlist = [7,2,4,8,1]
thirdlist = secondlist.copy()
secondlist.sort()
print(thirdlist)
print(secondlist)
secondlist.pop()
print(secondlist)
print(secondlist[len(secondlist)-1])
print(secondlist[-2])
print(secondlist[3])
print(secondlist[2:4])
print(secondlist[2:-2])