#number = int(input("Enter the num"))
#while loop

#while number > 0:
#    if number == 4:
#        number -=1
#       continue

#    print(number, "after break")
#    number -=1
#print("after while")

#for loop
for i in range(10): #[0,1,2,3,4,5,6,7,8,9] run from array
    if i==4:
        i +=100

    print(i)

print(" ")

for i in range(0,10,2):
    print(i)
print(" ")
for i in [0,10,2]:
    #?????
    print(i)
print(" ")
for i in (0,10,2):
    #?????
    print(i)