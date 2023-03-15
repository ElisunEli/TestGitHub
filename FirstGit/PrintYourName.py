#This code print your name number of times

name, number = input("Hello! Please enter your name and number of times you want to print it by space separation").split()
for i in range(int(number)):
    print(name)