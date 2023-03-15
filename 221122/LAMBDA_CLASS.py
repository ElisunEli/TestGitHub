grades = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted_grades_asc = sorted(grades, key=lambda x: x[1])
print(sorted_grades_asc)