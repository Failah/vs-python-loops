row = int(input("How many rows?: "))
col = int(input("How many columns?: "))
sym = input("Enter a symbol to use: ")

for i in range(row):
    for j in range(col):
        print(sym, end="")  # end = "" prevents from going into a new line with print()
    print()

