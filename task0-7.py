try:
   celsius = int(input('Please Enter the Temperature in Celsius: '))
   farenheit = int(input('Please Enter the Temperature in Farenheit: '))        
except:
    print('One or both input values were incorrect. Please make sure BOTH Values are integers')  

def to_celsius(farenheit):

    celsius = (farenheit - 32) * (5/9)
    return celsius


def to_farenheit(celsius):

    return (celsius * (9/5)) + 32


print(f"""{farenheit}°F is equal to {to_celsius(farenheit)}°C
While {celsius}°C is equal to {to_farenheit(celsius)}°F
""") 