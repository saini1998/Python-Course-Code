#import ecommerce.sales
from ecommerce.shopping import sales
# Creating Modules

# from sales import calc_tax, calc_shipping
import sys

sales.calc_shipping()
sales.calc_tax()


# Complied Python Files

# NOTE __pycache__
# complied versions of modules in our program like sales.py
# speeds up module loading
# It checks the date time of compiled versions and source code


# Module Search Path

print(sys.path)


# Packages


# Sub Packages


# Intra Package Refrences


# The dir Function

print("\n")
print(dir(sales))
print(sales.__file__)
print(sales.__name__)
print(sales.__package__)


# Executing Modules as Scripts
