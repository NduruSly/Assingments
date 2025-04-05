def classify_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

while True:
    user_input = input("Enter an integer:")
    try:
        num = int(user_input)
        break
    except ValueError:
        print("Invalid input.Please enter a valid integer")


