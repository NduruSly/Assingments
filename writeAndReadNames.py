names = ["Alic", "Bob", "Charlie", "David", "Eve"]
with open("names.txt", "w") as f:
    for name in names:
        f.write(f"{name}\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
