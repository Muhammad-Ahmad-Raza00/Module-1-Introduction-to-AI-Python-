def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    else:
        return "Invalid operation"
print("Addition:", calculator(10, 5, "add"))
print("Subtraction:", calculator(10, 5, "subtract"))
