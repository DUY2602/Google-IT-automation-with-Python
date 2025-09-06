# Debug using assert

def divide(a, b):
    print(f"DEBUG: a={a}, b={b}")

    assert b != 0, "Error: Cannot divide by zero!"

    return a / b


def main():
    print("Case 1: Divide 10 / 2")
    result = divide(10, 2)
    print("Result:", result)

    print("\nCase 2: Divide 5 / 0")
    result = divide(5, 0)
    # Activate the assert in function divide


if __name__ == "__main__":
    main()
