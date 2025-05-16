# print("I am learning python")
# print("I am learning python")
# print("I am learning python")
# print("I am learning python")
# print("I am learning python")
# print("I am learning python")
# print("I am learning python")
# print("I am learning python")
# print("I am learning python")

# #defining a function
# def print_rocky():
#     print("I am learning python")
#     print("I am learning python")
#     print("I am learning python")
#     print("I am learning python")
    
# print_rocky()

# #second method
# def print_rocky():
#     text="I am learning python"
#     print(text)
#     print(text)
#     print(text)

# print_rocky()

#third method
# def print_rocky(text):
#     print(text)
#     print(text)
#     print(text)
    
# print_rocky("I am learning python")

#defining a function with if,else and elif
def school_calculator(age, text):
    if age == 5:
        print("Hamza can join school")
    elif age>5:
        print("Hamza should join higher school")
    else:
        print("Hamza is too young to join school")
        
school_calculator(5, "Hamza")  #Hamza can join school
school_calculator(6, "Hamza")  #Hamza should join higher school
school_calculator(4, "Hamza")  #Hamza is too young to join school

#if only looking at the age

def school_calculator(age):
    if age == 5:
        print("Hamza can join school")
    elif age>5:
        print("Hamza should join higher school")
    else:
        print("Hamza is too young to join school")
school_calculator(5)  #Hamza can join school
school_calculator(6)  #Hamza should join higher school
school_calculator(4)  #Hamza is too young to join school


#defining a future function
def future_age(age):
    new_age=age+20
    return new_age

future_predicted_age=future_age(18)
print(future_predicted_age)  #38