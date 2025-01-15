# File Read & Write and Error Handling Combined Script

def read_and_write_file():
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read from (e.g., input.txt): ")
        with open(input_file, 'r') as file:
            content = file.read()
            print("\nContent of the input file:")
            print(content)

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Ask for the output filename
        output_file = input("\nEnter the name of the file to write to (e.g., output.txt): ")
        with open(output_file, 'w') as file:
            file.write(modified_content)
            print(f"\nModified content has been written to {output_file}.")
    
    except FileNotFoundError:
        print("\nError: The file you specified does not exist. Please check the filename and try again.")
    except IOError:
        print("\nError: Unable to read or write to the specified file. Please check permissions and try again.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

def main():
    while True:
        print("\n--- File Read & Write Program ---")
        read_and_write_file()

        # Ask if the user wants to run the program again
        choice = input("\nWould you like to process another file? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nExiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()