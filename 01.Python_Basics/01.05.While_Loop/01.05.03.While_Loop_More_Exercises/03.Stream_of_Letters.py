message = ""

c_count = 0
o_count = 0
n_count = 0

while True:
    command = input()

    if command == "End":
        break

    if








# message = ''  # here we store the message
#
# c_count = 0
# n_count = 0
# o_count = 0
#
# while True:
#     input_char = input()
#     if input_char == 'End':
#         break
#     # Check if char is from latin alphabet. Latin aplphabet in ascii table is between 65-90 for
#     # Capital letter and from 96-122 for small letters.
#     if (ord(input_char) >= 65 and ord(input_char) <= 90) \
#             or (ord(input_char) >= 97 and ord(input_char) <= 122):
#         #  Chek if input is c, n or o and increment counters
#         if input_char == 'c':
#             c_count += 1
#             if c_count >= 1 and n_count >= 1 and o_count >= 1:
#                 message += ' '
#                 print(message, end='')  # Print and dont go to new line
#                 # Reset counters and message
#                 message = ''
#                 c_count = 0
#                 n_count = 0
#                 o_count = 0
#                 continue
#             if c_count <= 1:  # If char is c and this is first time it appear we use continue bkz this char is not used in final message
#                 continue
#         elif input_char == 'n':
#             n_count += 1
#             if c_count >= 1 and n_count >= 1 and o_count >= 1:
#                 message += ' '
#                 print(message, end='')  # Print and dont go to new line
#                 # Reset counters and message
#                 message = ''
#                 c_count = 0
#                 n_count = 0
#                 o_count = 0
#                 continue
#             if n_count <= 1:  # If char is n and this is first time it appear we use continue bkz this char is not used in final message
#                 continue
#         elif input_char == 'o':
#             o_count += 1
#             if c_count >= 1 and n_count >= 1 and o_count >= 1:
#                 message += ' '
#                 print(message, end='')  # Print and dont go to new line
#                 # Reset counters
#                 message = ''
#                 c_count = 0
#                 n_count = 0
#                 o_count = 0
#                 continue
#             if o_count <= 1:  # If char is o and this is first time it appear we use continue bkz this char is not used in final message
#                 continue
#         # Check for space symbol!
#         if c_count >= 2 and n_count >= 2 and o_count >= 2:
#             message += ' '
#             print(message)
#             # Reset counters
#             c_count = 0
#             n_count = 0
#             o_count = 0
#             continue
#         message += input_char













