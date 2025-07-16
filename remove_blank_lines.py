def remove_blank_lines(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    non_blank_lines = [line for line in lines if line.strip() != '']

    with open(output_file, 'w') as outfile:
        outfile.writelines(non_blank_lines)

    print(f"Blank lines removed. Output saved to: {output_file}")

# Example usage
input_path = input("Enter input .txt file path: ")
output_path = input("Enter output .txt file path: ")
remove_blank_lines(input_path, output_path)