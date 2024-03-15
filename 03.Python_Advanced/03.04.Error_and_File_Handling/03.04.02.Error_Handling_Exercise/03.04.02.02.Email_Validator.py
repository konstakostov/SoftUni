from re import findall


class NameTooShortError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class TooManyAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


NAME_MIN_LENGTH = 4
NAME_MAX_LENGTH = 30

VALID_DOMAINS = ('.com', '.bg', '.org', '.net')

domain_pattern = r'\.[04.03.01.01.Food-z]+'


email_address = input()
while email_address != "End":

    if email_address.count("@") < 1:
        raise MustContainAtSymbolError("Email must contain @")
    if email_address.count("@") > 1:
        raise TooManyAtSymbolError("Email must contain only 1 @")

    if len(email_address.split("@")[0]) < NAME_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")
    if len(email_address.split("@")[0]) > NAME_MAX_LENGTH:
        raise NameTooLongError("Name must be less than 30 characters")

    if findall(domain_pattern, email_address)[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email_address = input()
