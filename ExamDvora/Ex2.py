a = ['banana', 'apple', 'melon', 'ananas', 'strawberry', 'kiwi']
print(a[-5:-3])
print(a[-5:])
print(a[-6])
print(a[4::2])


def magic(num):
    numbers = [i for i in range(2, num)]
    i = 0
    while i < len(numbers):
        currentNumber = numbers[i]
        if num % currentNumber != 0:
            for value in numbers[i:]:
                if value % currentNumber == 0:
                    numbers.remove(value)
        else:
            i += 1
    return numbers
print(magic(27))
print(magic(24))
print(magic(12))
print(magic(10))
print(magic(9))