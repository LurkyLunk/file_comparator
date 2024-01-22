def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines(data)

def compare_files(file1_lines, file2_lines):
    unique_in_file1 = set(file1_lines) - set(file2_lines)
    unique_in_file2 = set(file2_lines) - set(file1_lines)
    return sorted(unique_in_file1), sorted(unique_in_file2)

# Paths to the input files
input_file_1 = 'input1.txt'
input_file_2 = 'input2.txt'

# Read the input files
file1_lines = read_file(input_file_1)
file2_lines = read_file(input_file_2)

# Compare the files and get the unique lines
unique_file1, unique_file2 = compare_files(file1_lines, file2_lines)

# Paths to the output files
output_file_1 = '../output1.txt'
output_file_2 = '../output2.txt'

# Write the unique lines to the output files
write_file(output_file_1, unique_file1)
write_file(output_file_2, unique_file2)
