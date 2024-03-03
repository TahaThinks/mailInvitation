contents = []

with open("invited_names.txt") as file:
    for line in file:
        contents.append(line.rstrip())

print(contents)