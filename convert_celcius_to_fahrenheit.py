celcius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fahrenheit = list(map(lambda c: (c * 9 / 5) + 32, celcius))
print(fahrenheit)