#while and for loops
#while loop

x=0
while x<=5:
    print(x)
    x=x+1
    
    
#for loop
for x in range(5,10):
    print(x)
    

#array is a dataset
#array is a collection of data elements of the same data type stored in contiguous memory locations.

days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for d in days:
    if (d=="Fri"):break  #stops or breaks a loop
    if(d=="Fri"):continue #skips the current iteration and moves to the next one
    print(d)