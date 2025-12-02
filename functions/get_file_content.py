import os
import config
from google.genai import types

def get_file_content(working_directory, file_path):
    raw_path = os.path.join(working_directory, file_path)
    absolute_file_path = os.path.abspath(raw_path)
    absolute_working_dir = os.path.abspath(working_directory)

    if not os.path.isfile(absolute_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    if not absolute_file_path.startswith(absolute_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    with open(raw_path, "r") as f:
        file_content_string = f.read(config.MAX_CHARS)

    if len(file_content_string) == config.MAX_CHARS:
        file_content_string += f' "{file_path}" truncated at {config.MAX_CHARS} characters'


    return file_content_string


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file in the form of a string and returns the string",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to the file, relative to the working directory",
            ),
        },
    ),
)
