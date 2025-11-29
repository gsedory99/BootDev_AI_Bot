import os

def get_files_info(working_directory, directory="."):
    raw_path = os.path.join(working_directory, directory)
    absolute_path = os.path.abspath(raw_path)
    absolute_working_dir = os.path.abspath(working_directory)

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'
    if not absolute_path.startswith(absolute_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    dir_contents = os.listdir(absolute_path)
    contents_info = []

    for content in dir_contents:
        content_path = os.path.join(absolute_path, content)
        size= os.path.getsize(content_path)
        is_dir = os.path.isdir(content_path)
        contents_info.append(f"- {content}: file_size={size} bytes, is_dir={is_dir}\n")  
    return "".join(contents_info)
