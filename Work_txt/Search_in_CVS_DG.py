file = open("text.csv", "r", encoding="utf8")
authors = []
authors_count = {}
author_index = file.readline().split(",").index("authors")

for line in file.readlines():

    split_line = line.split(',')
    author = split_line[author_index]

    if author.startswith('\"'):
        author = author.replace('\"', "")
        current = author_index
        while not split_line[current].endswith('\"'):
            authors.append(author.strip())
            current += 1
            author = split_line[current]

        else:
            author = author.replace('\"',"")
    authors.append(author.strip())


for author in authors:
    if author in authors_count.keys():
        authors_count[author] += 1
    else:
        authors_count[author] = 1
authorCounter = 0
for author in authors:
    if authors_count[author] > authorCounter:
        authorCounter = authors_count[author]
        maxAuthor = author
print("##################")
print(authors)
print("Max Author is ",maxAuthor, "with ", authorCounter, " books!!!")
print("Total authors count is: ", len(authors))
print("##################")

file.seek(0)
first_line_parts = file.readline().split(",")

year_index = first_line_parts.index("original_publication_year")
title_index = first_line_parts.index("original_title")

min_year, min_title = 2023 , ""

for line in file.readlines():
    split_line = line.split(',')

    year_index2, title_index2 = year_index , title_index
    current = author_index

    if split_line[author_index].startswith('\"'):
        while not split_line[current].endswith("\""):
            current += 1
        else:
            current += 1
            year_index2 = current
            title_index2 = year_index2+1

    year = int(float(split_line[year_index2]))
    if year < min_year:
        min_year = year
        min_title = split_line[title_index2]

print("The oldest book :",min_year,min_title)