names = dict()
names["Masha"] = 25
names["Sasha"] = 22
numbers = [1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 4, 5, 6]
print(names)
print(names["Masha"])
names["Masha"] = 11
print(names["Masha"])

for key, value in names.items():
    print(key, value)

for key, value in names.items():
    print(key)

for key in names:
    print(key)

numbers2 = ["first", 1, 2, 3, "second", 1, 1, 2, 3, 4, "third", 5, 6, 4, 5, 6]
d = {}
current_str = ""
for item in numbers2:
    if type(item) == str:
        d[item] = []
        current_str = item
    else:
       # d[current_str] += [item]
       d[current_str].append(item)

print(d)

my_text = "kaka davai kaka gde kaka u tebe u mene ne kogo ura davai"
# my_list = my_text.split()
my_dict = {}
for word in my_text.split():
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

print(my_dict)


for word in my_text.split():
    my_dict[word] = my_dict.get(word, 0) + 1

print(my_dict)
