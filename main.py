# ask for the word
from get_definition import define, get_filename
from save_word import save_word

word = input("Enter a word: ")
word = word.title()

# find the definition
filename = get_filename(word)
definition = define(word, filename)

# print the definition
print(word)
print(definition)

# ask to save the word
save = True
decision = input("Do you want to save this word? (y - yes): ")
if decision.lower() != 'y':
    save = False

# save the word
if definition and save:
    save_word(word)