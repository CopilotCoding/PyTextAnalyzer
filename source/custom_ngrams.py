import re
import collections
import json

def clean_text(text):
    # Remove unwanted characters and words
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    return text

def generate_ngrams(text, n):
    # Generate n-grams of length n
    words = text.split()
    ngrams = zip(*[words[i:] for i in range(n)])
    return [' '.join(ngram) for ngram in ngrams]

def count_ngrams(ngrams):
    # Count the frequency of each n-gram
    return collections.Counter(ngrams)

def filter_ngrams(ngram_counts, min_freq, max_freq):
    # Filter out n-grams that occur less frequently than min_freq
    return {ngram: count for ngram, count in ngram_counts.items() if min_freq <= count <= max_freq}

def sort_ngrams(ngram_counts):
    # Sort the n-grams by frequency and length
    return sorted(ngram_counts.items(), key=lambda x: (-x[1], len(x), x))

def write_ngrams(ngram_counts, filename):
    # Write the n-grams and their frequencies to a JSON file
    data = {'ngrams': []}
    for ngram, count in ngram_counts:
        data['ngrams'].append({'ngram': ngram, 'count': count})
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    # Read the input text file
    with open('input.txt', 'r') as f:
        text = f.read()
    
    # Clean the text
    text = clean_text(text)
    text_length = len(text)

    # Generate n-grams of length nmin to nmax
    nmin = 1
    nmax = 100 # text_length
    ngrams = []
    for n in range(nmin, nmax+1):
        ngrams += generate_ngrams(text, n)

    # Count the frequency of each n-gram
    ngram_counts = count_ngrams(ngrams)

    # Filter out n-grams that occur less frequently than min_freq
    min_freq = 2
    max_freq = 100000
    filtered_ngrams = filter_ngrams(ngram_counts, min_freq, max_freq)
    
    # Sort the n-grams by frequency and length
    sorted_ngrams = sort_ngrams(filtered_ngrams)

    # Write the resulting n-grams and their frequencies to a JSON file
    write_ngrams(sorted_ngrams, 'output.json')
