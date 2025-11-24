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


'''
File contents:
---------------
    A. Comments in Python
    B. Readable Code Mindset
'''

'''
A. Comments in Python:
=======================
    - Comments are lines in your code that Python ignores, but humans read.
    - They help you explain logic, document code, and improve readability.
    - Think of comments as communication from your present self to your future self and your teammates.

Types:  1.Single-Line Comments
        2. Multi-Line Comments
'''

'''
1.Single-Line Comments: 
        Single-line comments start with the # symbol.
        Python ignores everything written after the # in that line.
'''

# This prints a welcome message  --> This is Single line comment
print("Welcome to Python")

x = 10  # number of trainees     --> This is Inline Comment

'''
When to use Single-Line Comments:
    -  Explaining a single line of logic
    -  Marking TODOs
    -  Giving context for a variable
    -  Quick notes for other developers
'''


'''
1.Multi-Line Comments: 
        Python does not have an official multi-line comment syntax, but developers use triple quotes.
        ''' ''' or """ """
        Python ignores everything written within quotes.

    These are technically multi-line strings not used in code, so Python ignores them.
'''

# Example 1:

'''
This section calculates the discount amount.
We are using formula: final_price = price - discount
Applicable only for premium customers
'''
price = 1000
discount = 150
final_price = price - discount
print("Price after discount: ", final_price)

# Example 2:

"""
Multi-line comment using double quotes.
Useful for explaining complex logic or module-level documentation.
"""

price = 1000
discount = 150
final_price = price - discount
print("Price after discount: ", final_price)


'''
When to use Multi-Line Comments:
    - Explaining a chunk of logic
    - Documenting a function prototype (temporary)
    - Writing large notes in teaching material
    - Adding block-level explanations or step-by-step guides
'''

'''
SUMMARY: 
========

| Type                  | Symbol                                 | Use Case                                     |
| --------------------- | -------------------------------------- | -------------------------------------------- |
| Single-Line Comment   | #                                      | Quick explanation, inline notes              |
| Multi-Line Comment**  | '''  ''' or """ ... """                | Block-level notes, teaching explanations     |
| Docstring             | triple quotes inside functions/classes | Official function/class/module documentation |
'''

"""
B. Readable Code Mindset :
========================
    Anybody can write code a computer can understand.
                Great developers write code humans can understand.

    Writing code is easy.
            Writing code another developer understands in 6 months — that’s engineering.
    
    Good code works.
            Great code communicates.

1. Expressive Naming & Intent-Driven Code: 
2. Transparent Logic & Traceable Data Flow:
3. Team-Friendly, Consistent Coding Style:
4. Maintainable & Future-Proof Code Structure:
5. Professional Standards & Enterprise Coding Discipline:
"""

'''
1. Expressive Naming & Intent-Driven Code:
        Makes code instantly understandable without guessing the developer’s intent
'''
# Poor Practice (Ambiguous Intent)
x = 10
print(x)

# Professional Standard (Clear Intent)
trainee_id = 10
print("Trainee id is : ", trainee_id)

# Outcome: Anyone reading the code knows it prints the trainee id

'''
2. Transparent Logic & Traceable Data Flow:
        Reduces debugging time because logic and data flow are clearly visible
'''
# Anti-Pattern
print(500 + (500 * 0.18))

# Professional Standard (Step-by-step clarity)
base_price = 500
tax_rate = 0.18
total_price = base_price + (base_price * tax_rate)
print("Total Price : ", total_price)

# Outcome: Every step can be understood and debugged easily

'''
3. Team-Friendly, Consistent Coding Style:
        Helps teams collaborate smoothly — everyone reads the same meaning
'''
# Not Recommended (Team cannot understand the context)
n = 20
f = 100
tp = n * f
print("Result :",tp)

# Team-Friendly Standard
num_students = 20
fee = 100
total_payment = num_students * fee
print("Total payment collected : ", total_payment)

# Outcome: Code is readable to anyone newly joining the project

'''
4. Maintainable & Future-Proof Code Structure:
        Prevents future maintenance issues caused by vague or messy code
'''
# Low-Quality Code (Hardcoded logic)
print("Discounted Amount:", 999 * 0.85)

# Maintainable Structure (Easy to update later)
bill_amount = 999
discount_rate = 0.15
final_amount = bill_amount * (1 - discount_rate)
print("Final Bill Amount : ", final_amount)
print("Applicable discount %:" ,discount_rate*100)

# Outcome: DRY Principle (Don’t Repeat Yourself) : Change discount_rate one time → code still works everywhere


'''
5. Professional Standards & Enterprise Coding Discipline:
        Creates production-ready habits expected from 3–5 YOE engineers
'''
# Poor Engineering Habit
print("User:", "Ferilion Labs", 25, "Bangalore")

# Enterprise-Ready Pattern (Structured, meaningful output)
user_name = "Ferilion Labs"
user_age = 25
user_city = "Bangalore"

print("User Info → ",user_name, user_age, user_city) # Logger concept

# Outcome: Logs become readable, structured, and useful in real systems




# Let us take simple example to consolidate above examples

print("============ ADDING NUMBERS ============")

'''
Approach 1: Hard-Coding Values
--------------------------------
    This is the beginner’s instinctive approach.
        -   Not scalable.
        -   Not reusable.
        -   Not acceptable in real-world systems.
    Used only to demonstrate a concept quickly.
'''
print("------------- Approach 1 -------------")
print(10 + 20)   # Hard-coded, single-use, fixed data


'''
Approach 2: Static Variables (Still Hardcoded, but Cleaner)
------------------------------------------------------------
    Here, the numbers are stored in variables.
    This is readable and maintainable for small demonstrations.
    However:
        - Values still cannot change dynamically.
        - Not suitable for UI, APIs, databases, or automated workflows.
'''
print("------------- Approach 2.1 -------------")
x = 10
y = 20
print("Addition :", x + y)

print("------------- Approach 2.2 -------------")
num1 = 10
num2 = 20
result = num1 + num2
print("Addition :", result)

'''
Approach 3: Ideal Real-World Approach (Dynamic Input)
--------------------------------------------------------
This is where engineering standards begin.

Key Concepts:
- Accept input dynamically (UI → Python → DB)
- Understand that input() returns STRING
- Demonstrate data flow between layers
- Highlight why type conversion matters

This is not just Python — this is Software Engineering Mindset.

BUT: This example still produces string concatenation.
That itself is a teaching moment!
'''
print("------------- Approach 3 (Ideal Input Flow) -------------")

x = int(input("Enter number1 : "))
y = int(input("Enter number2 : "))
output = x + y
print("Addition :", output)

'''
Why This Matters:
------------------
This trains developers to understand:
- how UI sends all values as strings
- why backend must handle conversion
- how databases expect typed data
- why validation is essential before processing
'''





