# File Read & Write Challenge 
def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as infile:
            content = infile.read()
            # Modify the content (for example, converting to uppercase)
            modified_content = content.upper()

        # Open the output file in write mode
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File '{output_filename}' has been created with modified content.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Error Handling 
def ask_for_filename_and_handle_errors():
    filename = input("Please enter the filename to read: ")
    output_filename = input("Please enter the name for the modified output file: ")

    # Call the function to read and write the file
    read_and_write_file(filename, output_filename)

# Run the error handling and file read/write process
ask_for_filename_and_handle_errors()
