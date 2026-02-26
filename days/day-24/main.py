#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def read_names():
    names = []
    with open("./Input/Names/invited_names.txt") as file:
        for line in file:
            names.append(file.readline().rstrip())
    return names

def read_letter():
    with open("./Input/Letters/starting_letter.txt") as file:
        return file.read()



names = read_names()
letter = read_letter()

for name in names:
    letter_with_name = letter.replace("[name]", name)
    print(letter_with_name)
    file_name = "./Output/ReadyToSend/letter_for_" + name.lower() + ".txt"
    with open(file=file_name, mode="x") as file:
        file.write(letter_with_name)

print(names)
