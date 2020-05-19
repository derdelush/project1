for i in range(1, 100):
    square = i**2
    if square > 2000:
        continue
    print(i, " * ", i, " = ", square)
