def concatenate(*args, **kwargs):
    message = ""

    for word in args:
        message += word

    for key, value in kwargs.items():
        message = message.replace(key, value)

    return message


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
