n = int(input("Enter N: "))

tot = 0
for i in range(1, n + 1):
    tot += i

print(f"Sum of the first {n} natural numbers: {tot}")