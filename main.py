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
        
with open(f"ReadyToSend/{contents[0]}.txt", "w") as file:
    
    starting_contents[0] = f"Dear {contents[0]},"
    
    for line in starting_contents:
        file.write(f"{line}\n")