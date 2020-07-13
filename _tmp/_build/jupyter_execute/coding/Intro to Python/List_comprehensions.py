# List comprehensions
``` {index} Lists: list comprehensions
```
List comprehensions are 'shortcuts' in creating lists using loops within one statement. The main advantage is that they are shorter to write. The syntax is:

    some_list = [ expression for item in some_iterable if condition]
    
This will generate a list with an expression based on items in 'some_iterable', if the condition is met. The 'if' condition is optional.

# List comprehensions

normal_numbers = [ number for number in range(1, 20, 3)]
print(normal_numbers)

cubic_numbers = [ number**3 for number in range(1, 20, 3)]
print(cubic_numbers)

# These are equivalent to 

normal_numbers = []
cubic_numbers = []

for number in range(1, 20, 3):
    normal_numbers.append(number)
    cubic_numbers.append(number**3)
    
print(normal_numbers)
print(cubic_numbers)

The expression in list comprehension can be anything, the same value for each item, a string...:

zeros_list = [ 0 for i in range(5)]
text_list = ["text" for i in range(5)]

print(zeros_list)
print(text_list)

Using 'if' condition:

# List comprehension with if statement
# number%2 == 1 means to search for numbers whose 
# remainder from division by 2 is 1 (odd numbers)

odd_numbers = [ number for number in range(20) if number%2 == 1]

print(odd_numbers)

# Equivalent to

odd_numbers = []

for number in range(20):
    if number%2 == 1:
        odd_numbers.append(number)
        
print(odd_numbers)

## Exercise:

Create a list comprehension to find Celsius temperatures for Fahrenheit temperatures between 20$^\circ$F and 80$^\circ$F at 5$^\circ$F increments. The Fahrenheit-Celsius conversion formula is:

$$ T_{Celsius} = \frac{5}{9}*(T_{Fahrenheit}-32) $$

temp_C = [ 5./9.*(i-32) for i in range(20, 81, 5)]

print(temp_C)