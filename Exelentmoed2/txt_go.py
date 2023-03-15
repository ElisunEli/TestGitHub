file = open("D:\\Univer\\Second year\\Dvora\\PYTHON\\work with files\\תרגיל CSV 1\913108.csv", "r", encoding="utf8")
# print(file.read())

# lines = file.readlines()
# print(lines)

authors = []  # List()
authors_count = {}  # dict()

author_index = file.readline().split(",").index("authors")
print(author_index)
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

for author in authors:
    if author in authors_count:
        authors_count[author] = authors_count[author] + 1
    else:
        authors_count[author] = 1

max = 0
for author in authors_count:
    if authors_count[author] > max:
        max = authors_count[author]

print(max)
print(authors_count)
maxautor = authors_count[max]
print(maxautor)
