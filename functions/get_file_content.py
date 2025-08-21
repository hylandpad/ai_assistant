import os
import config

def get_file_content(working_directory, file_path):
    
    try:
        working_dir_path = os.path.abspath(working_directory)
        target_dir_path = os.path.abspath(os.path.join(working_dir_path,file_path))

        if not target_dir_path.startswith(working_dir_path):
            return print(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        
        if not os.path.isfile(target_dir_path):
            return print(f'Error: Cannot read "{file_path}" as it is not a file')

        with open(target_dir_path, "r") as file:
            file_content = file.read()
            content_len = len(file_content)

        if content_len > config.MAX_CHARS:
            file_content_string = file_content[:config.MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters] \n \n ======END OF FILE====== \n \n '
        else:
            file_content_string = file_content + '\n \n ======END OF FILE====== \n \n'
        
    except FileNotFoundError: 
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    except PermissionError:
        return print(f"Error: Permission denied to access '{target_dir_path}'.")
    except Exception as e:
        return print(f"Error: An unhandled exception occurred [{e}]")
    
    return print(file_content_string)