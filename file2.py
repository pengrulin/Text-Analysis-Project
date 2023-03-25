import urllib.request

url = 'http://www.gutenberg.org/ebooks/730.txt.utf-8'
with urllib.request.urlopen(url) as f:
    text = f.read().decode('utf-8')
    print(text) # for testing