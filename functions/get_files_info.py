import os


def get_files_info(working_directory, directory=None):
    path = None
    root = os.path.abspath(working_directory)
    if directory == ".":
        path = root
    else:
        for d in os.listdir(root):
            if d == directory:
                path = os.path.join(root, d)
                break

    if path is None:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'

    filelist = []
    for file in os.listdir(path):
        filepath = os.path.abspath(os.path.join(path, file))
        filelist.append(
            f"- {file}: file_size={os.path.getsize(filepath)} bytes, is_dir={os.path.isdir(filepath)}"
        )
    return "\n".join(filelist)


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
