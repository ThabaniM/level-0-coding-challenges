def make_time(number):
    
    time = {
      'hours': 0,
      'minutes': 0
    }
    
    if number >= 60:
       time['hours'] = number//60
       time['minutes'] = number % 60
    else:
        time['minutes'] = number

    hour_text = 'hour' if time['hours'] == 1 else 'hours'
    minute_text = 'minute' if time['minutes'] == 1 else 'minutes'

    return f'{time["hours"]} {hour_text}, {time["minutes"]} {minute_text}'
          
answer = make_time(60)

print(answer)
    
