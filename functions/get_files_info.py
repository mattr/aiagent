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
