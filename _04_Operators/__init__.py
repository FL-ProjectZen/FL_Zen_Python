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
PAREPRAE CHATPER LEVEL SUMMARY HERE 

OPERATORS: CHAPTER LEVEL EXERCISES : 
==================================
Note:  While writing program, take your own scenario, follow naming conventions, coding practices 

A. EASY: (Beginner-friendly conceptual clarity)
------------------------------------------------
1. Take two numbers a and b, compute sum, difference and product using arithmetic operators, then check if the result is greater than 0 using comparison, and print a message using logical and
2. Read a student name and marks; calculate total and average using arithmetic operators, compare average with pass_marks using comparison, and print whether the student passed or failed using a logical expression
3. Create a list of three product prices, calculate total_cost, apply a fixed discount using -= assignment, then check if total_cost is in a given budget range using comparison and logical operators
4. Define a string city and a list of metro_cities; use membership (in, not in) to check if city is a metro, and also compare length of city name with a threshold using arithmetic and comparison operators
5. Create two variables x and y pointing to the same integer using assignment; print results of x == y and x is y, then change y using an arithmetic assignment operator (+=) and show how equality and identity results change

B. MEDIUM: (Deeper logic, multi-condition understanding)
--------------------------------------------------------
6. Build a small shopping bill where you calculate subtotal using arithmetic on item quantities and prices, apply tax and discount using arithmetic and assignment operators, then check if final_amount is within a valid range using comparison and logical operators, and whether coupon_code is in a list of valid coupons using membership
7. Create a simple grading system: compute percentage from marks in 3 subjects using arithmetic, assign a grade using comparison and logical operators (and, or), then verify that the grade string is in a list of allowed_grades before printing the result
8. Simulate a login check where username and role are given: verify that username is in a list of active_users, role is in allowed_roles, and account_status is not "blocked" using comparison, logical and membership operators; also use identity (is, is not) to check if a session object is None before granting access
9. Create two lists: completed_tasks and required_tasks; compute counts using arithmetic, compare counts, check if all required_tasks are present in completed_tasks using membership and logical operators, then print whether the user is eligible for a reward
10.Implement a small bank balance check where you start with an initial balance, apply deposit and withdrawal using arithmetic and assignment operators, then compare balance with minimum_balance using comparison, and use logical operators to decide whether to show “active account” or “low balance warning”

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
11. Design a payroll program that calculates gross_salary (basic + hra + allowances), net_salary (after deductions and tax) using arithmetic and assignment operators; then check using comparison and logical operators whether the employee is eligible for bonus (based on net_salary and years_of_experience) and confirm that employee_id is in the active_employee_ids list using membership
12. Build a course enrollment validator where you compute total_credits from selected_courses, ensure total_credits is within min and max credit limits using comparison, check that each selected course code is in available_courses using membership, and use logical operators to decide whether enrollment_status is “approved” or “rejected”; also use identity to check if advisor_approval is None before final approval
13. Create an inventory management mini-program: for a given product, update stock using arithmetic and assignment operators based on purchase and sale counts, check if stock is below reorder_level using comparison, verify that product_id is in active_products and not in discontinued_products using membership and logical operators, then print appropriate status messages
14. Simulate a trip planner: calculate total_distance, fuel_required and total_cost using arithmetic operators, apply discounts or surcharges using assignment operators, check multiple conditions like distance range, budget, and passenger_count using comparison and logical operators, and ensure selected_destination is in allowed_destinations before confirming the trip
15. Implement a simplified user session manager: start with session = None, create a session object when login is successful, use identity operators (is, is not) to check session state, update last_login_count using arithmetic and assignment operators, validate that user_role is in permitted_roles and account_status is not "suspended" using comparison, membership and logical operators, then print whether the session is active or terminated
"""

"""
OPERATORS: CHAPTER LEVEL INTERVIEW QUESTIONS :
===============================================

A. EASY: (Beginner-friendly conceptual clarity)
------------------------------------------------
1. What is the difference between /, //, and % when dividing numbers, and when would you use each in programs?
2. Explain how operator precedence affects expressions like 2 + 3 * 4. Which part executes first?
3. Why is a == b different from a is b? Give a simple example using integers or strings.
4. How are logical operators (and, or, not) used to combine multiple conditions? Provide a simple real-world example.
5. What is the purpose of assignment operators like += or *=? How do they simplify updating a variable?

B. MEDIUM: (Deeper logic, multi-operator understanding)
-------------------------------------------------------
6. How do arithmetic and comparison operators work together in scenarios like validating totals, computing grades, or calculating thresholds?
7. Why is using in or not in for membership checks more readable and safer than multiple equality comparisons?
8. Explain how operator precedence plays a role in expressions like (a * b + c) > (d / e) and how parentheses can change the outcome.
9. In what situations does Python's logical short-circuiting help avoid unnecessary computation or errors?
10. What happens when you mix arithmetic (+, *), assignment (+=), and membership operators (in) in the same workflow? Explain with an example.

C. DIFFICULT: (Advanced reasoning + real engineering logic)
-----------------------------------------------------------
11. How do operator combinations drive business formulas like payroll processing (basic + hra – deductions) or tax computation?
12. Explain how identity checks (is None, is not None) help avoid bugs in API handling, database lookups, or optional parameters.
13. When working with analytics, how do arithmetic transformations (sum, mean, scale, normalize) rely on different operators?
14. How would you debug a complex expression containing arithmetic, comparison, and logical operators, especially when the output is unexpected?
15. How do you choose between **, *, +, and % when designing a multi-step computation pipeline (e.g., scoring model, ranking engine, pricing engine)?
"""