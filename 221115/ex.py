from functools import reduce

# 1
mylist = [1, 'str', 6.88, "fargo", 5, "", "Amadeus"]

mylist2 = (list(filter(lambda x: isinstance(x, str), mylist)))

print(mylist2)

mylist3 = list(filter(lambda x: 'a' in x, mylist2))

print(mylist3)

# 1.1

print(list
      (filter
       (lambda x: 'a' in x, (
           filter(lambda x: isinstance(x, str), mylist)
       ))))

mylist4 = [1, -1, -2, 3, 4, -3, -5, 4]
print(list(filter(lambda x: x >  0, mylist4)))

print(reduce(lambda x, y: x + y, list(filter(lambda x: x < 0, mylist4))))

print(len(list(filter(lambda x: x < 0, mylist4))))

positive_count = len(list(filter(lambda x: x > 0, mylist4)))

print(positive_count)

# Define the grades from Mahat and Magen
grades_mahat = [85, 72, 95, 60, 84, 70, 96, 65, 70, 81]
grades_magen = [85, 75, 95, 60, 80, 70, 90, 65, 75, 85]

# Use map() function with a lambda function to calculate the average of the grades
list_avg = list(map(lambda x, y: (x + y)/2, grades_mahat, grades_magen))

# Print the resulting list
print(list_avg)