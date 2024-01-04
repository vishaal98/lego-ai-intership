import re

# Function to filter lines based on specified conditions
def filter(file_name):
    # Define regex pattern for filtering names
    pattern = re.compile(r'^[a-fA-F][^_\n]{3,}$')
    filtered_values = []

    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if pattern.match(line.strip()):
                filtered_values.append(line)

    return filtered_values

# File name containing the input data
file_name = 'input.txt'

# Filter names based on conditions
output = filter(file_name)

# write the filtered values to the output file
with open("output.txt", 'w') as file:
    for line in output:
        file.write(line)
