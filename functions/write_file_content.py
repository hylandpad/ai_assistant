import os

print("Working")
def write_file(working_directory, file_path, content):
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_dir_path = os.path.abspath(os.path.join(working_dir_path,file_path))

        if not target_dir_path.startswith(working_dir_path):
            return print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
        
        if os.path.exists(target_dir_path):
            print(f"{target_dir_path} found. Writing to file.")

        else:
            print(f"{target_dir_path} not found. Attempting to write new directory and file.")
            folder,file = os.path.split(target_dir_path)
            if not os.path.exists(folder):
                print("Parent directory/directories not found - creating required directories and writing file.")
                os.makedirs(folder)

        with open(target_dir_path,"w") as file:
            file.write(content)
        with open(target_dir_path) as file:
            file_content = file.read()
    
    except FileNotFoundError: 
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    except PermissionError:
        return print(f"Error: Permission denied to access '{target_dir_path}'.")
    except Exception as e:
        return print(f"Error: An unhandled exception occurred [{e}]")
    
    return print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')