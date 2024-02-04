start = int(input())
end = int(input())

for i in range(start, end + 1):
    result = chr(i)
    print(f"{result}", end=' ')
