"""
===============================================================================

    Ferilion Labs Private Limited

    Website       : https://www.ferilionlabs.com

    LMS Portal    : https://www.ferilion.com

    © Copyright — All Rights Reserved.
    This file is proprietary educational content created exclusively for
    trainees of Ferilion Labs.

    Unauthorized copying, distribution, modification, publishing, or
    sharing of this material in any form is strictly prohibited.

    Violations will result in legal action under applicable IP laws.

    Allowed Usage:
        - For personal learning within Ferilion Labs
        - For assignments, projects, and interview preparation
        - NOT permitted to redistribute or upload elsewhere

    Team Ferilion Labs
===============================================================================
"""

# Requirement : Demonstrate assignment (=)

# Ex 1 : Using = operator

print("------ Basic Assignment Operator (=) ------")

'''
Assignment operators are not just “symbols”
    They represent a state-update mindset

    Take the existing value, transform it, save the new state

Pattern : 
        LHS  =  RHS
     target     value/expression

RHS -> Something that resolves to a value at runtime
LHS ->     


'''

# Examples

x = 10
entity = "Ferilion Labs"
result = 10 + 20

'''
Why Assignment Operators Matter (Engineering Mindset)

1. Memory Efficient Updates: 
                Python updates existing objects where possible — no unnecessary new objects.
2. Cleaner, More Readable Code: 
                Instead of writing repetitive expressions, you express the intent clearly.
3. Perfect for Loops & State Updates:
                Used heavily in counters, accumulators, aggregators.
4. Matches Mathematical Transformation Logic
                x += 1 is mentally mapped to x = x + 1.
5. Used in Production-Grade Code & APIs
                Logging counters, metrics, batch processing loops, retry logic.



'''

# EXAMPLES:

# STATE
x = 10
y = 20

# BEHAVIOR
# Assign values directly
a = x
b = y

# DISPLAY
print("Value of a :", a)
print("Value of b :", b)


# Ex 2 : Using = to store arithmetic results

print("------ Using = Operator with Arithmetic ------")

# STATE
num1 = 50
num2 = 30

# BEHAVIOR
result = num1 + num2   # assignment of computed value

# DISPLAY
print("Addition Result :", result)


# Ex 3 : Real-Time Scenario (Wallet Recharge)

print("------ Wallet Recharge using = ------")

# STATE
wallet_balance = 1000
recharge_amount = 500

# BEHAVIOR
updated_balance = wallet_balance + recharge_amount

# DISPLAY
print("Updated Wallet Balance :", updated_balance)


'''
LHS = RHS

RHS Allowed Values : 
=====================
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
S.No | Python Chapter        | RHS Category                   | Python Example                               | Category Info / Extra Meaning                   | Purpose / Meaning (Simple)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
1    | Variables             | Literal Values                 | x = 10                                       | Final direct values (int/float/bool/str etc.)   | Assign fixed constant values
2    | Variables             | Variable to Variable           | y =  x                                       | Reuse of previously stored variable             | Reuse existing value
3    | Operators             | Expressions                    | total = price + tax                          | Combination of operators to compute a result    | Compute-and-assign
4    | Functions             | Function Calls                 | name = input("Enter name: ")                 | Value comes from function execution             | Capture return value of function
5    | String Methods        | Method Calls                   | cleaned = message.strip()                    | Object operations (.strip(), .upper(), etc.)    | Store method output
6    | Type Casting          | Type Conversions (Casting)     | age = int("25")                              | Convert type with int(), float(), bool(), str() | Convert data types before storing
7    | Built-ins             | Constructors (Built-ins)       | today = date(2025, 1, 1)                     | Create objects using built-in constructors      | Assign newly constructed objects
8    | OOPs                  | Class Instantiation            | emp = Employee("MAD", "Ferilion Labs", 101)  | Blueprint → object instance                     | Store object created from a class
9    | Functions / Lambda    | Lambda Expressions             | square = lambda x: x*x                       | Small anonymous inline functions                | Assign small callable functions
10   | Data Structures       | Comprehensions                 | nums = [x*x for x in range(5)]               | Dynamic list/set/dict generation                | Assign dynamically generated collections
11   | Data Structures       | Data Structure Literals        | config = {"a": 1, "b": 2}                    | List/tuple/dict/set literal syntax              | Assign structured data
12   | Modules               | Module Attributes              | pi = math.pi                                 | Values imported from modules                    | Assign predefined library constants
13   | Decision Making       | Inline Conditional Expressions | result = x if x > y else y                   | One-line conditional logic                      | Choose value based on condition
14   | File/OS Integration   | External Inputs                | env = os.getenv("ENV")                       | Comes from environment, file, API, user input   | Assign external runtime inputs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

LHS Allowed names : 
====================
------------------------------------------------------------------------------------------------------------------------------------------------------
S.No | Python Chapter        | LHS Category                     | Python Example                         | Purpose / Meaning (Simple)
------------------------------------------------------------------------------------------------------------------------------------------------------
1    | Variables             | Variable Name                    | x = 10                                 | Store a value in a named variable
2    | Variables             | Multiple Variable Assignment     | a, b = 10, 20                          | Assign multiple values at once
3    | Variables             | Chain Assignment                 | x = y = z = 100                        | Assign same value to multiple variables
4    | Data Structures       | Sequence Unpacking               | a, b, c = [1, 2, 3]                    | Extract items from list/tuple
5    | Data Structures       | Nested Unpacking                 | (a, (b, c)) = (1, (2, 3))              | Unpack nested structured data
7    | Data Structures       | Item Assignment                  | data[0] = 99                           | Update element in list/dict/set
8    | Data Structures       | Slicing Assignment               | nums[1:3] = [10, 20]                   | Replace part of a sequence
9    | OOPs                  | Instance Variables               | self.age = 25                          | Assign values inside objects
6    | OOPs                  | Attribute Assignment             | emp.company = "Ferilion Labs"          | Assign value to object attribute
10   | OOPs                  | Class Variables                  | Employee.company = "Ferilion Labs"     | Shared value for all class objects
11   | Type Hinting          | Annotated Assignment (PEP 526)   | age: int = 25                          | Assign value with type hint
12   | Operators / Expressions | Walrus Expression (LHS part)     | (x := 10)                              | Assign inside logical expressions
------------------------------------------------------------------------------------------------------------------------------------------------------


'''


'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
------------------------------------------------
1. Check whether 10 and 10 are equal
2. Compare the strings "Python" and "python" using ==
3. Take two variables a = 5, b = 3 + 2. Use == to check if they are equal

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
4. Ask the user for two numbers and check if they are equal using ==
5. Check if the total of (12 + 8) is equal to 20 using ==
6. Compare two results: (15 - 5) and (2 * 5) using ==

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-------------------------------------------------------------
7. A shopkeeper collected ₹2500 in the morning and ₹1500 in the evening
        Check using == if the total collection is equal to ₹4000

8. A student's marks: Math=40, Science=35, English=25
        Check using == whether the total marks equal 100

9. A bank account starts with ₹5000
            Two deposits: ₹250 and ₹750
            One withdrawal: ₹1000
        Check using == whether the final balance equals ₹5000
'''
