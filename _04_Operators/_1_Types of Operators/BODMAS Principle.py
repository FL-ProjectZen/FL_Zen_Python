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
BODMAS Principle:
===================
BODMAS stands for:
    B – Brackets
    O – Orders (Powers, Exponents)
    D – Division
    M – Multiplication
    A – Addition
    S – Subtraction

 - BODMAS decides which operator executes first when multiple operations appear inside the same expression.
 - This ensures predictable, consistent results regardless of code complexity.

Order of Execution:
--------------------
    -  B   : Python ALWAYS resolves brackets first, no matter what’s inside them.
    -  E   : Exponents (**) are evaluated before division/multiplication.
    -  DFM : Division (/, //, %) and multiplication (*) come next and share equal priority—Python evaluates them left to right.
    -  AS  : Addition (+) and subtraction (-) follow—also left to right.

Mixing many operations without parentheses reduces readability—using brackets is a professional coding practice.
BODMAS is important in real-world calculations like billing, tax computation, scientific formulas, and financial logic.
Wrong precedence leads to wrong outputs, making scenario analysis & testing essential.

'''
# Examples:

'''
|---------------------------------------------------------------------------------------------|
| S.No | Expression           | Step by Step Execution                               | Output |
|---------------------------------------------------------------------------------------------|
| 1    | `10 + 20 * 3`        | `20 * 3 = 60` → `10 + 60 = 70`                       | `70`   |
| 2    | `(10 + 20) * 3`      | `(10 + 20) = 30` → `30 * 3 = 90`                     | `90`   |
| 3    | `5 + 2 ** 3`         | `2 ** 3 = 8` → `5 + 8 = 13`                          | `13`   |
| 4    | `100 + 20 * 3 / 5`   | `20 * 3 = 60` → `60 / 5 = 12` → `100 + 12 = 112`     | `112`  |
| 5    | `(50  5) ** 2 / 5`   | `(50  5) = 45` → `45 ** 2 = 2025` → `2025 / 5 = 405` | `405`  |
| 6    | `(25 % 4) * (10  3)` | `25 % 4 = 1` → `(10  3) = 7` → `1 * 7 = 7`           | `7`    |
|---------------------------------------------------------------------------------------------|

'''
