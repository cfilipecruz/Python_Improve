# Create files named ex_005 to ex_100
for i in range(5, 50):
    file_name = f"challenges_{i:03d}.py"
    with open(file_name, 'w') as file:
        pass  # Create an empty file

print("Files created successfully.")