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

    
ans = make_time(90)


hour_text = 'hour' if ans['hours'] == 1 else 'hours'
minute_text = 'minute' if ans['minutes'] == 1 else 'minutes'

print(f'{ans["hours"]} {hour_text}, {ans["minutes"]} {minute_text}')
    
