def max_from_3(*numbers):
    maximum_number = 0
    for number in numbers:
        if not maximum_number or number > maximum_number:
            maximum_number = number

    return maximum_number


if __name__ == "__main__":
    the_maximum_number = max_from_3(2, -3, 5, 4)
    print(f"The maximum is {the_maximum_number}")
