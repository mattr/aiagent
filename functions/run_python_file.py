import os
import subprocess


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith('.py'):
        return f'Error: File "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ['python', abs_file_path],
            capture_output=True,
            timeout=30
        )

        output = [result.stdout.decode(), result.stderr.decode()]
        if result.returncode != 0:
            output.append(f'Process exited with code {result.returncode}')
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            output.append("No output produced")

        return "\n".join(output)

    except subprocess.TimeoutExpired:
        return "Command timed out after 30 seconds."
