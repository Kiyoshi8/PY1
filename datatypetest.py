# Python VARIABLES

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the type

x = 5
y = "John"
print(type(x))
print(type(y))

#Single or Double Quotes?

#String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

#Case Sensitive
#Variables names are case sensitive

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

#VARIABLES NAME CASE SENSITIVE
#Legal
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Illegal 
"""
2myvar = "John"
my-var = "John"
my var = "John"
"""

#Multi Words Variable Names

#Camel Case
#Each word, except the first, starts with a capital letter:
myVariableName = "Joe"
print(myVariableName)
#Pascal Case
#Each word starts with a capital letter:
MyVariableName = "John"
#Snake Case
#Each word is separated by an underscore character:
my_variable_name = "John"

####################### Python Variables - Assign Multiple Values #################################
#Many Values to Multiple Variables

#Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables

#And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
 
########################### Python - Output Variables ##############################
#OutPut Variable

#The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)

#In the print() function, you output multiple variables, separated by a comma:

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

 #You can also use the + operator to output multiple variables:

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

#For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

x = 5  ###########error#####
y = "John"
print(x + y)

#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

x = 5
y = "John"
print(x, y)

#Global

#Variables that are created outside of a function (as in all of the examples above) are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside.

#Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, 

#and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

#Create a variable inside a function, with the same name as the global variable.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The Global Keyword

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, you can use the global keyword.

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Pyhton is " + x)
 
x = "Hello World" #Text type string
print(x)
print(type(x))

x = 20 #Numeric Type int
print(x)
print(type(x))

x = 20.5 #Numeric Type float
print(x)
print(type(x))

x = 1j #Numeric Type complex
print(x)
print(type(x))

x =  ["apple", "banana", "cherry"] #Sequence type list
print(x)
print(type(x))

x =  ("apple", "banana", "cherry") #Sequence type tuple
print(x)
print(type(x))

x = range (6) # Sequence Type range
print(x)
print(type(x))

x = dict(name="John", age=36) #mapping type dict
print(x)
print(type(x))

x = set(("apple", "banana", "cherry")) #set type set
print(x)
print(type(x))

x = frozenset(("apple", "banana", "cherry")) #set type frozenset
print(x)
print(type(x))

x = bool (5) #boolean type bool
print(x)
print(type(x))

x = bytes (5) #Binary Type memoryview
print(x)
print(type(x))

x = bytearray(5) #Binary Type memoryview
print(x)
print(type(x))

x = memoryview(bytes(5)) #Binary Type memoryview
print(x)
print(type(x))

#Python Numeric Types
#1 int
#2 float
#3 complex

#Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x =  ["apple", "banana", "cherry"]
x = memoryview(bytes(5))
x = bool (5)
x = range (6)
x = 5
print(type(x))