# Write a program that asks the user for a number of days. The program then prints out the number of seconds in the number of days given.

num_days = float(input("Enter number of days: ")) # This asks the user to input the number of days

sum_seconds = num_days*24*60*60 # To calculate the total number of seconds in the given number of days

print("There are", sum_seconds, "seconds in", num_days, "days.") 



# Program that asks a user to input the radius then the program calculates the volume of a sphere 
r= float(input("Enter the radius of the sphere: ")) # Asks for the input (float) from the user
PI = 3.142 # Uppercase to show it is constant
volume = r ** 2 * 4/3 * PI # using the exponential operator ( r ** 2) for r^3
print("The volume of the sphere is:", volume)



# Program to calculate the perimeter and area of a square
# Function to calculate perimeter
def calculate_perimeter(length):
    return length * 4
# Function to calculate area
def calculate_area(length):
    return length * length
    
length = float(input("Enter the length of the square:"))
# To call the functions
perimeter = calculate_perimeter(length) 
area = calculate_area(length)
# To print the outputs
print(" The perimeter of the square is:", perimeter)
print(" The area of the square is:", area)
 


# program using functions that determines whether a character input by a user is uppercase or lower case
def det_char(ch): # function to determine the character's nature (Upper or Lower)
    if ch>="A" and ch<="Z":
        print(ch, "is an Uppercase Letter")
    elif ch>="a" and ch<="z":
         print(ch, "is a Lowercase Letter")
    else:
        print(ch, "is not an Alphabet Letter") # If the character entered is either a digit or symbol
    

ch = input(" Enter a Alphabetic Character") # To take input given by the user 
det_char(ch)  # Calls the function


   
# Program to compute variable x 
x=0
y=20
while y>=6:  # while y is greater  than 6 is true, must not be less than 6
     y=y-4
     x=x+2/y
print (x)  
x
1.0416666666666665
x=0
y=20
# Alternatively:
while True:  # While these conditions are true
    y = y - 4
    if y == 0: # If y is 0
        print("Mathematical Error")
        break # Stops the loop
    x = x + 2 / y
    if y < 6:
        break # Ends the loop

print(x)



# Program to loop for a user to continually input 5 values to populate an array
lst = [] # Starts when the array is empty
values = 5
for i in range (values): #  values from the user 
    lst.append(float(input(" Enter a Value ")) )# adds the value to the list (lst), can be a float
print(lst)

average = sum(lst)/values # Sums the values in the list then divides it by the numbe rof values

print(" The average is:", average)

 
