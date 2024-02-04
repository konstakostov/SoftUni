# # 01. File Opener
# try:
#     file_open = open("text.txt", 'r')
#     print("File Found")
# except FileNotFoundError:
#     print("File Not Found")
#


# # 02. File Reader
# file = open("numbers.txt", 'r')
#
# num_sum = 0
#
# for num in file:
#     num_sum += int(num)
#
# print(num_sum)
#


# # 03. File Writer
# file = open("my_first_file.txt", 'w')
# file.write("I just created my first file!")
#


# # 04. File Delete
# import os
#
# file = "my_first_file.txt"
#
# if os.path.exists(file):
#     os.remove(file)
# else:
#     print("File already deleted!")
#


# 05. Word Count


