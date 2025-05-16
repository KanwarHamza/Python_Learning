#variables: objects containing specific values

x=5
print(x)

y="we are learning python"
print(y)

x=x+10 #or x=15 as codes run from top to bottom so we can change the values of variables in the middle of the code when required
print(x)

#Types of variables
#1. Integer: whole numbers example : 5, 10, 20 etc.
#2. Float: decimal numbers example : 5.5, 10.2, 20.8 etc.
#3. String: sequence of characters enclosed in quotes example : "hello", 'hello', "we are learning python" etc.
#4. Boolean: True or False example : True, False etc.
#5. List: ordered collection of items enclosed in square brackets example : [1, 2, 3, 4, 5] etc.
#6. Tuple: ordered collection of items enclosed in round brackets example : (1, 2, 3, 4, 5) etc.
#7. Dictionary: unordered collection of items enclosed in curly brackets example : {"name": "John", "age": 25} etc.
#8. Set: unordered collection of items enclosed in curly brackets example : {"apple", "banana", "cherry"} etc.
#9. NoneType: represents the absence of a value example : None etc.
#Variables can be assigned values using the assignment operator (=) and can be printed using the print()
#Variables can be reassigned values using the assignment operator (=) and can be printed using the print

type(x)
print(type(x))
print(type(y))

#Rules to assign a variable
#1. The variable name should start with a letter or underscore
#2. The variable name should not start with a number
#3. The variable name should not contain any special characters except underscore
#4. The variable name should not be a keyword in python which are reserved words in python and cannot be used as variable names. 
# The list includes : and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is
# lambda, not, or, pass, raise, return, try, while, with, yield
#5. The variable name should not be too long, it should be short and meaningful
#6. The variable name should be in lowercase or camelcase or underscore notation example : my_variable, myVariable, my_variable etc.

fruit_basket="Mangoes , Oranges"
print(fruit_basket)
print(type(fruit_basket))
# In this example, the variable name is fruit_basket which is in lowercase notation and is short


x="15"
print(type(x))

x=int(x)
print(type(x))
# In this example, the variable name is x which is in lowercase notation and is short and int (x) is used to convert the string into integer

