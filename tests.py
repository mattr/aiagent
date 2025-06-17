# from functions.get_file_content import get_file_content
# from functions.get_files_info import get_files_info
# from functions.write_file import write_file
from functions.run_python_file import run_python_file


# class TestGetFilesInfo(unittest.TestCase):
#     def test_get_calculator(self):
#         actual = get_files_info("calculator", ".")
#         expected = """- tests.py: file_size=1343 bytes, is_dir=False
# - main.py: file_size=576 bytes, is_dir=False
# - pkg: file_size=160 bytes, is_dir=True"""
#         self.assertEqual(actual, expected)
#
#     def test_get_calculator_pkg(self):
#         expected = """- render.py: file_size=767 bytes, is_dir=False
# - __pycache__: file_size=128 bytes, is_dir=True
# - calculator.py: file_size=1750 bytes, is_dir=False"""
#         actual = get_files_info("calculator", "pkg")
#         self.assertEqual(actual, expected)
#
#     def test_get_calculator_bin(self):
#         actual = get_files_info("calculator", "bin")
#         expected = 'Error: Cannot list "bin" as it is outside the permitted working directory'
#         self.assertEqual(actual, expected)
#
#     def test_get_files_info(self):
#         actual = get_files_info("calculator", "../")
#         expected = 'Error: Cannot list "../" as it is outside the permitted working directory'
#         self.assertEqual(actual, expected)


def test():
    # print(get_files_info("calculator", "."))
    # print(get_files_info("calculator", "pkg"))
    # print(get_files_info("calculator", "/bin"))
    # print(get_files_info("calculator", "../"))
    # print(get_file_content("calculator", "main.py"))
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print(get_file_content("calculator", "/bin/cat"))
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))


if __name__ == '__main__':
    test()
