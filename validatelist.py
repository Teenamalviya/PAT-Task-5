# List of elements
data = [10, 501, 22, 37, 100, 999, 97, 351]

# Method to check whether element of list is string or integer
def is_string_or_integer(x):
    return isinstance(x, (str, int))

# Iterate lambda function each element of list
all_string_or_integer = all(is_string_or_integer(x) for x in data)

# If return value from above is true then all elements are strings/integers else they aren't
if all_string_or_integer:
  print("All elements of the list are strings or integers.")
else:
  print("Not all elements of the list are strings or integers.")