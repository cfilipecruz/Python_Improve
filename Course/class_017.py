values = [45, 67, 23, 89, 12, 56, 78, 34, 90, 11]
print(values)

# Append a new value to the end of the list
values.append(44)
print(values)

# Sort the list in ascending order
values.sort()
print(values)

# Reverse the order of the list
values.reverse()
print(values)

# Remove the first occurrence of the specified value from the list
values.remove(45)
print(values)

# Insert a new value at a specific index
values.insert(3, 77)
print(values)

# Count the occurrences of a specific value in the list
count_of_56 = values.count(56)
print(f"Number of times 56 appears in the list: {count_of_56}")

# Find the index of the first occurrence of a specific value
index_of_89 = values.index(89)
print(f"Index of the value 89: {index_of_89}")

# Remove the value at a specific index and return it
popped_value = values.pop(5)
print(f"Popped value: {popped_value}")
print(values)

# Extend the list by appending elements from another list
values.extend([1, 2, 3])
print(values)

# Clear all elements from the list
values.clear()
print(values)

# Re-populate the list for additional examples
values = [45, 67, 23, 89, 12, 56, 78, 34, 90, 11]
print(values)

# Get the length of the list
length_of_values = len(values)
print(f"Length of the list: {length_of_values}")

# Check if a value is in the list
is_56_in_list = 56 in values
print(f"Is 56 in the list? {is_56_in_list}")

# Make a copy of the list
values_copy = values.copy()
print(f"Copied list: {values_copy}")

# Find the minimum value in the list
min_value = min(values)
print(f"Minimum value in the list: {min_value}")

# Find the maximum value in the list
max_value = max(values)
print(f"Maximum value in the list: {max_value}")

# Sum all values in the list
sum_of_values = sum(values)
print(f"Sum of all values in the list: {sum_of_values}")

# Slice the list to get a sublist
sublist = values[2:6]
print(f"Sublist from index 2 to 5: {sublist}")

# Iterate through the list and print each element
for value in values:
    print(value)
