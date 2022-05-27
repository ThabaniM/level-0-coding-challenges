def get_maximum(*numbers):
    max = None
    for number in numbers:
        if max is None or number > max:
            max = number

    return max
    
ans = get_maximum(2, -3, 5, 4)

print(f'The maximum is {ans}')