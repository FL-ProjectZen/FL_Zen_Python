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

"""
---------------------------------------------------------------------
Module    Chapter        Lecture
---------------------------------------------------------------------
Python    4.Operators	 1. Arithmetic Operators
---------------------------------------------------------------------

To Summarize: 
============
I. ADDITION (+) :
----------------- 
 - Addition combines two or more numeric values into a single total, matching mathematical “sum” behavior.
 - Handles various scenarios: count-based (2 numbers, 3 numbers), type-based (positive, negative, zero), and datatype-based (int + float → float).
 - Zero behaves neutrally — adding zero does not change the output, as reflected in multiple examples in _1_addition.py.
 - Addition is widely used in real-world problems like billing, bank balance updates, and shopping totals.
 - Supports scalable operations: multi-number additions, dynamic inputs, and cross-type arithmetic conversions.

II. SUBTRACTION (-) :
--------------------
 - Subtraction deducts the second value from the first and models “difference” behavior like in mathematics.
 - Zero has no effect when subtracted (40 - 0 = 40), which is explicitly covered in your subtraction exercises.
 - Subtraction often works with addition (like deposits and withdrawals) in real-world scenarios such as bank transactions and stock calculations.
 - Supports both integer and float operations and requires careful handling of negative values for correct sign outcomes.
 - Frequently used for calculations involving profit/loss, passenger updates, temperature changes, and warehouse inventory adjustments.

III. MULTIPLICATION (*) :
-------------------------
 - Multiplication repeats a value a certain number of times (mathematically equivalent to repeated addition).
 - Common real-world use: price × quantity, production counts, total capacity, or scaling amounts.
 - Works predictably with all numeric types — int, float, and mixed types — automatically promoting types when needed.
 - Often combined with addition/subtraction inside billing, tax, discount, and shopping calculations as seen in your addition real-world examples.
 - Zero multiplied with any number results in zero, making it useful for initializations and edge-case validations.
 
IV. DIVISION (/) :
-------------------
 - Normal division returns a floating-point value, matching real mathematical division behavior (e.g., 15 ÷ 4 = 3.75).
 - Used for splitting totals, calculating averages, cost per item, and distributing resources evenly.
 - Always returns float, even when dividing two integers, so type awareness is required.
 - Division errors must be handled carefully — especially division by zero, which is invalid.
 - Forms the foundation for arithmetic reasoning in business use cases like tax rates, discounts, and financial computations.
 
 V. MODULUS (%) :
 -----------------
 - Modulus returns the remainder after division (e.g., 25 % 4 = 1) as described in the operator table.
 - Widely used for cycle-based logic — clocks, rotations, periodic scheduling, and repeating patterns.
 - Essential for parity checks (even/odd), digit extraction, and hashing operations.
 - Forms the core of time-cycle calculations and remainder-based decisions in real engineering tasks.
 - Works across integer types cleanly; float modulus is allowed but typically used for numeric algorithms.
 
VI. FLOOR DIVISION (//) :
-------------------------
 - Floor division performs division and removes the decimal part, returning the integer floor value (e.g., 25 // 4 → 6).
 - Used for full-unit calculations: box packing, complete batches, full groups, and team formation counts.
 - Always returns the lower integer, even for negative results, aligning with mathematical floor behavior.
 - Useful when dealing with capacity planning, transport calculations, and chunking of data.
 - Often paired with modulus to split “full units” vs “remaining items” in distributed systems.
 
VII. EXPONENTIATION (**) :
--------------------------
 - Raises one value to the power of another (e.g., 2 ** 5 = 32) following mathematical exponent laws.
 - Fundamental for growth calculations: compound interest, exponential scaling, and scientific computations.
 - Powers and squares play a role in geometry, physics, machine learning formulas, and algorithmic complexity.
 - Built-in type handling allows both integer and floating-point exponentiation.
 - Used in advanced calculations such as computing bitstrings count (2ⁿ), population modeling, and statistical simulations.

BODMAS Principle:
------------------

"""

"""
LECTURE LEVEL EXERCISES : 
=========================
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
------------------------------------------------
1. Evaluate a + b, a - b, and a * b for a = 5, b = 3
2. Compute 10 / 2, 10 // 3, and 10 % 3 for any chosen values
3. For numbers x = 4, y = 2, calculate x ** y, x + y, and x - y

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
4. Given a list [10, 20, 30], compute the sum, average (sum/len), and modulus (sum % 7)
5. Using strings "Python" and "Code", compute their lengths, then derive (len1 + len2), (len1 * len2), and (len1 - len2)
6. For a = 7, b = 3, evaluate (a * b), (a + b), (a % b)

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
7. Using salary metrics: base = 45000, bonus = 8000, deductions = 5000
    Compute total = base + bonus - deductions and any other arithmetic variation you choose
8. For lists A = [2, 4, 6] and B = [3, 5, 7], 
    compute -> sumA, sumB, difference (sumB - sumA)
9. For a = 5, b = 2, compute
    expr1 = a ** b, expr2 = a * b, expr3 = a + b


LECTURE LEVEL INTERVIEW QUESTIONS :
====================================

A. EASY: (Beginner-friendly conceptual clarity)
------------------------------------------------
1. Explain how operators like +, -, and * are used to derive new values from existing variables
2. Describe how /, //, and % differ when used to divide or break down numbers
3. Explain how exponentiation (**) helps create derived values like powers or scaling factors

B. MEDIUM: (Deeper logic, multi-operator understanding)
-------------------------------------------------------
4. How does combining +, -, %, and // help in real-world scenarios like billing, splitting, and grouping data
5. Why might multiplying lengths of values change complexity, size, or behavior in an arithmetic computation
6. Explain how mixing operations like *, %, and + in the same expression relies on operator precedence

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
7. Explain how arithmetic formulas such as salary = base + bonus - deductions are used in business logic
8. How do arithmetic transformations like sum(list), diff(listB - listA), and scaling values help in analytics workloads
9. How would you decide whether to use **, *, or + when designing a calculation pipeline involving multiple steps
"""