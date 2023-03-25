from unicodedata import category
import urllib.request
import sys
import random
# Since I couldn't run successfully, I added the two lines below from Chatgpt to address the error
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.gutenberg.org/cache/epub/64317/pg64317.txt'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) # for testing

# The codes below were learned from our class session under analyze_book.py; 
def process_file(text, skip_header):
    """Makes a histogram that contains the words from a file.
    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = text.split('/n')

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = ''.join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')
        line = line.replace(
            chr(8212), ' '
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THIS PROJECT'):
            break


def total_words(hist):
    return sum(hist.values())
    # Remove the following line
    return len(histogram)


def different_words(hist):
    """Returns the number of different words in a histogram."""
    total = 0
    for freq in hist.values():
        if freq == 1:
            total += 1
    return total

stopwords = ['this','and','a','of','to']

# I am not sure if I did this part correctly
def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.
    hist: map from word to frequency
    returns: list of (frequency, word) pairs
    """
    res = [] 

    for word in hist:
        freq = hist[word]
        res.append((freq, word))

    res.sort(reverse = True)
    return res


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common (hist)
    print("The most common words here are: ")
    for freq, word in t [ :num]:
        print(word, freq)


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    sub = {}
    for key in d1:
        if key not in d2:
            sub[key] = None
    return sub


def random_word(hist):
    """Chooses a random word from a histogram.
    The probability of each word is proportional to its frequency.
    """
    t = []
    for word, freq in hist.items():
        t.extend ([word]*freq)

        return random.choice(t)
    

def main():
    hist = process_file(text, skip_header=True)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[2900:3000]:
        print(word, '\t', freq)

if __name__ == '__main__':
    main()
