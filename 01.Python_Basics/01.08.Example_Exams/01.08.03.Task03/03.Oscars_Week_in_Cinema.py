movie = input()
room = input()
tickets = int(input())

money = 0

if movie == "A Star Is Born":
    if room == "normal":
        money = tickets * 7.50
    elif room == "luxury":
        money = tickets * 10.50
    elif room == "ultra luxury":
        money = tickets * 13.50

elif movie == "Bohemian Rhapsody":
    if room == "normal":
        money = tickets * 7.35
    elif room == "luxury":
        money = tickets * 9.45
    elif room == "ultra luxury":
        money = tickets * 12.75

elif movie == "Green Book":
    if room == "normal":
        money = tickets * 8.15
    elif room == "luxury":
        money = tickets * 10.25
    elif room == "ultra luxury":
        money = tickets * 13.25

elif movie == "The Favourite":
    if room == "normal":
        money = tickets * 8.75
    elif room == "luxury":
        money = tickets * 11.55
    elif room == "ultra luxury":
        money = tickets * 13.95

print(f"{movie} -> {money:.2f} lv.")
