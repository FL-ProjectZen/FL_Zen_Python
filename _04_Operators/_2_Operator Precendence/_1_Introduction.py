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
Operator Precedence:
====================
    - Python follows precedence, then associativity (left → right)
    - Using parentheses is always a good engineering habit—makes code readable and avoids wrong calculations
    - Division, floor division, modulus, and multiplication all share equal priority and execute left→right
    - Precedence errors are a common cause of incorrect billing, discount, and interest calculations in real projects


Python Operator Precedence (High → Low):
=========================================

|-----------------------------------------------------------|
| S.No | Precedence Level                  | Operators      |
| ----------------------------------------------------------|
| 1    | Parentheses                       | ()             |
| 2    | Exponent                          | **             |
| 3    | Unary Operators                   | +x , -x , ~x   |
| 4    | Multiplication / Division Group   | * , / , // , % |
| 5    | Addition / Subtraction            | + , -          |
| 6    | Comparison Operators              | < , <= , > , >=|
| 7    | Equality Operators                | == , !=        |
| 8    | Logical NOT                       | not            |
| 9    | Logical AND                       | and            |
| 10   | Logical OR                        | or             |
|-----------------------------------------------------------|

- Try to remember order like this 
    1. Parentheses
    2. Arithmetic : MD / AS 
    3. Equality 
    4. Logical
    
    Above operators we will use very frequently.

Examples:

|----------------------------------------------------------------------------------------------------|
| S.No | Expression                   | Step by Step Execution                                                      | Output |
|----------------------------------------------------------------------------------------------------|
| 1    | 10 + 20 * 2                  | 20 * 2 = 40 → 10 + 40 = 50                                                   | 50     |
| 2    | (5 + 5) * 3                  | (5 + 5) = 10 → 10 * 3 = 30                                                   | 30     |
| 3    | 4 + 3 ** 2                   | 3 ** 2 = 9 → 4 + 9 = 13                                                      | 13     |
| 4    | 100 / 5 + 6 * 2              | 100 / 5 = 20 → 6 * 2 = 12 → 20 + 12 = 32                                     | 32     |
| 5    | (50 - 10) / 2 + 3 ** 2       | (50 - 10) = 40 → 40 / 2 = 20 → 3 ** 2 = 9 → 20 + 9 = 29                      | 29     |
| 6    | 20 % 6 * (8 - 3)             | 20 % 6 = 2 → (8 - 3) = 5 → 2 * 5 = 10                                        | 10     |
| 7    | (25 // 4) ** 2 - 10 * 3      | 25 // 4 = 6 → 6 ** 2 = 36 → 10 * 3 = 30 → 36 - 30 = 6                        | 6      |
| 8    | 100 / (5 + 5) * 3 ** 2       | (5 + 5) = 10 → 100 / 10 = 10 → 3 ** 2 = 9 → 10 * 9 = 90                      | 90     |
| 9    | (50 - 5 * 3) ** 2 / 5        | 5 * 3 = 15 → 50 - 15 = 35 → 35 ** 2 = 1225 → 1225 / 5 = 245                  | 245    |
|----------------------------------------------------------------------------------------------------|


'''
