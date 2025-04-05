def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

input_filename = 'answers.txt' 
output_filename = 'modified_answers.txt'  
read_and_write_file(input_filename, output_filename)


##Error Handling Lab## 
def open_file_and_read():
    filename = 'answers.txt'  # Hardcoded file name

    try:
        # Attempt to open the file and read its contents
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} cannot be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
open_file_and_read()


