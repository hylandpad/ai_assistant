import os

def get_files_info(working_directory, directory="."):
    target_path = os.path.join(working_directory,directory)
    working_abs_path = os.path.abspath(working_directory)
    target_abs_path = os.path.abspath(target_path)

    if os.path.isdir(target_abs_path) == False:
        print(f'Error: "{target_abs_path}" is not a directory')
    elif target_abs_path.startswith(working_abs_path) == False:
        print(f"{directory} NOT found in {working_abs_path}")
    else:
        print(f"{directory} found in {working_abs_path}")
        dir_contents = os.listdir(target_abs_path)
        for content in dir_contents:
            full_path = os.path.join(target_abs_path, content)
            content_list = []
            content_list.append(content)
            content_list.append(os.path.getsize(full_path))
            content_list.append(os.path.isdir(full_path))
            print(content_list)


get_files_info("/home/hylan/workspace/github.com/hylandpad/ai_assistant/calculator","pkg")
