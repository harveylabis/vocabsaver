import json
# try to use csv

filename = "myVocabs.json"
counter = 1

def save_word(word):
    if not present(word):
        data = {counter: word}
        with open(filename, 'a') as f:
            json.dump(data, f, indent=3)
            print("The word has been added.")
    else:            
        print("The word already exist.")

def present(word):
    with open(filename) as f:
        words = json.load(f)
        if word in words.values():
            return True
        return False



        
