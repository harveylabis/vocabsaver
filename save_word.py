"""Functions necessary to record the word to vocabulary file if the user desires."""

import csv
import os.path

fieldnames = ['id', 'word']
filename = "myVocabs.csv"

def word_present(word):
    """Checks if the word is already present in the vocabulary record."""
    
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['word'] == word:
                return True
        
        return False

def save_word(word):
    "Add the word to vocabulary if user desires and not yet existing."

    if not word_present(word):
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            id = get_id()
            writer.writerow({'id': id, 'word': word})
            print("The word '{}' has been added.".format(word))

    else:            
        print("'{}' ALREADY exists.".format(word))

def create_vocab_file():
    """Create the vocab file and write the header keys."""

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        print("Vocabulary file has been created.")

def vocab_file_present():
    """Returns True if the vocab file already exist, else False."""

    return os.path.isfile(filename)

def get_id():
    """Returns the id based on the number of lines in vocabfile."""

    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        id = len(list(reader)) + 1
        return id



        
