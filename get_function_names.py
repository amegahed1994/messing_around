# Code that extracts all functions name from an imported module

import sample_module
from inspect import getmembers, isfunction

# List containing function names (str)
functions_name = [member[0] for member in getmembers(sample_module) if isfunction(member[1])]

# Pro: dynamically access all function names
# Cons: need to import module before using getmembers
