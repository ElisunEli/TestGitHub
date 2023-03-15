number = int(input("Please enter a grade"))
if issubclass(number, int):
    if number < 0 or number > 100:
        print("Grade must be between 0-100")

    elif 89 < number:
        print("Excellent")

    elif 79 < number:
        print("Very good")

    elif 69 < number:
        print("Good")

    elif 54 < number:
        print("Passed")

    else:
        print("not passed")
