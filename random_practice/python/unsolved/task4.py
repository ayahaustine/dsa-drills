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


#######################################################################################

# Possible solution 1

from sympy import symbols, Eq, And, Or, Not, Xor
from sympy.logic.inference import satisfiable

# Define symbols for houses
houses = 3
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
constraints.append(And(
    Eq(house_owners[0], canadian),
    Eq(house_owners[1], american),
    Eq(house_owners[2], japanese),
))

# each nationality is assigned to exactly one house
constraints.append(And(
    Xor(house_owners[0] == canadian, house_owners[1] == canadian, house_owners[2] == canadian),
    Xor(house_owners[0] == american, house_owners[1] == american, house_owners[2] == american),
    Xor(house_owners[0] == japanese, house_owners[1] == japanese, house_owners[2] == japanese),
))

# 1:1 house:colour
# each house is assigned one colour
constraints.append(And(
    Eq(house_colours[0], blue),
    Eq(house_colours[1], green),
    Eq(house_colours[2], red),
))

# each colour is assigned to one house
constraints.append(And(
    Xor(house_colours[0] == blue, house_colours[1] == blue, house_colours[2] == blue),
    Xor(house_colours[0] == green, house_colours[1] == green, house_colours[2] == green),
    Xor(house_colours[0] == red, house_colours[1] == red, house_colours[2] == red),
))

# 1:1 house:drink
# each house is assigned one drink
constraints.append(And(
    Eq(house_drinks[0], coffee),
    Eq(house_drinks[1], milk),
    Eq(house_drinks[2], tea),
))

# each drink is assigned to one house
constraints.append(And(
    Xor(house_drinks[0] == coffee, house_drinks[1] == coffee, house_drinks[2] == coffee),
    Xor(house_drinks[0] == milk, house_drinks[1] == milk, house_drinks[2] == milk),
    Xor(house_drinks[0] == tea, house_drinks[1] == tea, house_drinks[2] == tea),
))

# the blue house has milk
constraints.append(Eq(house_drinks[0], milk))

# only the Canadian owns the house which has coffee
constraints.append(Eq(house_owners[house_drinks.index(coffee)], canadian))

# Combine constraints into one logical expression using And
combined_constraints = And(*constraints)

# Check satisfiability
result = satisfiable(combined_constraints)

def print_result(result):
    for house in range(len(house_colours)):
        print(f"House {house + 1}:")
        print(f"  Owner: {result[house_owners[house]]}")
        print(f"  Colour: {result[house_colours[house]]}")
        print(f"  Drink: {result[house_drinks[house]]}\n")

if result: 
    print_result(result)
else:
    print("No solution found")


############################################################################

# Possible solution 2

from sympy import symbols, Eq, And, Or
from sympy.logic.inference import satisfiable
import itertools

# Help function to define uniqueness among symbols
def unique_symbols(*args):
    return And(*[Or(*[Eq(a, b) for a in args]) for b in args])

def print_result(result):
    # Convert result to str and parse using regex for better readability
    result_str = str(result)
    for colour, owner, drink in itertools.product(colours, nationalities, drinks):
        if result[colour] and result[owner] and result[drink]:
            house_number = re.search(f"{colour}.(\d)", result_str).group(1)
            print(f"House {house_number}: Colour {colour}, Owner {owner}, Drink {drink}")

# Define number of houses
houses = 3

# Define symbols for houses
house_colours = symbols(f'house_colour:{houses}')
house_owners = symbols(f'house_owner:{houses}')
house_drinks = symbols(f'house_drink:{houses}')

# Specific entities
colours = (blue, green, red) = symbols('blue green red')
nationalities = (canadian, american, japanese) = symbols('canadian american japanese')
drinks = (coffee, milk, tea) = symbols('coffee milk tea')

constraints = []

# 1:1 house:nationality
# each house owned by one nationality
for house_owner in house_owners:
    constraints.append(unique_symbols(*[house_owner == nationality for nationality in nationalities]))

# each nationality is assigned to exactly one house
for nationality in nationalities:
    constraints.append(unique_symbols(*[house_owner == nationality for house_owner in house_owners]))

# 1:1 house:colour
# each house is assigned one colour
for house_colour in house_colours:
    constraints.append(unique_symbols(*[house_colour == colour for colour in colours]))

# each colour is assigned to one house
for colour in colours:
    constraints.append(unique_symbols(*[house_colour == colour for house_colour in house_colours]))

# 1:1 house:drink
# each house is assigned one drink
for house_drink in house_drinks:
    constraints.append(unique_symbols(*[house_drink == drink for drink in drinks]))

# each drink is assigned to one house
for drink in drinks:
    constraints.append(unique_symbols(*[house_drink == drink for house_drink in house_drinks]))

# the blue house has milk
constraints.append(unique_symbols(*[Eq(house_colour == blue, house_drink == milk) for house_colour, house_drink in zip(house_colours, house_drinks)]))

# only the canadian owns the house which has coffee
constraints.append(unique_symbols(*[And(house_owner == canadian, house_drink == coffee) for house_owner, house_drink in zip(house_owners, house_drinks)]))

# Combine constraints into one logical expression using And
combined_constraints = And(*constraints)

# Check satisfiability
result = satisfiable(combined_constraints)
if result:
    print_result(result)
else:
    print("No solution found")