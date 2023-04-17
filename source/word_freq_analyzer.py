import os
import json

# Read the file contents select the encoding or default 'r'
with open("input.txt", encoding='utf-8') as file:
    text = file.read()

# Split the text into words
words = text.split()

# Count the frequency of each word
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Sort the dictionary by value
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

# Create a list of dictionaries for each word and its count
word_list = []
for word, count in sorted_word_freq.items():
    word_dict = {"word": word, "count": count}
    word_list.append(word_dict)

# Create a dictionary with the "words" and "total" keys
output_dict = {"words": word_list, "total": sum(sorted_word_freq.values())}

# Write the dictionary to a JSON file
with open("output.json", "w") as file:
    json.dump(output_dict, file, indent=4)
