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
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S.No | Scenario                        | Code Example           | Object Relation                                                      | Value Comparison (==) | Identity Comparison (is)     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | Different values                | x = 10    y = 15       | Different objects in memory                                          | False                 | False                        |
| 2    | Same value, created separately  | x = 10    y = 10       | Same value but may be different objects (depends on integer caching) | True                  | False (if different objects) |
| 3    | Same value, same reference      | x = y = 10             | Both variables point to the same object                              | True                  | True                         |
| 4    | Python small integer caching    | a = 100   b = 100      | Reused cached object (0–256)                                         | True                  | True                         |
| 5    | Large integers (no caching)     | a = 1000  b = 1000     | Separate objects in memory                                           | True                  | False                        |
| 6    | Mutable objects (lists)         | x = [1,2]  y = [1,2]   | Same value but different list objects                                | True                  | False                        |
| 7    | Mutable aliasing                | x = [1,2]  y = x       | Both point to the same list                                          | True                  | True                         |
| 8    | None check (identity preferred) | x = None               | None is a singleton object                                           | N/A                   | x is None → True             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

'''

# Examples:

# Case 1: Different Values
print("Case 1: Different Values ")
x = 10
y = 15
'''
      x -----> 10  (id: 22323)
      y -----> 15  (id: 32432)
'''

print("Result : ", x == y)  #  False
print("Result : ", x is y)  # False
print("------------------------------------")


# Case 2: (created in different memory blocks)
print("Case 2: Created in different memory blocks ")
x = 10
y = 10
'''
      x -----> 10  (id: 3243)
      y -----> 10  (id: 2333)
'''
print("------------------------------------")

# Case 3: (created in same memory blocks)
print("Case 3: Created in same memory blocks ")
x = 10
y = 10
'''
      x -----> 10  (id: 2345)
      y -----> 10  (id: 2345)
'''
print("Result : ", x == y)  #  True
print("Result : ", x is y)  #  True
print("------------------------------------")

# Case 4: (Aliasing)
print("Case 4: Aliasing ")
x = y = 10

'''
      10  (id: 3243)
     /   \
     x    y  
'''
print("Result : ", x == y)  #  True
print("Result : ", x is y)  # True
print("------------------------------------")


'''
# BEST PRACTICES:
=================

|-----------------------------------------------------------------------------------------------------------------------------|
| S.No | Use Case         | When to Use ==                          | When to Use is                                          |
|-----------------------------------------------------------------------------------------------------------------------------|
| 1    | Value comparison | Compare numbers, strings, list contents | Not recommended                                         |
| 2    | Memory identity  | Not applicable                          | When checking if two variables refer to the same object |
| 3    | None check       | Avoid using == None                     | Always use `is None` or `is not None`                   |
| 4    | Mutable objects  | Compare contents (`==`)                 | Check reference equality (same object)                  |
|-----------------------------------------------------------------------------------------------------------------------------|

# DO's & DONT's:
================

|----------------------------------------------------------------------------------------------------|
| S.No | Do                                             | Don’t                                      |
|----------------------------------------------------------------------------------------------------|
| 1    | Use `is None` for null checks                  | Don’t use `== None`                        |
| 2    | Use `is` for checking object identity          | Don’t use `is` for numeric equality        |
| 3    | Use `is` to detect aliasing in mutable objects | Don’t assume equal values mean same object |
| 4    | Use `is not` to verify separate objects        | Don’t compare strings using `is`           |
|----------------------------------------------------------------------------------------------------|


# SUMMARY:
===========

|-----------------------------------------------------------------------------|
| S.No | Concept         | Explanation                                        |
|-----------------------------------------------------------------------------|
| 1    | ==              | Compares values/content                            |
| 2    | is              | Compares object memory identity                    |
| 3    | Python caching  | Small integers (0–256) and some strings are cached |
| 4    | Mutable objects | Lists/sets/dicts usually create separate objects   |
| 5    | None checking   | `None` is a singleton; always use `is`             |
|-----------------------------------------------------------------------------|

|-----------------------------------------------------------------------------------------------------------------------------|
| S.No | Topic                | Rule / Best Practice / Summary Point                                                          |
|-----------------------------------------------------------------------------------------------------------------------------|
| 1    | Value Comparison     | Use `==` to compare values of numbers, strings, lists, tuples, etc.                           |
| 2    | Memory Identity      | Use `is` to check if two variables refer to the same object in memory.                        |
| 3    | None Checking        | Always use `is None` or `is not None`; avoid using `== None`.                                 |
| 4    | Immutable Objects    | For numbers and strings, `==` checks value; `is` should not be used for equality.             |
| 5    | Mutable Objects      | Use `==` to compare contents; use `is` to detect aliasing (same list/dict object).            |
| 6    | Python Caching       | Python caches small integers (0–256) and some strings, causing `is` to return True sometimes. |
| 7    | Avoiding Misuse      | Do not assume equal values imply identical objects (`a == b` does not mean `a is b`).         |
| 8    | Recommended Use      | Use `is` only for identity checks and `None` checks, not for regular equality comparisons.    |
| 9    | Good Coding Practice | Prefer `is not` to verify two variables are not referring to the same object.                 |
|-----------------------------------------------------------------------------------------------------------------------------|


'''

'''
EXERCISES:  
===========
Write programs for below requirements:
Note:  While writing program, take your own scenario, follow naming conventions,
       coding practices, and use is / is not (and optionally ==) to show identity vs equality

A. EASY(Beginner-friendly conceptual clarity):
-----------------------------------------------
1. Create two integer variables with different values and print results of x == y and x is y
2. Create two string variables with the same text but assigned separately and print results of s1 == s2 and s1 is s2
3. Assign a variable to None and write a program that checks if the variable is None before using it

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
4. Create a list, assign it to another variable (alias), and show that a is b is True while modifying one affects the other
5. Create two separate lists with the same elements and show that list1 == list2 is True but list1 is list2 is False
6. Write a function that returns None in some cases and a value in other cases, and in the caller use is None and is not None to decide what to print

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
7. Simulate a small caching example using integers: create two variables with the same small integer value and two with the same large integer value, print their ids and compare using both == and is, then display observations
8. In a class based system (for example Employee), create two references pointing to the same object and another independent object; compare them using == and is to decide whether they represent the same employee instance or not
9. Design a resource loader where a configuration object is initially set to None and later loaded; process the configuration only if config is not None, otherwise print a clear message that configuration is missing
'''
