import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

def analyze_text(file_path):
    # Read the text from the input file
    try:
        with open(file_path, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return

    # Tokenize the text into sentences and words
    sentences = nltk.sent_tokenize(text)
    words = word_tokenize(text)

    # Remove stop words from the words list
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Detect the sentiment of each sentence
    sia = SentimentIntensityAnalyzer()
    sentences_sorted = [{'index': i, 'sentence': sentence, 'score': sia.polarity_scores(sentence)['compound']} for i, sentence in enumerate(sentences)]
    for sentence in sentences_sorted:
        if sentence['score'] < -0.05:
            sentence['label'] = 'negative'
        elif sentence['score'] > 0.05:
            sentence['label'] = 'positive'
        else:
            sentence['label'] = 'neutral'

    # Calculate the overall sentiment score of the text data
    scores = [sentence['score'] for sentence in sentences_sorted]
    overall_score = sum(scores) / len(scores)

    # Extract the most common keywords from the words list
    keywords = [word for word, count in Counter(words).most_common(10)]

    # Write the summary of the analysis to the output file in a more descriptive and useful format
    output = {
        'overall_score': overall_score,
        'keywords': keywords,
        'sentences': sentences_sorted
    }
    with open('output.json', 'w') as f:
        json.dump(output, f, indent=4, sort_keys=False, ensure_ascii=False)

    return

# Call the analyze_text() function with the input file path
analyze_text('input.txt')
