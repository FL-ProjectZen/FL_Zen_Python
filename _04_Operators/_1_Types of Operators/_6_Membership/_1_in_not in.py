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
# Examples


# 1. String

print("p" in "python")      # True
print("z" not in "python")  # True
print("t" not in "python")  # False



# 2. List

nums = [10, 20, 30, 40]
print(20 in nums)           # True
print(50 not in nums)       # True

# 3. Tuple

t = (1, 2, 3, 4)
print(3 in t)               # True
print(10 not in t)          # True


# 4. Range

r = range(1, 10)
print(5 in r)               # True
print(15 not in r)          # True

# 5. Bytes

b = b"hello"
print(104 in b)             # True   # ASCII of 'h' is 104
print(120 not in b)         # True

# 6. Bytearray

ba = bytearray(b"madhu")
print(109 in ba)            # True   # ASCII of 'm'
print(122 not in ba)        # True


# Summary

data = ["python", (1, 2), range(5), b"hi", bytearray(b"ok")]
print("python" in data)     # True
print(2 in data[1])         # True
print(3 in data[2])         # True
print(ord("h") in data[3])  # True   # ASCII match
print(ord("o") in data[4])  # True

'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions,
       coding practices, and use in / not in with sequences (string, list, tuple, set, dict, range) 

A. EASY(Beginner-friendly conceptual clarity):
-----------------------------------------------
1. Check if a given character exists in a word using in
2. Check if a number exists inside a predefined list of valid IDs using in
3. Verify if a given subject name is not part of a list of restricted subjects using not in

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
4. Validate if a username exists in a list of registered users using in, and print a welcome message if found
5. Check if a product code is present in a list of available products; if not found using not in, print “Out of stock”
6. Given a sentence, check whether a specific keyword exists in it using in and print whether the sentence is relevant or not

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
7. In an e-commerce app, validate if a coupon code exists in a list of active coupons; if present using in, apply discount, otherwise show “Invalid coupon”
8. In a school system, check if a roll number exists in a list of students who paid fees; if the roll number is not in that list, print a reminder message
9. In an access control system, check if a given role (like "admin") is present in a list/tuple of allowed roles; if the role is in the list, grant access, else deny with a proper message
'''
