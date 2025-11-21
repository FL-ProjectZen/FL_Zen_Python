"""_2_or.py"""

# Requirement : Check whether at least one condition is True using logical OR operator

# Ex 1 : Basic OR condition check
print("------ Simple Example ------")

# STATE
x = 10
y = 5

# BEHAVIOR
result = (x > 15 or y > 2)   # ANY one condition being True makes output True

# DISPLAY
print("Is at least one condition True? :", result)
# Expected output : True , Actual output :


# Ex 2 : Checking if a student gets grace pass
print("------ Using OR Operator for Grace Pass Check ------")

# STATE
score = 38
has_grace_marks = True

# BEHAVIOR
is_passed = (score >= 40 or has_grace_marks)

# DISPLAY
print("Student Score       :", score)
print("Grace Marks?        :", has_grace_marks)
print("Passed?             :", is_passed)


# Ex 3 : Real-Time Scenario (Bank Alert)
print("------ Bank Alert Trigger using OR ------")

# STATE
balance = 500
min_required = 1000
sms_alert_enabled = True

# BEHAVIOR
is_alert_triggered = (balance < min_required or sms_alert_enabled)

# DISPLAY
print("Account Balance     :", balance)
print("SMS Alerts Enabled? :", sms_alert_enabled)
print("Is Alert Triggered? :", is_alert_triggered)


# Ex 4 : Shopping Discount Eligibility using OR
print("------ Shopping Discount Check using OR ------")

# STATE
cart_value = 800
is_premium_member = True

# BEHAVIOR
is_discount_applicable = (cart_value >= 1000 or is_premium_member)

# DISPLAY
print("Cart Value             :", cart_value)
print("Premium Member?        :", is_premium_member)
print("Discount Applicable?   :", is_discount_applicable)



'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
================================================
1. Check if a number is positive OR even using OR
2. Verify if a user gets entry if (age >= 18 OR has_parent_consent == True)
3. Check conditions: a = 5 < 3 OR b = 10 > 2

B. MEDIUM: (Deeper logic, multi-condition understanding)
=============================================================
4. Validate login access if (is_admin == True OR has_temp_password == True)
5. Check if a student passes if (score >= 40 OR grace_marks == True)
6. Check if a discount applies when (cart_value >= 1500 OR coupon_applied == True)

C. DIFFICULT: (Advanced reasoning + real engineering logic)
=============================================================
7. A person qualifies for a loan if income >= 50000 OR has_guarantor == True
        Write a program to check eligibility

8. A job candidate may proceed if experience >= 2 OR certification_completed == True
        Validate candidate status

9. A system gives access if (is_employee == True OR has_guest_pass == True)
        Check and display access permissions
'''

