with open("README.md", "r") as f:
    a, b = map(int, f.read().split())

result = a + b

print("Sum is", result)

# condition check (simulate test)
if result != 15:
    raise Exception("Test Failed: Incorrect Sum")
