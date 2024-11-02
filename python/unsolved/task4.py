"""
The following code uses sympy to solve a simple logic problem.
There are 3 coloured houses, 3 nationalities of the owners, and 3 drinks for the houses 1 each.
The details and constraints are specified in the comments
but need to be completed as indicated by TODO: Complete this code to solve the puzzle: 
what owner owns which house and what drink is served in each?
"""


from sympy import symbols, Eq, And, Xor
from sympy.logic.inference import satisfiable
import re

# Define symbols for houses
house_colours = symbols(f'house_colour:{houses}')
house_owners = symbols(f'house_owner:{houses}')
house_drinks = symbols(f'house_drink:{houses}')

# Specific entities
colours = (blue, green, red) = symbols('blue green red')
nationalities = (canadian, american, japanese) = symbols('canadian american japanese')
drinks = (coffee, milk, tea) = symbols('coffee milk tea')

# now for constraints
constraints = []

# 1:1 house:nationality
# each house owned by one nationality
# TODO:

# each nationality  is assigned to exactly one house
# TODO:

# 1:1 house:colour
# each house is assigned one colour
# TODO:

# each colour is assigned to one house
# TODO:

# 1:1 house:drink
# each house is assigned one drink
# TODO:

# each drink is assigned to one house
# TODO:

# the blue house has milk
# TODO:

# only the canadian owns the house which has coffee
# TODO:

# Combine constraints into one logical expression using And
# TODO:

# Check satisfiability
result = satisfiable(combined_constraints)
if result: 
    print_result(result)
else:
    print("No solution found")