def calculate_average(*numbers):
    """Return the average of the given numbers. Returns 0 if no numbers are provided."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


print(calculate_average(2, 8, 27, 8))
print(calculate_average(5, 10, 15, 6))
print(calculate_average())