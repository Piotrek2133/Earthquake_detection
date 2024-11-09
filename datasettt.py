import re

# Open the file and process each line separately
with open('dataset1.txt', 'r') as file:
    lines = file.readlines()

# Process each line to replace multiple spaces with a single comma
processed_lines = [re.sub(r"\s+", ",", line.strip()) for line in lines]

# Write the modified content back to the file while keeping new lines
with open('dataset2.txt', 'w') as file:
    file.write("\n".join(processed_lines))