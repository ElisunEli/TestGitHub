file = open("text.csv", "r", encoding="utf8")

# print(file.read())
# file.seek(0)

lines = file.readlines()
oldest_book = 0
oldest_book_name = ""
oldest_book_set = False
for line in lines:
    print(line)
    temp = line.split(",")[8][0:4]
    #print(temp)
    if temp.isnumeric():
        if not oldest_book_set:
             oldest_book = temp
             oldest_book_set = True
             oldest_book_name = line.split(",")[9]
        else:
            if temp < oldest_book:
                 oldest_book = temp
                 oldest_book_name = line.split(",")[9]

print(oldest_book)
print(oldest_book_name)

authors = []  # List()
authors_count = {}  # dict()
file.seek(0)
author_index = file.readline().split(",").index("authors")

for line in file.readlines():
    split_line = line.split(',')
    # print(split_line)
    author = split_line[author_index]
    print(author)

    if author.startswith('\"'):
        author = author.replace('\"', "")

        current = author_index + 1

        while not split_line[current].endswith("\""):
            authors.append(author.strip())
            author = split_line[current]
            current += 1
        else:
            author = author.replace('\"', "")

    authors.append(author.strip())

print(authors_count)
print(authors)


def most_frequent(List):
    return max(set(List), key=List.count)


print(most_frequent(authors))

# author = ""
# for line in lines[1:]:
#
#
#     author = author +" " + line.split(",")[7]
#     print(author)
