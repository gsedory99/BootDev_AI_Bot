import os

def get_file_content(working_directory, file_path):
    raw_path = os.path.join(working_directory, file_path)
    absolute_file_path = os.path.abspath(raw_path)
    absolute_working_dir = os.path.abspath(working_directory)

    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{absolute_file_path}"'
    if not absolute_file_path.startswith(absolute_working_dir):
        f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'kk
