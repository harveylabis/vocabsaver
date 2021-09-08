from bs4 import BeautifulSoup

def get_filename(word):
    first_letter = word[0].upper()
    filename = "definitions/" + first_letter + ".html"
    
    return filename

def define(word, filename):
    with open(filename) as f:
        print(filename, "opened")
        definitions = ''
        soup = BeautifulSoup(f, 'html.parser')
        for line in soup.body.find_all('p'):
            print(line.b.get_text())
            if line.b and line.b.get_text() == word:
                definitions = definitions + "\n  -" + line.get_text().strip(word)
            else:
                definitions = "No word found"

        return definitions

