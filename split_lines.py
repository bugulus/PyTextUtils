def split_lines_by_separator(file_path, separator):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if separator in line:
                    parts = line.split(separator)
                    print(f"Line {line_num}: {parts}")
                else:
                    print(f"Line {line_num}: [No separator '{separator}' found] -> {line}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_path = input("Enter path to .txt file: ").strip()
    separator = input("Enter separator character (e.g. :, |, ,, etc): ").strip()

    if len(separator) != 1:
        print("Please enter exactly one character for the separator.")
    else:
        split_lines_by_separator(file_path, separator)

input("\nPress Enter to exit...")