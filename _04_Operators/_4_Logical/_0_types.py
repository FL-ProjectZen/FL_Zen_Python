"""_0_types.py"""

'''

Logical Operators:
==================

| ------------ | --------------------- | -------------------------------------- | ----------------------------- | ---------------------------- | ---------- | ----------------------------------------------------------- |
| Operator     | Name                  | Purpose (Simple Meaning)               | Mathematical Analogy          | Python Example               | Output     | Real-World Use Case                                         |
| ------------ | --------------------- | -------------------------------------- | ----------------------------- | ---------------------------- | ---------- | ----------------------------------------------------------- |
| and          | Logical AND           | True only if BOTH conditions are true  | (5 > 3) AND (8 > 2) → True    | (10 > 5) and (3 < 8)         | True       | Login with username & password, multi-condition filters     |
| or           | Logical OR            | True if ANY ONE condition is true      | (5 > 10) OR (8 > 2) → True    | (4 == 4) or (7 < 3)          | True       | Discount eligibility, fallback logic, access checks         |
| not          | Logical NOT           | REVERSES the Boolean value             | NOT(True) → False             | not(5 > 2)                   | False      | Validation negation, feature disabling, inverse conditions  |
| ------------ | --------------------- | -------------------------------------- | ----------------------------- | ---------------------------- | ---------- | ----------------------------------------------------------- |

Truth Table for Logical Operators:
==================================
| ---------------- | ------------------ | ------------------------------- | ----------------------------- | ---------------------------- |
| Expression       | Operator Used      | Evaluation Logic                | Example                       | Output                       |
| ---------------- | ------------------ | ------------------------------- | ----------------------------- | ---------------------------- |
| True and True    | Logical AND        | Both values must be True        | True and True                 | True                         |
| True and False   | Logical AND        | One value is False              | True and False                | False                        |
| False and True   | Logical AND        | One value is False              | False and True                | False                        |
| False and False  | Logical AND        | Both are False                  | False and False               | False                        |
| ---------------- | ------------------ | ------------------------------- | ----------------------------- | ---------------------------- |
| True or True     | Logical OR         | At least one value True         | True or True                  | True                         |
| True or False    | Logical OR         | One value True                  | True or False                 | True                         |
| False or True    | Logical OR         | One value True                  | False or True                 | True                         |
| False or False   | Logical OR         | Both are False                  | False or False                | False                        |
| ---------------- | ------------------ | ------------------------------- | ----------------------------- | ---------------------------- |
| not True         | Logical NOT        | Reverses Boolean value          | not True                      | False                        |
| not False        | Logical NOT        | Reverses Boolean value          | not False                     | True                         |
| ---------------- | ------------------ | ------------------------------- | ----------------------------- | ---------------------------- |

'''