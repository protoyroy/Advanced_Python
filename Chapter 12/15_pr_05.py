# num = int(input('Enter your number\n'))
# table = [num * i for i in range (1,11)]
# # print(table)

# formatted = [f"{num} x {i} = {table[i-1]}" for i in range(1,11)]
# print(*formatted, sep='\n')
# with open("Chapter 12/tables.txt", "a") as f:
#     f.write('\n'.join(formatted))
#     if formatted != 10:  ## Code block to be executed if the length of 'formatted' is not equal to 10
#         f.write('\n')


import os

# Create a directory path
directory_name = "Chapter 12/tables"

# Create the directory if it doesn't exist
os.makedirs(directory_name, exist_ok=True)

# Get user input for the number
num = int(input('Enter your number\n'))

# Generate the multiplication table
table = [num * i for i in range(1, 11)]

# Format the table entries
formatted = [f"{num} x {i} = {table[i-1]}" for i in range(1, 11)]

# Print the formatted table
print(*formatted, sep='\n')

# Define the filename for the table
filename = f"Chapter 12/tables/Multiplication_table_of_{num}.txt"

# Write the table to a file
with open(filename, "w") as f:
    f.write('\n'.join(formatted))
    f.write('\n')  # Add a newline character after the table

