"""_1_equals.py"""

# Requirement : Check whether given 2 input numbers are equal or not.

# STATE
x = 10
y = 10

# BEHAVIOR
result = (x == y)

# Display Result
print("Are the two numbers equal? :", result)
# Expected output : True , Actual output :


# Ex 2 : Checking if the addition result is correct

print("------ Using == Operator with Addition Result ------")

# STATE
x = 10
y = 20

expected = 30

# BEHAVIOR
result = x + y
is_correct = (result == expected) # COMPARISON USING == operator

# Display Result
print("Addition Result     :", result)
print("Expected Result     :", expected)
print("Is result correct?  :", is_correct)

# Ex 3 : 2. Using == in Real-Time Scenario (Bank Deposit)

print("------ Bank Balance Verification using == ------")

# STATE
bank_balance = 5000
dep1 = 100
dep2 = 500
expected_balance = 5600

# BEHAVIOR
final_balance = bank_balance + dep1 + dep2
is_match = (final_balance == expected_balance) # COMPARISON USING == operator

# Display Result
print("Calculated Balance :", final_balance)
print("Expected Balance   :", expected_balance)
print("Bank balance correct?:", is_match)

# Ex 3 : 3. Using == in Shopping Bill Calculation

print("------ Shopping Bill Verification using == ------")

# STATE
shoe = 2000
bag = 3000
bottle = 100
watch = 500

gross_expected = 2000*5 + 3000*3 + 100*10 + 500*2   # expected total

# BEHAVIOR
gross_calculated = (shoe*5) + (bag*3) + (bottle*10) + (watch*2)

# COMPARISON USING ==
is_total_correct = (gross_calculated == gross_expected)

# DISPLAY
print("Expected Gross Bill :", gross_expected)
print("Calculated Bill     :", gross_calculated)
print("Is Bill Correct?    :", is_total_correct)


'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
================================================
1. Check whether 10 and 10 are equal
2. Compare the strings "Python" and "python" using ==
3. Take two variables a = 5, b = 3 + 2. Use == to check if they are equal

B. MEDIUM: (Deeper logic, multi-condition understanding)
=============================================================
4. Ask the user for two numbers and check if they are equal using ==
5. Check if the total of (12 + 8) is equal to 20 using ==
6. Compare two results: (15 - 5) and (2 * 5) using ==

C. DIFFICULT: (Advanced reasoning + real engineering logic)
=============================================================
7. A shopkeeper collected ₹2500 in the morning and ₹1500 in the evening
        Check using == if the total collection is equal to ₹4000

8. A student's marks: Math=40, Science=35, English=25
        Check using == whether the total marks equal 100

9. A bank account starts with ₹5000
            Two deposits: ₹250 and ₹750
            One withdrawal: ₹1000
        Check using == whether the final balance equals ₹5000
'''
