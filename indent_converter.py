#!/usr/bin/env python3

def convert_indentation(file_path, to_two_spaces=True):
    """Convert between 2 and 4 space indentation."""
    try:
        # Read file content
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Process each line
        converted_lines = []
        for line in lines:
            # Count leading spaces
            leading_spaces = len(line) - len(line.lstrip())
            # Calculate new indentation
            if to_two_spaces:
                # Convert from 4 to 2 spaces
                new_indent = ' ' * (leading_spaces // 2)
            else:
                # Convert from 2 to 4 spaces
                new_indent = ' ' * (leading_spaces * 2)
            
            # Replace old indentation with new
            converted_lines.append(new_indent + line.lstrip())
        
        # Write back to file
        with open(file_path, 'w') as file:
            file.writelines(converted_lines)
            
        print(f"Successfully converted {file_path}")
            
    except Exception as err:
        print(f"Error processing {file_path}: {str(err)}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python indent_converter.py <file_path> [--to-four-spaces]")
        sys.exit(1)
        
    file_path = sys.argv[1]
    to_two_spaces = "--to-four-spaces" not in sys.argv
    
    convert_indentation(file_path, to_two_spaces)
