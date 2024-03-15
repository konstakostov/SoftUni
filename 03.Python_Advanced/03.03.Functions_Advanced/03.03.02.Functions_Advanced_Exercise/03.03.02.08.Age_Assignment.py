def age_assignment(*names, **kwargs):
    names = sorted(names)

    result = []

    for name in names:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                result.append(f"{name} is {age} years old.")

    return "\n".join(result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
