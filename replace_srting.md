# Generate a script that changes a certain string in all the files in a directory to another input string.

## Bash

```bash
#!/bin/bash

# Usage: ./replace_string.sh "old_string" "new_string" /path/to/directory

OLD_STRING=$1
NEW_STRING=$2
DIRECTORY=$3

# Check if all arguments are provided
if [ -z "$OLD_STRING" ] || [ -z "$NEW_STRING" ] || [ -z "$DIRECTORY" ]; then
  echo "Usage: $0 OLD_STRING NEW_STRING DIRECTORY"
  exit 1
fi

# Find and replace
find "$DIRECTORY" -type f -exec sed -i '' "s/$OLD_STRING/$NEW_STRING/g" {} +

echo "Replacement completed."
```

### Explanation:
1. **Argument Check:** The script first checks if all the required arguments (`OLD_STRING`, `NEW_STRING`, and `DIRECTORY`) are provided.
2. **Find Command:** `find "$DIRECTORY" -type f` finds all files in the specified directory.
3. **sed Command:** `sed -i '' "s/$OLD_STRING/$NEW_STRING/g" {} +` performs an in-place replacement of `OLD_STRING` with `NEW_STRING` in all found files.

### Usage Example:
Save this script as `replace_string.sh` and run it like this:
```bash
./replace_string.sh "old_text" "new_text" /path/to/directory
```

This will replace all occurrences of `"old_text"` with `"new_text"` in all files within `/path/to/directory`.


## Python
Here's a Python script that accomplishes the same task of replacing a specific string with another string in all the files within a directory. This script uses the `os` and `fileinput` modules:

```python
import os
import fileinput

def replace_string_in_files(old_string, new_string, directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
                for line in file:
                    print(line.replace(old_string, new_string), end='')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python replace_string.py OLD_STRING NEW_STRING DIRECTORY")
        sys.exit(1)

    old_string = sys.argv[1]
    new_string = sys.argv[2]
    directory = sys.argv[3]

    replace_string_in_files(old_string, new_string, directory)
```

### Explanation:
1. **os.walk:** This function is used to traverse the directory tree. It yields a tuple for each directory it visits, containing the directory path, the directories it contains, and the files it contains.
2. **fileinput.FileInput:** This is used for in-place modification of files. The `inplace=True` parameter allows the script to replace text within the file directly. The `backup='.bak'` creates a backup of the original file.
3. **Replacing Strings:** Each line in the file is read, the specified string is replaced, and the modified line is printed back into the file.

### Usage:
Save this script as `replace_string.py` and run it like this:

```bash
python replace_string.py "old_text" "new_text" /path/to/directory
```

This will replace all occurrences of `"old_text"` with `"new_text"` in all files within `/path/to/directory`.
