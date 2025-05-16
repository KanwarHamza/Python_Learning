x=10 #type integer
y=10.2 #type float
z="Hello" #type string

print(type(x))
print(type(y))
print(type(z))

#implicit type conversion
x= x*y
print(x, "Type of x is:", type(x)) 


#explicit type conversion
age=input("What is your age? ")
# age=int(age)
print(age, type(float(age)))

name=input("What is your name? ")
# age=str(name)
print(name, type(str(name))) #python dont know what to ask you have to tell python what to ask and in which exact format you want the answer to be in.  #python is very strict about this.  #



