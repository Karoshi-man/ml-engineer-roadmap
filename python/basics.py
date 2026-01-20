# basic syntax

# Python is a dynamically typed language

# It ruled by Indentation (1 tab - 4 spaces)

    # Scope Definition - it is like {} in C
        # if a line has a larger indent than the previous one, 
        # it is “nested” within the previous block.

    # The Golden Rule of 4 Spaces
        # PEP8 requires 4 spaces for tabulation

    # The Colon Connection
        # Indentation always follows a line ending with a colon `:`

    # IndentationError
        # This is a type of error that occurs even before the program starts 
        # (at the parsing stage) if the indents are placed randomly.



# Comments

"""
Comments are lines of code that the Python interpreter completely ignores. 
They exist solely for humans (you, your colleagues, or yourself in two weeks) 
to explain logic, “preserve” part of the code, or create documentation.
"""

# Single-Line Comments
    # they begin with the hash symbol (#) 
    # everything written after this symbol on the same line is not executed

    # Inline: written to the right of the code. 
        # Use with caution so as not to clutter the code.

    # Block: written above the code they explain.

# This is a separate comment explaining the block below.
x = 5  # And this is an inline comment

# Docstrings
    # this is a special type of comment
    # they are enclosed in triple quotes """...""" or '''...'''

    # unlike regular comments, Docstrings are tied to objects 
    # (functions, classes, modules) 
    # and become part of their meta-information.

    # they can be read programmatically via the .__doc__ attribute or 
    # by calling the help() function 
    # this is the standard for creating professional code documentation

def calculate_tax(income):
    """
    Calculates income tax.
    Accepts: income (int)
    Returns: tax (float)
    """
    pass

# Commenting Out fot debugging
    # you place # before the working code 
    # to temporarily disable its execution without deleting it.

# print("This line will not work now")
print("And this one will work")

# The "Why", Not "What"
    # the comment should explain the reason for the decision or a complex algorithm

    # Bad: 

x = x + 1 # Increase x by 1 (This is obvious)

    # Good: 

x = x + 1 # compensate for the index offset, 
          # because the API counts from 1 (Explains the business logic)



# Input/Output
    # these are mechanisms that transform a script from a “black box” into an interactive program 
    # the basic syntax refers to interaction with a text console (terminal)

# Standard Output
    # the print() function is your primary tool for displaying information.

print("Data", "Science")              # Data Science
print("Data", "Science", sep="-")     # Data-Science
print("Loading", end="...")           # Loading... (without starting a new line)
print("Done")                         # Add “Done” to the same line

# User Input
    # the input() function allows you to pause the program and wait 
    # until the user types something and presses Enter

    # The String Trap: the most important rule is that input() always returns a string (str)

age = input("Скільки вам років? ") # Enter: 25
# now age = “25” (string)

# year = 2024 - age  # ERROR! You cannot subtract a string from a number.

real_age = int(age)  # Converting into int
year = 2024 - real_age # now all is working

# String Formatting
    # in modern Python (3.6+), f-strings (formatted string literals) are the standard
    # this is a way to insert variable values into text without using cumbersome plus signs
    
    # place f before the quotation marks, 
    # in {}, you can write not only variables, but also simple expressions or method calls

name = "Alex"
score = 95.5

# The old (bad) way:
print("User " + name + " got " + str(score) + " points") 

# Modern (f-string) way:
print(f"User {name} got {score} points")

# Even that way:
print(f"Double score is {score * 2}")



# Operators

"""
| Operator Type       | Symbols                | Example / Explanation                  |
|---------------------|------------------------|----------------------------------------|
| Arithmetic          | +, -, *, /             | a + b                                  |
| Exponentiation      | **                     | 2 ** 3 (results in 8)                  |
| Floor Division      | //                     | 10 // 3 (results in 3)                 |
| Modulo / Remainder  | %                      | 10 % 3 (results in 1)                  |
| Comparison          | ==, !=, >, <, >=, <=   | 5 > 3 (True)                           |
| Logical             | and, or, not           | True and False                         |
| Assignment          | =, +=, -=, *=          | x += 1 (same as x = x + 1)             |
"""



# Variables

