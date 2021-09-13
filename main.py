import sys
import os
from get_definition import define, get_filename
from save_word import save_word, vocab_file_present, create_vocab_file

# ask user for a word
word = input("Enter a word: ")
word = word.title()

# find the definition
filename = get_filename(word)
definition = define(word, filename)

# print the definition if found
if definition:
    print(word, end='')
    print(definition)
else:
    sys.exit("Sorry, NO definition found.")

# ask the user to save the word
save = True
decision = input("Do you want to save this word? (y - yes): ")
if decision.lower() != 'y':
    save = False

# check if the file exists
if not vocab_file_present():
    create_vocab_file()

# save the word
if save:
    save_word(word)
else:
    print("'{}' NOT added.".format(word))