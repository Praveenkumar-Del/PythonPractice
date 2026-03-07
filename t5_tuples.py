
# Tuples in Python - Comprehensive Details

# Tuples are immutable sequences in Python, meaning their elements cannot be changed after creation.
# They are ordered, allow duplicate values, and can contain elements of different data types.

# Creating tuples
# Using parentheses
empty_tuple = ()
single_element_tuple = (1,)  # Note the comma for single element
tuple_with_elements = (1, 2, 3, 4, 5)

# Without parentheses (tuple packing)
packed_tuple = 1, 2, 3, 4, 5

# Mixed data types
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3])

# Nested tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))

# Accessing elements
# Indexing (zero-based)
first_element = tuple_with_elements[0]
last_element = tuple_with_elements[-1]

# Slicing
slice_example = tuple_with_elements[1:4]  # Elements from index 1 to 3
reverse_slice = tuple_with_elements[::-1]  # Reverse the tuple

# Tuple methods
# count() - returns the number of occurrences of a value
count_example = tuple_with_elements.count(3)

# index() - returns the index of the first occurrence of a value
index_example = tuple_with_elements.index(4)

# Tuple operations
# Concatenation
concat_tuple = (1, 2) + (3, 4)

# Repetition
repeat_tuple = (1, 2) * 3

# Length
length = len(tuple_with_elements)

# Unpacking tuples
a, b, c = (1, 2, 3)
first, *middle, last = (1, 2, 3, 4, 5)

# Tuple with mutable elements (list inside tuple)
mutable_inside = (1, 2, [3, 4, 5])
# Note: The tuple itself is immutable, but mutable elements inside can be changed

# Converting to other types
list_from_tuple = list(tuple_with_elements)
string_from_tuple = str(tuple_with_elements)


# Printing examples
print("Empty tuple:", empty_tuple)
print("Single element tuple:", single_element_tuple)
print("Tuple with elements:", tuple_with_elements)
print("Packed tuple:", packed_tuple)
print("Mixed tuple:", mixed_tuple)
print("Nested tuple:", nested_tuple)
print("First element:", first_element)
print("Last element:", last_element)
print("Slice [1:4]:", slice_example)
print("Reversed:", reverse_slice)
print("Count of 3:", count_example)
print("Index of 4:", index_example)
print("Concatenated:", concat_tuple)
print("Repeated:", repeat_tuple)
print("Length:", length)
print("Unpacked a, b, c:", a, b, c)
print("Unpacked first, *middle, last:", first, middle, last)
print("Mutable inside:", mutable_inside)
print("As list:", list_from_tuple)
print("As string:", string_from_tuple)