score = 100 # score is a variable (var) with value 100
    # Operator = is “assign” operator
    # Logic: First, an object is created on the right, 
        # and then it is given a name on the left.

# Naming Rules
    # may contain letters (a-z, A-Z), numbers (0-9), and underscores (_)
    # cannot start with a number (1var — error)
    # case sensitive: Data and data are two different variables.

# Style (Convention): 
    # in Python, it is customary to use snake_case 
    # (lowercase letters separated by underscores) for regular variables

    # example: user_login_count, not UserLoginCount

# Dynamic Typing
    # the type is tied to the value (object) rather than the variable (name) 
    # this means that the same variable can point to different data types 
    # throughout the life of the program

x = 10        # x refers to int
x = "Hello"   # now x refers to str (and that's OK)

# Reference Model
    # when you write a = [1, 2] and b = a, 
    # you are not copying the list,
    # you are simply attaching a second label (b) to the same object in memory



# Data types. Types are categorized:
    # numeric, sequence, mapping, set, boolean, and binary types 

# Numeric Types

x = 10              # integer (<class 'int'>)
y = -5234234234234  # can be as large as you want, as long as you have enough RAM

pi = 3.14     # float (<class 'float'>)
sci = 1.2e-5  # scientific record

z = 2 + 3j    # comlex (<class 'complex'>)

# Python does not have 'double' type 
    # you could use double via numpy (np.float64 - double)


# Sequence Types

my_list = [1, "a", 3.5] # list (mutable) (<class 'list'>)  
    # may contain elements of different types (int, string, float, bool, list)

my_tuple = (1, "Hello", 3.14, True, [10, 20]) # tuple (immutable) (<class 'tuple'>)
    # may contain elements of different types (int, string, float, bool, list)
# or like this
my_tuple2 = 12, "bye!", 2.71, (12, 'o'), False # tuple (immutable) (<class 'tuple'>)

r = range(5) # range, generates 0, 1, 2, 3, (<class 'range'>)

s = "Hello" # string (<class 'str'>) Unchanging Unicode character sequence (text)
    # technically, it is an array of characters


# Mapping Types

user = {"name": "Ivan", "age": 25} # dictionary (mutable) (<class 'dict'>)
    # works as key:value
    # Keys must be unique and unchangeable 
    # e.g. strings, numbers, tuples. Values can be anything.


# Set Types

# Unordered collections of unique elements 
    # The main feature is instant checking of element availability 
    # and mathematical operations (intersection, union)

my_set = {1, 2, 3, 3} # set (mutable) (<class 'set'>)

fs = frozenset([1, 2, 3]) # frozenset (immutable) (<class 'frozenset'>)
    # since it is unchanging, it can be used as a key in a dictionary


# Boolean Type
    # Only 2 meanings and used to check conditions

x = True    # True  (<class 'bool'>)
y = False   # False (<class 'bool'>)

    # in Python, bool is a subclass of int
    # True is 1 and False is 0
    # so:

z = True + True   # 2 (<class 'int'>)
t = True + False  # 1 (<class 'int'>)


# Binary Types
    # for working with “raw” data (images, files, network packets)
    # where it is important to operate with bytes rather than characters

    # bytes - unchanging sequence of bytes (numbers from 0 to 255)

b = b'Hello' # byte sequence (<class 'bytes'>)
    # also when data needs to be transmitted over a network (TCP/UDP)

    # bytearray - changing byte sequence. Individual bytes can be changed

ba = bytearray(5) # bytearray(b'\x00\x00\x00\x00\x00') (<class 'bytearray'>)
    # array of 5 zero bytes

    # memoryview - This is a “window” on a byte buffer 
                   # (e.g., bytes, bytearray, array.array) 
                   # without creating a new copy of the data.

# !For 'bytes', 'memoryview' will be read-only because 'bytes' are immutable!

mv = memoryview(b)  # creating memoryview (<class 'memoryview'>)
    # This is a tool for optimizing work with large amounts of data

print(mv[0])                # 72  → ASCII code 'H'
print(mv[1:4])              # <memory at 0x...>, but can be converted into bytes:
print(mv[1:4].tobytes())    # b'ell'


