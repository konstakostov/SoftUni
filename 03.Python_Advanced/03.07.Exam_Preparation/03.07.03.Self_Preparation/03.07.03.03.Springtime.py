def start_spring(**kwargs):
    result = ""
    spring = {}

    for spring_object, spring_type in kwargs.items():
        if spring_type not in spring:
            spring[spring_type] = []

        spring[spring_type].append(spring_object)

    spring = sorted(spring.items(), key=lambda x: (-len(x[1]), x[0]))

    for item in spring:
        result += f"{item[0]}:\n"
        spring = sorted(item[1])

        for spring_item in spring:
            result += f"-{spring_item}\n"

    return result.strip()


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))

print()

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

print()

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
