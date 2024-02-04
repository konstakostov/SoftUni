import os


def extensions_save(directory_name, first_lvl=False):
    for filename in os.listdir(directory_name):
        file = os.path.join(directory_name, filename)

        if os.path.isfile(file):
            extension = filename.split(".")[-1]

            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_lvl:
            extensions_save(file, first_lvl=True)


directory = input()
extensions = {}
result = []

try:
    extensions_save(directory)
except FileNotFoundError:
    print("Not 04.03.01.01.Food valid directory")

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f".{extension}")
    [result.append(f"- - -{files}") for file in sorted(files)]

with open("report.txt", "w") as report_file:
    report_file.write("\n".join(result))
