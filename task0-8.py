number_ok = True

while number_ok:
    number = int(input('Please enter a number greater than or equal zero: '))
    if number < 0:
        print('The number needs to be zero or positive')
        continue
    break

def make_time(number):
    
    time = {
      'hours': 0,
      'minutes': 0
    }
    
    if number > 60:
       time['hours'] = number//60
       time['minutes'] = number % 60
    else:
        time['minutes'] = number
    
    return time

    
ans = make_time(number)

# sort the singular hour and minute problem
hour_text = 'hour' if ans['hours'] == 1 else 'hours'
minute_text = 'minute' if ans['minutes'] == 1 else 'minutes'

print(f'{ans["hours"]} {hour_text}, {ans["minutes"]} {minute_text}')
    
