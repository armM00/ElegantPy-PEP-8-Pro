"""
This is my documentation
"""

from __future__ import unicode_literals

__all__ = ['summarizer', 'parser']
__version__ = '1.1'
__author__ = 'Armen-Jean Andreasian'

import os
from typing import Any

import requests

from sample_script import my_function

URL = 'https://www.google.com'
pi_number = 3.14


class MyClass:
    """
    This is a sample class that follows PEP 8 guidelines.
    ...
    """

    def __init__(self):
        self.name = "MyClass"
        self.count = 0

    def my_method(self):
        self.count += 1
        print(f"Hello from {self.name}! Count: {self.count}")


my_object = MyClass()
my_object.my_method()


def parser(url, filepath='C:\\Users\\User\\Desktop\\file.txt'):
    """
    Downloads the content from the given URL and saves it to the specified file path.

    Args:
        url (str): The URL of the content to download.
        filepath (str): The file path where the content will be saved. Defaults to 'C:\\Users\\User\\Desktop\\file.txt'.

    Returns:
        str: The absolute path of the saved file.

    """
    if not os.path.exists(filepath):
        os.makedirs(filepath)
    else:
        exit()

    response = requests.get(url)
    content = response.text

    with open(filepath, 'w') as file:
        file.write(content)

    return os.path.abspath(filepath)


parser_result = parser(URL)


def summarizer(var_one, var_two, var_three,
               var_four, var_five, var_six) -> list[Any]:
    print(var_one, var_two, var_three, var_four,
          var_five, var_six)

    return sum([var_one, var_two, var_three,
                var_four, var_five, var_six])


number_zero = my_function()

result = summarizer(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

my_list = [
    1, 2, 3,
    4, 5, 6,
]
my_new_variable = 2 * pi_number

gross_wages = 100_000
dividends = 2_000
taxable_interest = 1000
qualified_dividends = 150000

income = (
    gross_wages
    + taxable_interest
    + (dividends - qualified_dividends)
)

multiplicative = gross_wages*qualified_dividends
