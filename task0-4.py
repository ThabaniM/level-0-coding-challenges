# Write a function named even_or_odd or evenOrOdd. The name of the function 
# depends on the conventions of the language you are writing in. 
# If you don’t know what name to choose then you should check the clean code guidelines.

# Your function should take an integer and print in the word “even” or “odd”.

# eg: if the input is 3 then the output is “odd”. If the input is 4 then the output is “even”
int_number = int(input())
def even_or_odd(int_number):
    
    print('odd') if int_number % 2 == 0 else print('even')

even_or_odd(int_number)