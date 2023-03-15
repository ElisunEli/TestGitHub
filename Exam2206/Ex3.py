file = open("D:\\Users\\ELI\\PycharmProjects\\Exam2206\\Loren Ipsun.txt", "r", encoding="utf8")

##############
# txt = {}
# line = file.read().lower()
# print(line)
# for i in line:
#     if i.isalpha():
#         if i in txt:
#             txt[i] += 1
#         else:
#             txt[i] = 1
# print(txt)

#######################
txt = []
for line in file.readlines():
    txt.extend(line)
print(line)
print(txt)

# print(txt)
# for i in range(len(txt) - 1):
#     if txt[i] == ' ' or '\n' or ',':
#         print(txt.pop(i))
#         # split_line.remove(i)
# print(txt)
# print(txt)
freq = {}
for item in txt:
    if item.isalpha():
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
print(freq)
