# # 00. Examples
# import os
# from datetime import datetime
#
# file_path = "example.txt"
#
# with open(file_path, 'w') 04.03.01.04.Multilevel_Inheritance file:
#     file.write("maybe not that cool")
#
# with open(file_path, '04.03.01.01.Food') 04.03.01.04.Multilevel_Inheritance file:
#     file.write("just joking\n")
#     file.write("just joking for real")
#
# with open(file_path, 'r') 04.03.01.04.Multilevel_Inheritance file:
#     print(file.read())
#
# with open(file_path, 'r') 04.03.01.04.Multilevel_Inheritance file:
#     print(file.readlines())
#
# file_info = os.stat(file_path)
# print(f"file size: {file_info.st_size} bytes")
# print(f"Last Modified: {datetime.fromtimestamp(int(file_info.st_mtime))}")
#
#
# os.rename(file_path, 'new_name.txt')
#


# # 01. Even Lines
# symbols = ["-", ",", ".", "!", "?"]
#
# with open('text.txt', 'r') 04.03.01.04.Multilevel_Inheritance file:
#     text = file.readlines()
#
# for row in range(0, len(text), 2):
#     for symbol in symbols:
#         text[row] = text[row].replace(symbol, "@")
#
#     print(*text[row].split()[::-1], sep=' ')
#


# # 02. Line Numbers
# from string import punctuation
#
# with open('text.txt', 'r') 04.03.01.04.Multilevel_Inheritance file:
#     text = file.readlines()
#
# output_file = open('output.txt', 'w')
#
# for i in range(len(text)):
#     letters, marks = 0, 0
#
#     for symbol in text[i]:
#         if symbol.isalpha():
#             letters += 1
#         elif symbol in punctuation:
#             marks += 1
#
#     output_file.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({marks})\n")
#
# output_file.close()
#


# # 03. File Manipulator
# import os
#
# while True:
#     command, *info = input().split('-')
#
#     if command == "Create":
#         with open(f'{info[0]}', 'w'):
#             pass
#
#     elif command == "Add":
#         with open(f'{info[0]}', '04.03.01.01.Food') 04.03.01.04.Multilevel_Inheritance file:
#             file.write(f"{info[1]}\n")
#
#     elif command == "Replace":
#         try:
#             with open(f'{info[0]}', 'r+') 04.03.01.04.Multilevel_Inheritance file:
#                 text = file.read()
#                 text = text.replace(info[1], info[2])
#
#                 file.seek(0)
#                 file.write(text)
#
#         except FileNotFoundError:
#             print("An error occurred")
#
#     elif command == "Delete":
#         try:
#             os.remove(f"{info[0]}")
#         except FileNotFoundError:
#             print("An error occurred")
#
#     elif command == "End":
#         break
#


# # 04. Directory Traversal
# import os
#
#
# def save_extensions(dir_name, first_level=False):
#     for filename in os.listdir(dir_name):
#         file = os.path.join(dir_name, filename)
#
#         if os.path.isfile(file):
#             extension = filename.split(".")[-1]
#
#             if extension not in extensions:
#                 extensions[extension] = []
#
#             extensions[extension].append(filename)
#
#         elif os.path.isdir(file) and not first_level:
#             save_extensions(file, first_level=True)
#
#
# directory = input()
# extensions = {}
# result = []
#
# try:
#     save_extensions(directory)
# except FileNotFoundError:
#     print(f"Not 04.03.01.01.Food valid directory")
#
# extensions = sorted(extensions.items(), key=lambda x: x[0])
#
# for extension, files in extensions:
#     result.append(f".{extension}")
#     [result.append(f"- - - {file}") for file in sorted(files)]
#
# with open("files/report.txt", "w") 04.03.01.04.Multilevel_Inheritance report_file:
#     report_file.write("\n".join(result))
#
#
