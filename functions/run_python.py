import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        target_path = os.path.join(working_directory,file_path)
        working_abs_path = os.path.abspath(working_directory)
        target_abs_path = os.path.abspath(target_path)
        dir,file = os.path.split(target_abs_path)

        #print(f"working dir = {working_abs_path}, file path = {file_path}, file absolute path = {target_abs_path}")

        if not target_abs_path.startswith(working_abs_path):
            return print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        elif not os.path.exists(target_abs_path):
            return print(f'Error: File "{file_path}" not found.')
        elif not file.endswith('.py'):
            return print(f'Error: "{file_path}" is not a Python File.')
        else:
            try:
                print("Executing python file")
                cmd = ['python',file_path] + args                
                python_execute = subprocess.run(cmd, cwd=working_abs_path, timeout=30, capture_output=True, text=True, check=True)
                pyth_stdout = python_execute.stdout
                pyth_stderr = python_execute.stderr
                pyth_exit = python_execute.returncode
                if not python_execute:
                    return "No output produced"
                return_stmt = f"STDOUT: {pyth_stdout}\n STDERR: {pyth_stderr}\n"
                if pyth_exit != 0:
                    return_stmt += f"Process exited with code {pyth_exit}"
                return print(return_stmt)
            except Exception as e:
                return print(f"Error: executing Python file [{e}]")
    except FileNotFoundError: 
        return print(f'Error: File not found or is not a regular file: "{file_path}"')
    except PermissionError:
        return print(f"Error: Permission denied to access '{file_path}'.")
    except Exception as e:
        return print(f"Error: An unhandled exception occurred [{e}]")