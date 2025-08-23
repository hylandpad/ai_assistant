from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file_content import write_file
from functions.run_python import run_python_file
from google.genai import types

def call_function(function_call_part, verbose=False):
    
    error_return = types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_call_part.name,
            response={"error": f"Unknown function: {function_call_part.name}"},
        )
    ],
    )
    
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file
    }

    function_call_part.args["working_directory"] = "./calculator"
    
    try:
        if function_call_part.name in function_map:
            running_func = function_map[function_call_part.name]
            function_result = running_func(**function_call_part.args)
        
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"result": function_result},
                    )
                ],
            )
        
        else:
            return error_return
    except Exception as e:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Error: {e}"},
                )
            ],
        )
