"""
Here are the test steps for the multiplication function in positive test cases:

Define the first number
Define the second number
Perform the multiplication operation
Check if the user gets the expected
Now, let’s automate the test:"""

"""
Create a function called test_multiply() by using the def keyword.
Define the first and second numbers as an integer variable. a = 2 b = 3
Write the snippet for multiplication. multiply = a * b
Add an assertion to check if the user gets the expected. assert multiply == 6
Take a look at the test code:"""

# Test 1. Verification of multiplication function
# Positive test

def test_multiply():
    # Define the first number
    a = 2
    # Define the second number
    b = 3
    # Perform the multiplication operation
    multiply = a * b
    # Check if the user gets the expected
    assert multiply == 6