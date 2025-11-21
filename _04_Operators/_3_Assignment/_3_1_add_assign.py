"""_3_1_add_assign.py"""

# Requirement : Demonstrate assignment (=) and add & assign (+=) operators

# ADD & ASSIGN OPERATOR (+=)

print("------ Add & Assign Operator (+=) ------")

# STATE
counter = 0

# BEHAVIOR
counter = counter + 10     # Long Form
print("Counter after long form (counter = counter + 10):", counter)

counter += 10              # Short Form (preferred)
print("Counter after short form (counter += 10):", counter)


# Ex 2 : Score Update

print("------ Using += Operator for Score Update ------")

# STATE
score = 100

# BEHAVIOR
score += 50   # increase score

# DISPLAY
print("Updated Score :", score)


# Ex 3 : Shopping Cart Quantity Update

print("------ Shopping Cart Quantity Update using += ------")

# STATE
cart_items = 5

# BEHAVIOR
cart_items += 3   # customer added 3 more items

# DISPLAY
print("Total Items in Cart :", cart_items)


'''You can practice 1 example each for all remaining operators '''