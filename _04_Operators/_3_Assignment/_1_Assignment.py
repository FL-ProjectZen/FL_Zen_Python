"""_1_Assignment.py"""

# Requirement : Demonstrate assignment (=) and add & assign (+=) operators

# Ex 1 : Using = operator

print("------ Basic Assignment Operator (=) ------")

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
