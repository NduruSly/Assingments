def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Invalid types - both arguments must be numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


safe_divide(10, 2)
safe_divide(10, 0)
safe_divide("10", 2)
safe_divide(10, "2")