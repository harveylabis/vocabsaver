# ask for the word
from get_definition import define, get_filename

word = input("Enter a word: ")
word = word.title()

# find the definition
filename = get_filename(word)
definition = define(word, filename)

print(word)
print(definition)