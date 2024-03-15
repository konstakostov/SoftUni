def sorting_cheeses(**kwargs):
    result = ""

    sorted_cheese = sorted(kwargs.items(),
                           key=lambda x: (-len(x[1]), x[0]))

    for cheese_name, quantity in sorted_cheese:
        result += cheese_name + "\n"
        reversed_quantities = sorted(quantity, reverse=True)
        result += "\n".join(str(el) for el in reversed_quantities) + "\n"

    return result


print(sorting_cheeses(Parmesan=[102, 120, 135],
                      Camembert=[100, 100, 105, 500, 430],
                      Mozzarella=[50, 125],
                      )
      )

print(sorting_cheeses(Parmigiano=[165, 215],
                      Feta=[150, 515],
                      Brie=[150, 125],
                      )
      )