# Python Data Types Cheat Sheet
"""
| Category        | Type(s)                 | Mutable?                     |
|-----------------|-------------------------|------------------------------|
| Numeric         | int, float, complex     | No (creates a new object)    |
| Sequence        | str, tuple, range       | No                           |
| Sequence        | list                    | Yes                          |
| Mapping         | dict                    | Yes                          |
| Set             | set                     | Yes                          |
| Set             | frozenset               | No                           |
| Boolean         | bool                    | No                           |
| Binary          | bytes                   | No                           |
| Binary          | bytearray               | Yes                          |
| Binary          | memoryview              | Yes                          |
"""



# Conditional Statements

# The if Statement
    # the keyword if, a condition (an expression that returns True/False), 
    # and a mandatory colon :


# The elif Clause 
    # short for “else if” 
    # this is a unique feature of Python (other languages often write else if).


# The else Clause
    # this is the “in all other cases” option
    # does not accept any conditions
    # it is guaranteed to work if none of the above checks 
        # (if and elif) returned True. This is your “plan B”


status_code = 404

if status_code == 200:
    print("Success! Data received")
elif status_code == 404:
    print("Error: Resource not found")
elif status_code == 500:
    print("Server error: We are working on it")
else:
    # This block will work for all other codes (403, 401, 301, etc.)
    print(f"Unknown status: {status_code}")
    

# Truth Value Testing
    # this is a very “Python-like” concept
    # not only comparisons (x > 5) can be passed to the if condition, 
    # but also simple objects. Python automatically converts them to bool

    # Falsy values (as False)
        # the number 0 or 0.0.
        # empty containers: "" (empty string), [] (list), () (tuple), {} (dictionary).
        # None
        # False
    
    # Truthy values (as True)
        # any non-zero numbers (even -1)
        # any non-empty lines or lists


# Nested Conditions
    # you can place an if statement inside another if statement
    # each level of nesting requires an additional indent (4 spaces)

x = 10
if x > 0:
    print("True")
    if x % 2 == 0:
        print("and even")



# Loops
    # loops allow computers to do what they do best: 
    # quickly and accurately repeat the same action thousands of times


# The for Loop
    # in Python, the for loop works a little differently than in C++ or Java
    # it is an iterator. It doesn't just “count from 0 to 10”; 
    # it goes through the elements of any sequence (list, string, file)


fruits = ["Apple", "Banana", "Cherry"]

for fruit in fruits:
    # On the first iteration fruit = “Apple”
    # On the second = “Banana”...
    print(f"I like {fruit}")


# The range() Function
    # if you just need to repeat an action N times (like a classic loop in C), 
    # use the range() number generator

    # range(start, stop, step)
        # start: where to start (default is 0)
        # stop: where to stop (not including this number!)
        # step: step size (default is 1)


# counting from 0 to 4
for i in range(5): 
    print(i) # 0, 1, 2, 3, 4

# counting even numbers from 10 to 20
for i in range(10, 21, 2):
    print(i) # 10, 12, ... 18, 20


# The while Loop
    # used when we do not know how many times an action needs to be repeated, 
    # but we know the condition under which it needs to be performed

    # while this condition is True, run the loop

    # infinite Loop: 
        # if the condition never becomes False (for example, while True:), 
        # the program will hang. This is often used for servers that need to run forever
    

battery = 100

while battery > 0:
    print(f"Charge: {battery}% - Working...")
    battery -= 20 # It is important to change the condition so that the cycle stops at some point!

print("The battery is dead")


# Loop Control
    # sometimes you need to intervene in the standard cycle flow.

    # break: “Stop valve.” Immediately takes you out of the cycle, stopping its execution.

    # continue: “Skip move.” Immediately moves on to the next iteration, 
        # ignoring the rest of the code in the current loop.


for i in range(10):
    if i == 3:
        continue # skip three, continue printing
    if i == 8:
        break    # reached 8 and completely stopped the cycle
    print(i)


# The else Block in Loops
    # This is a unique and often misunderstood feature of Python. Loops can have an else block!

    # when it works: only if the loop has ended naturally 
        # i.e., it has not been stopped by a break

    # example: searching for something in a list


my_list = [1, 3, 5]
target = 4

for num in my_list:
    if num == target:
        print("Found!")
        break
else:
    # It will work because break was never called
    print("The number is not on the list")
