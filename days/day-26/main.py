

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Step 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
import pandas as p
words_ds = p.read_csv("nato_phonetic_alphabet.csv")

words_dict = {row.letter:row.code for (index,row) in words_ds.iterrows() if row.letter != "letter"}

print(words_dict)

#Step 2. Create a list of the phonetic code words from a word that the user inputs.

print(words_dict["B"])

input_word = input("Enter a word: ")

code_words = [words_dict[letter.upper()] for letter in input_word]

print("-".join(code_words))

