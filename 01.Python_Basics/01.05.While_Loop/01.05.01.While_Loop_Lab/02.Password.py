username = input()
password = input()
security = None

while security != password:
    security = input()
    if security == password:
        print(f"Welcome {username}!")
