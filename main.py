contents = []

with open("invited_names.txt") as file:
    for line in file:
        contents.append(line.rstrip())

print(contents)

starting_contents = []

with open("starting_letter.txt") as file:
    for line in file:
        starting_contents.append(line.rstrip())

# Line to change at position[0] of starting_content

for content in contents:
    with open(f"ReadyToSend/letter_for_{content}.txt", "w") as file:
        starting_contents[0] = f"Dear {content},"
        for line in starting_contents:
            file.write(f"{line}\n")