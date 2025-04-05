import random

def generate_random_numbers(count, min_val, max_val):
    """Generate a list of random integers between min_val and max_val."""
    return [random.randint(min_val, max_val) for _ in range(count)]

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0


random_numbers = generate_random_numbers(10, 1, 100)


average = calculate_average(random_numbers)


print("Generated numbers:", random_numbers)
print("Average:", average)