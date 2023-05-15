def max_from_3(*numbers):
    max = None
    for number in numbers:
        if max is None or number > max:
            max = number

    return max


ans = max_from_3(2, -3, 5, 4)

print(f"The maximum is {ans}")

if __name__ == "__main__":
    ans = max_from_3(2, -3, 5, 4)
    print(f"The maximum is {ans}")
