import os

def write_file(working_directory, file_path, content):
    raw_path = os.path.join(working_directory, file_path)
    absolute_file_path = os.path.abspath(raw_path)
    absolute_working_dir = os.path.abspath(working_directory)

    if not absolute_file_path.startswith(absolute_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    file_directory = os.path.dirname(raw_path)
    os.makedirs(file_directory, exist_ok=True)
    with open(raw_path, "w") as f:
        f.write(content)

    return f'Successfully write to "{file_path}" ({len(content)} characters written)'
