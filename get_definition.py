from bs4 import BeautifulSoup

def get_filename(word):
    """Find the appropriate file to search in and return its filename."""

    first_letter = word[0].upper()
    filename = "definitions/" + first_letter + ".html"
    
    return filename

def define(word, filename):
    """Returns the definition of the word."""

    with open(filename) as f:
        definitions = ''
        soup = BeautifulSoup(f, 'html.parser')
        for line in soup.body.find_all('p'):
            found = line.b.get_text().title() == word
            if found:
                definitions = definitions + "\n  -" + line.get_text().replace(word, '')
                
        return definitions

