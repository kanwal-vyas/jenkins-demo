with open("README.md", "r") as f:
    a, b = map(int, f.read().split())

print("Sum is", a + b)
