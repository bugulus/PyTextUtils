def sort_text_file(input_path, output_path=None):
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]

        lines.sort()  # Sort alphabetically

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                for line in lines:
                    outfile.write(line + '\n')
            print(f"✅ Sorted lines saved to {output_path}")
        else:
            print("📄 Sorted lines:")
            for line in lines:
                print(line)

    except FileNotFoundError:
        print(f"❌ File not found: {input_path}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    input_file = input("Enter path to .txt file: ").strip()
    save_option = input("Save to a new file? (y/n): ").strip().lower()

    if save_option == 'y':
        output_file = input("Enter path for output file: ").strip()
        sort_text_file(input_file, output_file)
    else:
        sort_text_file(input_file)

    input("\nPress Enter to exit...")