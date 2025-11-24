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

# REQUIREMENT : PRINT ADDITION OF NUMBERS

# Draft Code:

# STATE
x = 10
y = 20

# BEHAVIOR
result = x + y

# Display end result
print("Addition of 2 numbers = ", result)


print("================ REQUIREMENT : PRINT ADDITION OF NUMBERS ================")

'''
Requirement Deconstruction & Functional Understanding:
--------------------------------------------------------
    - Breaking down requirements
    - discovering intent
    - mapping STATE + BEHAVIOR
    - Identifying constraints

Let us see step by step:
    
    STEP 1: Understand the Requirement Like a Developer
            Flow Steps: 
                1. Read the requirement in plain English
                        - The system should be able to add two or more numbers and return the correct sum
                2. Identify STATE
                        - Input : Min. 2 numbers (int,float etc.,)
                        - Output: 1 number 
                3. Define BEHAVIOR
                        - Functional : Here the action part is to perform addition operation on given input values
                        - Technical  : To achieve this functionality, 
                                            - Use operator + of Arithmetic Ops
                4. Display the result: Use print statement and display the result 
    
    STEP 2: Create Scenario Buckets (Testing Methodology)
                A. Count-based Scenarios  : Does the function handle 2 numbers? 3 numbers? N numbers?
                B. Type-based Scenarios   : How does addition behave with +, –, and 0?
                C. Datatype Scenarios     : What happens with int vs float combinations?
                D. Zero-handling Scenarios: Is zero allowed? Does it change the result?
    
    STEP 3: Expand Each Bucket Into Scenarios
                A. Count-Based Scenarios:
                    --------------------------
                    | Scenario                    | Meaning                                               |
                    | --------------------------- | ----------------------------------------------------- |
                    | 1. Add exactly 2 numbers    | Basic operation (most common)                         |
                    | 2. Add 3 numbers            | Multi-argument support                                |
                    | 3. Add 4 or more numbers    | Scalability of the addition logic                     |
                    | 4. Add 1 number (edge case) | Should return the same number                         |
                    | 5. Add zero numbers         | Should raise error OR return 0 (based on requirement) |
                    
                    B. Type-Based Scenarios:
                    ------------------------
                    | Scenario                           | Meaning               |
                    | ---------------------------------- | --------------------- |
                    | 1. Both positive                   | Normal addition       |
                    | 2. Both negative                   | Sum remains negative  |
                    | 3. First positive, second negative | Mixed signs           |
                    | 4. First negative, second positive | Reverse mixed signs   |
                    | 5. Zero + positive/negative        | Zero-neutral behavior |
                    | 6. Positive/negative + zero        | Same as above         |
                    
                    C. Datatype-Based Scenarios:
                    ----------------------------
                    | Scenario                         | Meaning                               |
                    | -------------------------------- | ------------------------------------- |
                    | 1. Both int                      | Integer arithmetic                    |
                    | 2. Both float                    | Floating point arithmetic             |
                    | 3. int + float                   | Type promotion expected (int → float) |
                    | 4. float + int                   | Same as above                         |
                    | 5. Non-numeric datatypes (error) | Strings, booleans, lists              |
                    
                    D. Zero-Handling Scenarios:
                    ---------------------------
                    | Scenario                | Meaning                |
                    | ----------------------- | ---------------------- |
                    | 1. Zero allowed         | Valid input            | 
                    | 2. Zero not allowed     | Raise validation error |
                    | 3. Zero as first input  | No effect              |
                    | 4. Zero as middle input | No effect              |
                    | 5. Zero as last input   | No effect              |
    
    STEP 4: Convert Scenarios → Test Cases (Unit Testing Standard)
            Scenario:                           Test Case 
            ------------------------            -------------------------------------------       
            Both numbers positive               Input: 4 + 5        Expected Output: 9
            int + float                         Input: 10 + 2.5     Expected Output: 12.5

print("------------------- SCENARIOS -------------------")
Understand the Requirement and extract scenarios as below. 
      I. Based on Count
     II. Based on Type
    III. Based on DataType
     IV. Zero Handling Scenarios
'''
print("================ SC I. Based on Count ================")

