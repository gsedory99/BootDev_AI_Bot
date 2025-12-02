import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    raw_path = os.path.join(working_directory, file_path)
    absolute_file_path = os.path.abspath(raw_path)
    absolute_working_dir = os.path.abspath(working_directory)

    if not absolute_file_path.startswith(absolute_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(absolute_file_path):
        return f'Error: File "{file_path}" not found.'
    if absolute_file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        import sys
        command = [sys.executable, absolute_file_path] + args
        result = subprocess.run(
            command, 
            timeout=30,
            cwd=absolute_working_dir,
            capture_output=True,
            text=True
        )
    except subprocess.TimeoutExpired:
        return "Error: Process timed out after 30 seconds."
    
    except Exception as e:
        return f"Error: executing Python file: {e}"

    final_output = f'STDOUT: {result.stdout}\nSTDERR:{result.stderr}'

    if result.returncode != 0:
        final_output += f'\nProcess exited with code {result.returncode}'

    if not result.stdout and not result.stderr:
        return "No output produced."

    return final_output
    
