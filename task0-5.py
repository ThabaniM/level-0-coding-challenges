# Write a function that takes in three numbers. 
# These numbers represent the lengths of the sides of a triangle. 
# The function should return the area of a triangle.

# This might help: https://www.wikihow.com/Calculate-the-Area-of-a-Triangle

# handle incorrect input and ask user for input again

try:
   base = int(input('Please Enter the Value of Base: '))
   height = int(input('Please Enter the Value of Height: '))        
except:
    print('Please Enter a Positive Integer greater than zero')  
else: 
    if base <= 0 or height <= 0:
        raise Exception('Sorry both values must be integers greater than zero')


def area_of_triangle(base, height):

    area = 0.5 * base * height
    return area

ans = area_of_triangle(base, height)

print('The area is equal to', ans, 'units squared')