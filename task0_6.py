def get_maximum(*numbers):
    max = None
    for number in numbers:
        if number is not int:
            raise Exception('All arguments must be integers')
        if max is None or number > max:
            max = number
    
ans = get_maximum(2, 3, 5, 4)

print(f'The maximum is {ans}')