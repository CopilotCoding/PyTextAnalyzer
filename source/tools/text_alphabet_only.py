import re

def remove_non_alpha(string):
    """
    This function removes all non-alphabetic characters from a string using regular expressions.
    """
    alpha_string = re.sub('[^a-zA-Z]+', '', string)
    return alpha_string

file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    input_string = file.read()
output_string = remove_non_alpha(input_string)

print("Input string: ", input_string)
print("Output string: ", output_string)
input()
