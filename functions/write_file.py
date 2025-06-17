import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    path = os.path.abspath(os.path.join(working_directory, file_path))

    if not path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'

    if not os.path.exists(path):
        dirs = path.split(os.path.sep)
        os.makedirs(os.path.sep.join(dirs[:-1]), exist_ok=True)
    try:
        with open(path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error writing file "{file_path}": {e}'
