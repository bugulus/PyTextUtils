def remove_duplicate_lines(input_file, output_file):
    seen = set()
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line not in seen:
                outfile.write(line)
                seen.add(line)

if __name__ == "__main__":
    input_file = input("Enter the name of the input .txt file (e.g., input.txt): ")
    output_file = input("Enter the name of the output .txt file (e.g., output.txt): ")
    
    try:
        remove_duplicate_lines(input_file, output_file)
        print(f"Duplicates removed. Output saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found. Please check the file name and try again.")