x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if (x == x1 or x == x2) and y1 < y < y2:
    print("Border")
elif (y == y1 or y == y2) and x1 < x < x2:
    print("Border")
elif (x == x1 and y == y2) or (x == x2 and y == y1) or\
        (x == x1 and y == y1) or (x == x2 and y == y2):
    print("Border")
elif (y != y1 or y != y2) and x1 < x < x2:
    print("Inside / Outside")
elif (x != x1 or x != x2) and y1 < y < y2:
    print("Inside / Outside")
elif (y != y1 or y != y2) and x1 < x < x2:
    print("Inside / Outside")
else:
    print("Inside / Outside")

# x1 < x2
# y1 < y2
# x,y lies on x1,y1 or x2,y2 if:
#                               x == x1, x == x2 & y is between y1 and y2
#                               y == y1, y == y2 & x is between x1 and x2
