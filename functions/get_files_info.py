import os

def get_files_info(working_directory, directory="."):
    target_path = os.path.join(working_directory,directory)
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(target_path)
    
    if target_abs_path.startswith(working_abs_path) == False:
        return print(f"Error: Cannot list '{directory}' as it is outside the permitted working directory")

    try:
        dir_contents = os.listdir(target_abs_path)
    except FileNotFoundError:
        return print(f"Error: The directory '{target_abs_path}' does not exist.")
    except PermissionError:
        return print(f"Error: Permission denied to access '{target_abs_path}'.")
    except Exception as e:
        return print(f"Error: An unhandled exception occurred [{e}]")
    
    content_list = []
    for content in dir_contents:
        full_path = os.path.join(target_abs_path, content)
        try:
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)
            content_list.append(f"{content}: file_size={file_size} bytes, is_dir={is_dir}")
        except Exception as e:
            print(f"Error: An unhandled exception occurred [{e}]")
    return print("\n".join(content_list))