CHANGE = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    letter_contents = letters.read()
    for name in name_list:
        new_name = name.strip()
        new_letter_contents = letter_contents.replace(CHANGE, new_name)
        with open(f"./Output/ReadyToSend/letter_to_{new_name}", mode="w") as new_letter:
            new_letter.write(new_letter_contents)




