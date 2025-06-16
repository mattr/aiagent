import os


def get_files_info(working_directory, directory=None):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if directory:
        target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    root = os.path.abspath(working_directory)
    try:
        path = os.path.join(root, file_path)
    except FileNotFoundError:
        return f'Error: "{file_path}" is not a file'
    if not os.path.isfile(path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            file_content_string = file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    except ValueError:
        return f'Error: "{file_path}" is not in the working directory'

    return file_content_string


def write_file(working_directory, file_path, content):
    path = os.path.join(os.path.abspath(working_directory), file_path)
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path, "w") as f:
        f.write(content)
