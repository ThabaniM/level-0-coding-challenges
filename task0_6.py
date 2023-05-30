def max_from_3(*numbers):
    greatest_number = None
    for number in numbers:
        if greatest_number is None or number > greatest_number:
            greatest_number = number

    return greatest_number


if __name__ == "__main__":
    the_greatest_number = max_from_3(2, -3, 5, 4)
    print(f"The maximum is {the_greatest_number}")
