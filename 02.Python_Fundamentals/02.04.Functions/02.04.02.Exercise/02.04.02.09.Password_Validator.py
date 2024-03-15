def password_validation(user_input):
    validation = True

    if len(user_input) < 6 or len(user_input) > 10:
        print("Password must be between 6 and 10 characters")
        validation = False

    if not user_input.isalnum():
        print("Password must consist only of letters and digits")
        validation = False

    num_counter = 0

    for character in user_input:
        if character.isdigit():
            num_counter += 1

    if num_counter < 2:
        print("Password must have at least 2 digits")
        validation = False

    return validation


password = input()

password_is_valid = password_validation(password)

if password_is_valid:
    print("Password is valid")
