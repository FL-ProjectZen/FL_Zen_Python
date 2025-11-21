"""_1_and.py"""

# Requirement : Check whether two conditions are True using logical AND operator

# Ex 1 : Basic AND condition check
print("------ Simple Example ------")

# STATE
x = 10
y = 20

# BEHAVIOR
result = (x > 5 and y > 10)   # BOTH conditions must be True

# DISPLAY
print("Are both conditions True? :", result)
# Expected output : True , Actual output :


# Ex 2 : Checking if both subject scores qualify the student
print("------ Using AND Operator for Qualification Check ------")

# STATE
math = 45
science = 50

passing_marks = 40

# BEHAVIOR
is_passed = (math >= passing_marks and science >= passing_marks)

# Display Result
print("Math Score        :", math)
print("Science Score     :", science)
print("Both Subjects Passed? :", is_passed)


# Ex 3 : Real-Time Scenario (Bank Minimum Balance + KYC)
print("------ Bank Account Activation using AND ------")

# STATE
min_balance_required = 1000
account_balance = 1200
kyc_completed = True

# BEHAVIOR
is_account_active = (account_balance >= min_balance_required and kyc_completed)

# DISPLAY
print("Account Balance         :", account_balance)
print("KYC Completed?          :", kyc_completed)
print("Is Account Active?      :", is_account_active)

# Ex 4 : Shopping Offer Eligibility using AND
print("------ Shopping Offer Check using AND ------")

# STATE
cart_value = 2500
is_member = True

# BEHAVIOR
is_offer_applicable = (cart_value >= 2000 and is_member)

# DISPLAY
print("Cart Value          :", cart_value)
print("Membership Status   :", is_member)
print("Is Offer Applicable :", is_offer_applicable)



'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY:
========== 
1. Check if a number is both positive and even using AND
2. Verify if a person is eligible for entry (age >= 18 AND ticket == True)
3. Check two conditions: a = 5 > 2 AND b = 10 > 8

B. MEDIUM: (Deeper logic, multi-condition understanding)
=============================================================
4. Validate login using (username_correct AND password_correct)
5. Check if a student passes when both theory_score >= 40 AND practical_score >= 20
6. Check if an offer applies when cart_value >= 1000 AND coupon_applied == True

C. DIFFICULT: (Advanced reasoning + real engineering logic)
=============================================================
7. A bank approves a loan if income >= 50000 AND cibil_score >= 700
        Write a program to check approval status
8. A job candidate is eligible if experience >= 3 AND qualification == "BTech"
        Check eligibility for a given candidate
9. A travel pass is issued only if (id_provided == True AND vaccination_status == True)
        Validate and print whether pass is issued

'''
