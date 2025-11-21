"""_3_not.py"""

# Requirement : Reverse (invert) the result of a condition using logical NOT operator

# Ex 1 : Basic NOT condition check
print("------ Simple Example ------")

# STATE
is_active = True

# BEHAVIOR
result = not is_active   # NOT reverses the Boolean value

# DISPLAY
print("Is Active?       :", is_active)
print("NOT Active?      :", result)
# Expected output : False , Actual output :


# Ex 2 : Checking user access denial using NOT
print("------ Using NOT Operator for Access Denial ------")

# STATE
has_access = False

# BEHAVIOR
is_blocked = not has_access

# DISPLAY
print("Access Granted?   :", has_access)
print("Access Blocked?   :", is_blocked)


# Ex 3 : Real-Time Scenario (Maintenance Mode)
print("------ System Availability using NOT ------")

# STATE
under_maintenance = True

# BEHAVIOR
system_available = not under_maintenance

# DISPLAY
print("Under Maintenance? :", under_maintenance)
print("System Available?  :", system_available)


# Ex 4 : Shopping Free Delivery Condition using NOT
print("------ Free Delivery Check using NOT ------")

# STATE
is_guest_user = True

# BEHAVIOR
free_delivery_applicable = not is_guest_user   # Only registered users get free delivery

# DISPLAY
print("Is Guest User?           :", is_guest_user)
print("Free Delivery Applicable :", free_delivery_applicable)



'''
EXERCISES:  
===========
Write programs for below requirements:
Note: While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
================================================
1. Take a Boolean variable logged_in = True and print its NOT value
2. Create a variable is_raining and check not is_raining
3. Check NOT of a simple comparison like not(5 > 2)

B. MEDIUM: (Deeper logic, multi-condition understanding)
=============================================================
4. A user is blocked if not is_verified
        Write a program to check block status
5. A student gets attendance if not on_leave
        Validate attendance using NOT
6. Check whether a device is working when not device_faulty

C. DIFFICULT: (Advanced reasoning + real engineering logic)
=============================================================
7. A system becomes available when not under_maintenance
        Build a program to validate availability
8. A discount applies only when not is_guest_user
        Validate discount eligibility
9. A secure area grants entry only when not is_blacklisted
        Check access permission and display final result
'''
