# Hi, this is an example of an ideal code corresponding to all PEP-8 guidelines.

# Important: You should have not more than 79 characters per line. 79 is the limit.

# Important: Variables and function names CAN'T contain ANY uppercase letters. No matter what other 'teachers' say!
# You need to use lowercase letters and separate words with underscores '_' . This type is called a snake_case.

# First of all you need to write the documentation of the file. Then keep one blank line.
# And yes, comments can be more than one line.
"""
This is my documentation
"""

# (Optional) Then you need to write "from __future__ import module_name" the special import statement in Python 2
# that enables a feature from Python 3 to be used in the current Python 2 code. (In Python 3, the
# from __future__ import unicode_literals import is not required.) After this import keep one blank line.
from __future__ import unicode_literals

# (Optional) Module level “dunders” (i.e. names with two leading and two trailing underscores)
# such as __all__, __author__, __version__, etc. should be placed after the module docstring but
# before any import statements except from __future__ imports. Then keep one blank line.
__all__ = ['summarizer', 'parser']
__version__ = '1.1'
__author__ = 'Armen-Jean Andreasian'

# After doc-strings come special imports (optional), then dunders (optional), then import statements.
# The sequence of imports is following: built-in (standard) libraries, 3rd party libraries, local files/functions
# First comes the full import (import library), then partial (from library import function)
# Between each group of imports keep one blank line.
import this  # to read the bible of Python
import os
from typing import Any

import requests

from sample_script import my_function

# After imports come constant variables, and variables with a value that is not intended to be modified.
URL = 'https://www.google.com'
pi_number = 3.14


class MyClass:
    """
    This is a sample class that follows PEP 8 guidelines.
    ...
    """

    def __init__(self):
        # Initialize class variables or attributes here.
        self.name = "MyClass"
        self.count = 0

    def my_method(self):
        # Define class methods here.
        self.count += 1
        print(f"Hello from {self.name}! Count: {self.count}")


# Place the class and its call at the appropriate position in the code.
my_object = MyClass()
my_object.my_method()


# After the constant variable(s) come function definitions.
# Keep two break lines before and after function definitions.
# Also, you can use blank lines between the comments to separate them.
# However, it does recommend using comments sparingly and keeping them concise.

# In the function definition below, I show you how to document the function, and also
# that's good to separate each logical iteration by a blank line.
def parser(url, filepath='C:\\Users\\User\\Desktop\\file.txt'):
    """
    Downloads the content from the given URL and saves it to the specified file path.

    Args:
        url (str): The URL of the content to download.
        filepath (str): The file path where the content will be saved. Defaults to 'C:\\Users\\User\\Desktop\\file.txt'.

    Returns:
        str: The absolute path of the saved file.

    Raises:
        None

    """
    # NEVER use comments for documenting functions, classes, and modules in Python. Docstrings  are used
    # to generate documentation automatically, can be accessed at runtime through the "__doc__" attribute, and
    # can be formatted and processed by various tools.
    # Docstrings are for documenting, comments are for commenting.
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    else:
        exit()

    response = requests.get(url)
    content = response.text

    with open(filepath, 'w') as file:
        file.write(content)

    return os.path.abspath(filepath)


# Only assignments related to a particular function immediately following that function's definition.
# Don't forget to keep two blank lines before and after the assignment(s).
parser_result = parser(URL)


def summarizer(var_one, var_two, var_three,
               var_four, var_five, var_six) -> list[Any]:  # "->" is called a function annotation. It's a hint.
    # in the arguments of a function should not have any additional spaces, except for one space that comes
    # after a comma.
    print(var_one, var_two, var_three, var_four,
          var_five, var_six)  # Inline comments should be placed at least two spaces from the statement.

    return sum([var_one, var_two, var_three,
                var_four, var_five, var_six])


# After function definitions come assignments with dependencies. Import-assignments in rough terms.
# Keep one blank line after them.
number_zero = my_function()

# After assignments with dependencies come function calls. With multiple variables in this case.
# Function calls, just like any containers are better to break the line after the opening bracket,
# and also before the closing bracket ], }, or ).
result = summarizer(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# After function calls come the rest of variable assignments. Local assignments, in rough terms.
# Between variables containing multiple elements should be kept ONLY one blank line.
# Pay attention that we have a trailing-comma after the last item "6" of "my-list".
# Having trailing-commas is optional. However, if you use it, remember to add one whitespace/break line after it.
my_list = [
    1, 2, 3,
    4, 5, 6,
]
# Important note!
my_new_variable = 2 * pi_number

# Assigning variables should be explicit. It's not recommended to assign multiple variables in one line.
# As a tip I demonstrate you the alternative way of writing long numbers. 100_000 = 100000, it's just more readable.
gross_wages = 100_000
dividends = 2_000
taxable_interest = 1000
qualified_dividends = 150000

# After variables come expression assignments.
# Always break the line before a binary operator.
income = (
    gross_wages
    + taxable_interest
    + (dividends - qualified_dividends)
)
# Binary operators are:
# Arithmetic Operators,Comparison Operators, Assignment Operators, Logical Operators,
# Bitwise Operators, Membership Operators, Identity Operators.

multiplicative = gross_wages*qualified_dividends  # According to PEP 8, there should not be a space around the "*".

# After the last line of the code you should keep one break line.
