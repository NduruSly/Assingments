def calculate_average(*args):
    """Calculate the avaerage of a variable number of arguments"""
    if not args:
        return 0.0
    return sum(args) / len(args)


calculate_average(1, 4, 9, 23, 8, 9)

