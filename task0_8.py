def number_to_time_converter(number):
    
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

if __name__ ==  "__main__":
  answer = number_to_time_converter(60)
  print(answer)
    
