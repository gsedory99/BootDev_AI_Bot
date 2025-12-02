import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="writes a file with the given conetent constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to write the file to, relative to the working directory. If the directoy does not extist it will be created.",
            ),
        },
    ),
)
