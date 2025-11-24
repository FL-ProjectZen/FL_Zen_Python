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
BITWISE OPERATORS (Integrated with Binary Concepts): 
=====================================================
 - Bitwise operators operate directly on binary representation of integers.
 - Computers store numbers, text, images, audio, video — everything — ultimately in binary (0s and 1s).

So to truly understand bitwise operators, learners must first understand Decimal ↔ Binary conversions.

Decimal → Binary Conversion: 
----------------------------
Integer  : 137
Convert to binary ===>  
                     2 | 137
                     2 |  68  - 1
                     2 |  34  - 0
                     2 |  17  - 0 
                     2 |   8  - 1 
                     2 |   4  - 0
                     2 |   2  - 0
                       |   1  - 0     

Binary format = 1000 1001

Binary to Decimal:
------------------
Given Binary Number        :  1  0  0  0  1  0  0  1
Positions (right to left)  :  7  6  5  4  3  2  1  0
                             2  2  2  2  2  2  2  2
-----------------------------------------------------
Powers of 2                : 128 64 32 16  8  4  2  1
-----------------------------------------------------
Wherever 1 exists, pick value:
                             : 128 + 8 + 1  
                             = 137

Everything in computers — Text files, Zip files, Images, Audio, Videos — is ultimately stored in binary format.

Bitwise AND in Maths: 
---------------------
  1100   (12)
& 1010   (10)
-------
  1000   (8)

Bitwise AND in Python: 
---------------------
a = 12
b = 10
print(a & b)   # 8

Bitwise OR in Maths: 
---------------------
  1100
| 1010
------
  1110   (14)

print("------ Bitwise OR Example ------")

a = 12
b = 10

print( a | b )  # 14

1's Compliment : 
-----------------
Flip every bit:
0 → 1
1 → 0

Input :  1010 
1’s Complement:  0101



2's Compliment : 
-----------------
 - Take the 1’s complement (flip bits). Add 1 to the result

Input : 13 → 0000 1101
 
13 : 0000 1101
     1111 0010   ← 1’s complement

2's Compliment :
    1111 0010
    +       1
    -----------
    1111 0011   ← 2’s complement = -13


'''
# Requirement : Demonstrate Bitwise Operators (Python + Real Life Meaning)
print("--------------------------------------------------------")

# 1 : Bitwise AND
print("Example 1 : Bitwise AND – Permission Check")

# STATE
READ  = 1   # 0001
WRITE = 2   # 0010
user_perm = 3   # 0011  (User has READ + WRITE)

# BEHAVIOR
can_read = (user_perm & READ) != 0
can_write = (user_perm & WRITE) != 0

# DISPLAY
print("User Permissions :", user_perm)
print("Can Read?        :", can_read)
print("Can Write?       :", can_write)
print("--------------------------------------------------------")

# 2 : Bitwise OR
print("Example 2 : Bitwise OR – Combining Features")

# STATE
feature_A = 1   # 0001
feature_B = 4   # 0100

# BEHAVIOR
enabled_features = feature_A | feature_B   # 0101

# DISPLAY
print("Feature A :", feature_A)
print("Feature B :", feature_B)
print("Enabled Features (A OR B) :", enabled_features)
print("--------------------------------------------------------")

# 3 : Bitwise XOR
print("Example 3 : Bitwise XOR – Detecting Changes")

# STATE
old_flags = 10   # 1010
new_flags = 6    # 0110

# BEHAVIOR
difference = old_flags ^ new_flags   # Bits that changed

# DISPLAY
print("Old Flags :", old_flags)
print("New Flags :", new_flags)
print("Changed Bits (XOR) :", difference)
print("--------------------------------------------------------")

# 4 : Bitwise NOT
print("Example 4 : Bitwise NOT – Inverting Bits")

# STATE
x = 10   # 1010

# BEHAVIOR
result = ~x   # Two's complement => -(x+1)

# DISPLAY
print("Original :", x)
print("After ~  :", result)
print("--------------------------------------------------------")

# 5 : Left Shift
print("Example 5 : Left Shift – Fast Multiplication")

# STATE
x = 5   # 0101

# BEHAVIOR
shifted = x << 1   # Multiply by 2 → 0101 << 1 = 1010 = 10

# DISPLAY
print("Original Value :", x)
print("After x << 1   :", shifted)
print("--------------------------------------------------------")


# 6 : Right Shift
print("Example 6 : Right Shift – Fast Division")

# STATE
x = 40   # 101000

# BEHAVIOR
shifted = x >> 3   # Divide by 2³ → 40 / 8 = 5

# DISPLAY
print("Original Value :", x)
print("After x >> 3   :", shifted)
print("--------------------------------------------------------")

'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY(Beginner-friendly conceptual clarity):
-----------------------------------------------
1. Use bitwise AND (&) to check whether a number is even (hint: num & 1)
2. Use bitwise OR (|) to combine two simple flags (for example, READ and WRITE) and print the final permission value
3. Use bitwise XOR (^) to compare two numbers and print whether any bit differs between them

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
4. Given a number, turn ON a specific bit position using bitwise OR (|) and print the updated value
5. Given a number, turn OFF a specific bit position using bitwise AND (&) with a mask and print the updated value
6. Given a number, left shift it by 1 and 2 positions using (<<) and show how the value changes (interpret as fast multiplication)

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
7. Design a small permission system: READ = 1, WRITE = 2, EXECUTE = 4. For a given user_perm value, use bitwise AND (&) to check and print which permissions the user has
8. Use XOR (^) to "encrypt" a small integer value with a secret key and then "decrypt" it back using the same key (show both steps)
9. Use right shift (>>) operations to simulate dividing a file size (in bytes) into chunks of power-of-2 sizes and print how many chunks you get after each shift

'''