print("------ 1.1 Two Numbers ------")
# STATE
x = 10
y = 20
# BEHAVIOR
result = x + y
# DISPLAY
print("Addition of 2 numbers = ", result)

print("------ 1.2 Three or More Numbers ------")
# STATE
a = 10
b = 20
c = 30
# BEHAVIOR
result = a + b + c
# DISPLAY
print("Addition of 3 numbers = ", result)

# You can extend this to 4, 5,... numbers similarly


print("================ SC II. Based on Type ================")

print("------ 2.1 Both Positive ------")
# STATE
x = 10
y = 20
# BEHAVIOR
result = x + y
# DISPLAY
print("Both positive = ", result)

print("------ 2.2 Both Negative ------")
# STATE
x = -5
y = -12
# BEHAVIOR
result = x + y
# DISPLAY
print("Both negative = ", result)

print("------ 2.3 First Positive, Second Negative ------")
# STATE
x = 4
y = -20
# BEHAVIOR
result = x + y
# DISPLAY
print("First positive, second negative  = ", result)

print("------ 2.4 First Negative, Second Positive ------")
# STATE
x = -4
y = 20
# BEHAVIOR
result = x + y
# DISPLAY
print("First negative, second positive  = ", result)


print("------ 2.5.1 Zero, Positive Number ------")
# STATE
x = 0
y = 30
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero + Positive  = ", result)

print("------ 2.5.2. Zero, Negative Number ------")
# STATE
x = 0
y = -30
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero + Negative = ", result)

print("------ 2.6.1. Positive Number, Zero ------")
# STATE
x = 30
y = 0
# BEHAVIOR
result = x + y
# DISPLAY
print("Positive + Zero = ", result)


print("------ 2.6.2. Negative Number, Zero ------")
# STATE
x = -30
y = 0
# BEHAVIOR
result = x + y
# DISPLAY
print("Negative + Zero = ", result)


print("================ SC III. Based on DataType ================\n")

print("-------- 3.1 Both Integers --------")
# STATE
x = 20
y = 10
# BEHAVIOR
result = x + y
# DISPLAY
print("Int + Int = ", result)

# 2. Both Floats
print("-------- 3.2 Both Float --------")
# STATE
x = 20.5
y = 10.7
# BEHAVIOR
result = x + y
# DISPLAY
print("Float + Float = ", result)

print("-------- 3.3 Int + Float --------")
# STATE
x = 20
y = 10.7
# BEHAVIOR
result = x + y      # corrected to addition, not multiplication
# DISPLAY
print("Int + Float = ", result)

print("-------- 3.4 Float + Int --------")
# STATE
x = 20.5
y = 10
# BEHAVIOR
result = x + y
# DISPLAY
print("Float + Int = ", result)

print("-------- 3.5 Non-numeric datatypes (error)--------")
    # STATE
x = 20
y = "Ferilion Labs"
    # BEHAVIOR
# result = x + y # Statement (Equation)
    # DISPLAY
# print("Int + String = ", result)

print("=============== SC IV. Zero Handling Scenarios ===============")

print("------ 4.1 Zero Allowed ------")
# STATE
x = 0
y = 25
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero + Positive = ", result)


print("------ 4.2 Zero Not Allowed ------")

x = 10
y = 0
if x == 0 or y == 0:
    print("Zero Not Allowed ")
else:
    result = x + y
    print("Non Zero  = ", result)

print("------ 4.3. Zero as First Input ------")
# STATE
x = 0
y = -40
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero as first input  = ", result)

print("------ 4.4 Zero as Middle Input ------")
# STATE
a = 10
b = 0
c = 30
# BEHAVIOR
result = a + b + c
# DISPLAY
print("Zero in the middle = ", result)


