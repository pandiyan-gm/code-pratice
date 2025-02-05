#This program prints the diamond shape 

n = 7  # Number of rows for the upper half

# Upper part of the diamond
for i in range(1, n + 1, 2):
    print(" " * ((n - i) // 2) + "*" * i)

# Lower part of the diamond
for i in range(n - 2, 0, -2):
    print(" " * ((n - i) // 2) + "*" * i)
