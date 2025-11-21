print("================ I. ADDITION OF NUMBERS ================")
print("------------------- SCENARIOS -------------------\n")
'''
  I. Based on Count
 II. Based on Type
III. Based on DataType
 IV. Zero Handling Scenarios
'''
print("================ I. Based on Count ================\n")

print("------ 1.1 Two Numbers ------")
# STATE
x = 10
y = 20
# BEHAVIOR
result = x + y
# DISPLAY
print("Addition of 2 numbers (", x, "+", y, ") =", result, "\n")

print("------ 1.2 Three or More Numbers ------")
# STATE
a = 10
b = 20
c = 30
# BEHAVIOR
result = a + b + c
# DISPLAY
print("Addition of 3 numbers (", a, "+", b, "+", c, ") =", result, "\n")

# You can extend this to 4, 5,... numbers similarly


print("================ II. Based on Type ================\n")

print("------ 2.1 Both Positive ------")
# STATE
x = 10
y = 20
# BEHAVIOR
result = x + y
# DISPLAY
print("Both positive (", x, "+", y, ") =", result, "\n")

print("------ 2.2 Both Negative ------")
# STATE
x = -5
y = -12
# BEHAVIOR
result = x + y
# DISPLAY
print("Both negative (", x, "+", y, ") =", result, "\n")

print("------ 2.3 First Positive, Second Negative ------")
# STATE
x = 4
y = -20
# BEHAVIOR
result = x + y
# DISPLAY
print("First positive, second negative (", x, "+", y, ") =", result, "\n")

print("------ 2.4 First Negative, Second Positive ------")
# STATE
x = -4
y = 20
# BEHAVIOR
result = x + y
# DISPLAY
print("First negative, second positive (", x, "+", y, ") =", result, "\n")


print("------ 2.5.1 Zero, Positive Number ------")
# STATE
x = 0
y = 30
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero + Positive (", x, "+", y, ") =", result, "\n")

print("------ 2.5.2. Zero, Negative Number ------")
# STATE
x = 0
y = -30
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero + Negative (", x, "+", y, ") =", result, "\n")

print("------ 2.6.1. Positive Number, Zero ------")
# STATE
x = 30
y = 0
# BEHAVIOR
result = x + y
# DISPLAY
print("Positive + Zero (", x, "+", y, ") =", result, "\n")


print("------ 2.6.2. Negative Number, Zero ------")
# STATE
x = -30
y = 0
# BEHAVIOR
result = x + y
# DISPLAY
print("Negative + Zero (", x, "+", y, ") =", result, "\n")


# =========================================================
# III. Based on DataType
# =========================================================
print("================ III. Based on DataType ================\n")

print("-------- 3.1 Both Integers --------")
# STATE
x = 20
y = 10
# BEHAVIOR
result = x + y
# DISPLAY
print("Int + Int (", x, "+", y, ") =", result, "\n")

# 2. Both Floats
print("-------- 3.2 Both Float --------")
# STATE
x = 20.5
y = 10.7
# BEHAVIOR
result = x + y
# DISPLAY
print("Float + Float (", x, "+", y, ") =", result, "\n")

print("-------- 3.3 Int + Float --------")
# STATE
x = 20
y = 10.7
# BEHAVIOR
result = x + y      # corrected to addition, not multiplication
# DISPLAY
print("Int + Float (", x, "+", y, ") =", result, "\n")

print("-------- 3.4 Float + Int --------")
# STATE
x = 20.5
y = 10
# BEHAVIOR
result = x + y
# DISPLAY
print("Float + Int (", x, "+", y, ") =", result, "\n")

print("-------- 3.5 Non-numeric datatypes (error)--------")
    # STATE
x = 20
y = "Ferilion Labs"
    # BEHAVIOR
result = x + y
    # DISPLAY
print("Int + String (", x, "+", y, ") =", result, "\n")

print("=============== 4. Zero Handling Scenarios ===============\n")

print("------ 4.1 Zero Allowed ------")
# STATE
x = 0
y = 25
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero + Positive (", x, "+", y, ") =", result, "\n")


print("------ 4.2 Zero Not Allowed ------")

def add_without_zero(a, b):
    if a == 0 or b == 0:
        raise ValueError("Zero is not allowed as an input")
    return a + b

# DEMO
try:
    print(add_without_zero(0, 10))
except ValueError as e:
    print("Error:", e, "\n")

print("------ 4.3. Zero as First Input ------")
# STATE
x = 0
y = -40
# BEHAVIOR
result = x + y
# DISPLAY
print("Zero as first input (", x, "+", y, ") =", result, "\n")

print("------ 4.4 Zero as Middle Input ------")
# STATE
a = 10
b = 0
c = 30
# BEHAVIOR
result = a + b + c
# DISPLAY
print("Zero in the middle (", a, "+", b, "+", c, ") =", result, "\n")


print("------ 4.5. Zero as Last Input ------")
# STATE
p = 50
q = -10
r = 0
# BEHAVIOR
result = p + q + r
# DISPLAY
print("Zero as last input (", p, "+", q, "+", r, ") =", result, "\n")



print("------------ REAL-TIME SCENARIOS ----------\n")

# Scenario 1: Bank Balance After Deposits
# ========================================

print("------ Bank Balance Calculation ------")
# STATE
bank_balance = 5000
dep1 = 100
dep2 = 500

# BEHAVIOR
final_balance = bank_balance + dep1 + dep2

# DISPLAY
print("Initial Balance:", bank_balance)
print("Deposits:", dep1, "+", dep2)
print("Final Bank Balance:", final_balance, "\n")


# Scenario 2: Shopping Bill Calculation
# ======================================
print("------ Shopping Bill Calculation ------")
# STATE: Item prices
shoe = 2000
bag = 3000
water_bottle = 100
watch = 500

# Quantities purchased
shoe_qty = 5
bag_qty = 3
water_qty = 10
watch_qty = 2

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
print("Final Amount Payable:", bill_after_discount, "\n")
print("--- Thank You. Visit Again ---")


'''
EXERCISES:
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
================================================
1. Add Two Positive Numbers
        Write a Python program to add two positive numbers 15 and 30 and display the result.
2. Add a Number and Zero
        Add the numbers 25 and 0.Explain why the output remains unchanged.
3. Add Three Floating-Point Numbers
        Calculate the sum of 12.5 + 3.25 + 7.80.Print the final result.

B. MEDIUM: (Deeper logic, multi-condition understanding)
=============================================================
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
=============================================================
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