print("------ 4.5. Zero as Last Input ------")
# STATE
p = 50
q = -10
r = 0
# BEHAVIOR
result = p + q + r
# DISPLAY
print("Zero as last input = ", result)



print("------------ REAL-TIME EXAMPLES ----------")

# Requirement 1: Print Bank Balance After Deposits

print("------ Requirement 1: Bank Balance Calculation ------")

# STATE: Balance details
bank_balance = 5000
dep1 = 100
dep2 = 500

# BEHAVIOR
final_balance = bank_balance + dep1 + dep2

# DISPLAY
print("Initial Balance:", bank_balance)
print("Deposits:", dep1, dep2)
print("Final Bank Balance:", final_balance)


# Requirement 2: Shopping Bill Calculation

print("------ Requirement 2: Shopping Bill Calculation, bag with 10% discount ------")
# STATE

# Item prices
shoe = 2000
bag = 3000
water_bottle = 100
watch = 500
# Quantities purchased
shoe_qty = 5
bag_qty = 3
water_qty = 10
watch_qty = 2

# gross_bill = shoe*shoe_qty + bag*bag_qty + water_bottle*water_qty + watch*watch_qty
# print("Gross bill (before tax & discount):", gross_bill)

# BEHAVIOR: Calculate item totals
shoe_price = shoe * shoe_qty
bag_price = bag * bag_qty
water_price = water_bottle * water_qty
watch_price = watch * watch_qty

# Total before tax + discount
gross_bill = shoe_price + bag_price + water_price + watch_price


# DISPLAY intermediate results
print("Gross bill (before tax & discount):", gross_bill)

# Tax and discount rates
c_tax = 2.5  # Central GST
s_tax = 2.5  # State GST
discount = 10  # Flat discount %

# BEHAVIOR: Add GST
bill_after_tax = gross_bill + gross_bill * c_tax / 100 + gross_bill * s_tax / 100

# BEHAVIOR: Apply discount
bill_after_discount = bill_after_tax - bill_after_tax * discount / 100

# DISPLAY final bill breakdown
print("Bill After Tax:", bill_after_tax)
print("Bill After Discount:", bill_after_discount)
print("Final Amount Payable:", bill_after_discount,)
print("------- Thank You. Visit Again -------")


'''
EXERCISES:
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
------------------------------------------------
1. Add Two Positive Numbers
        Write a Python program to add two positive numbers 15 and 30 and display the result.
2. Add a Number and Zero
        Add the numbers 25 and 0.Explain why the output remains unchanged.
3. Add Three Floating-Point Numbers
        Calculate the sum of 12.5 + 3.25 + 7.80.Print the final result.

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
4. Profit Calculation in a Shop
    A shopkeeper sells: 
            3 pens at ₹10 each, 
            2 notebooks at ₹40 each
    Calculate the total amount collected.
5. Bus Passenger Count Update
    A bus starts with 35 passengers.
        At Stop 1 → 7 passengers board
        At Stop 2 → 3 passengers board
        At Stop 3 → 5 passengers get off
    Find the final count of passengers.

6. Type-Based Addition
    Add the following mixed types:
        x = 20 (int)
        y = -5.75 (float)
    Print the result and explain whether the output is int or float.

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
7. Shopping Bill with Tax and Discount
    A customer buys:
        Shoes: price ₹1500, quantity 2
        Bags: price ₹2000, quantity 1
        Water bottles: price ₹80, quantity 4
    
        GST: 5%
        Discount: 10%
    Calculate the final bill amount.

8. Salary Components Calculation
    Given:
        Basic Salary: ₹30,000
        HRA: 12% of basic
        DA: 7% of basic
        Travel Allowance: ₹3,000
    Find the total salary after addition of all components.

9. Bank Account Simulation (Zero Handling + Multiple Deposits)
        Initial balance: ₹8000
        Deposits: ₹0, ₹1500, ₹350, ₹900
    Task:Treat zero deposit as valid input.
        Add all deposits to find the final account balance.
'''
