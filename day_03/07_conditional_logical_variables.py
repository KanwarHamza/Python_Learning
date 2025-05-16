#logical operators are either "true or false" or "yes or no" or "0 or 1"
#equal to ==
#not equal to !=
#greater than >
#less than <
#greater than or equal to >=
#less than or equal to <=
#Logical operators are used to combine conditions in a single statement. They are: and, or, not. For exampl
#and
#or
#not
#Membership operators are used to check if a value is present in a sequence or not. They are: in, not
#in
#not in
#Identity operators are used to check if both variables are the same or not. They are: is, is not
#is
#is not
#Bitwise operators are used to perform operations on the binary representation of the numbers. They are: &, |, ^, ~
#&
#^
#|
#<<
#>>
#**
#//
#%
#//Bitwise NOT operator are used to flip the bits of the number. They are: ~
#~
#//Bitwise AND operator are used to perform AND operation on the binary representation of the numbers. They are: &, &
#&
#//Bitwise OR operator are used to perform OR operation on the binary representation of the numbers. They are: |, |
#//Bitwise XOR operator are used to perform XOR operation on the binary representation of the numbers. They are: ^, ^
#^
#//Bitwise left shift operator are used to shift the bits of the number to the left. They are: <<, <<
#<<
#//Bitwise right shift operator are used to shift the bits of the number to the right. They are: >>, >>
#>>


#is 4 equal to 4
print(4 == 4)  # Output: True
#is 4 not equal to 4
print(4 != 4)  # Output: False

print(4>3) # Output: True
print(4<3) # Output: False
print(4>=3) # Output: True
print(4<=3) # Output: False

#application of logical operators
Hamza_age=4
age_at_school=5
#is Hamza_age equal to age_at_school
print(Hamza_age==age_at_school) # Output: False
#is Hamza_age greater than age_at_school
print(Hamza_age>age_at_school) # Output: False

#input function and logical operator
age_at_school=5
Hamza_age=input("Enter your age: ") #input function
Hamza_age=int(Hamza_age)
print(type(Hamza_age))
print(Hamza_age==age_at_school) #logical operator


#convert input
