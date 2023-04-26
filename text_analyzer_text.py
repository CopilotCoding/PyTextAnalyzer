import nltk
from textblob import TextBlob
import spacy
import gensim
import yake

# Load NLTK's English stopwords
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

# Load spaCy's English model
nlp = spacy.load('en_core_web_sm')

# Load the text file
with open('input.txt', 'r') as f:
    text = f.read()

# Tokenize the text using NLTK
tokens = nltk.word_tokenize(text)

# Remove stopwords using NLTK
tokens = [token for token in tokens if token.lower() not in stopwords]

# Normalize the tokens using NLTK
normalizer = nltk.stem.WordNetLemmatizer()
tokens = [normalizer.lemmatize(token.lower()) for token in tokens if token.isalpha()]

# Perform part-of-speech tagging using TextBlob
pos_tags = TextBlob(text).tags

# Perform named entity recognition using spaCy
doc = nlp(text)
entities = [(entity.text, entity.label_) for entity in doc.ents]

# Extract topics using Gensim
doc_repr = gensim.corpora.Dictionary([tokens])
doc_bow = doc_repr.doc2bow(tokens)
lda_model = gensim.models.LdaModel([doc_bow], num_topics=5, id2word=doc_repr)
topics = lda_model.print_topics()

# Extract keywords using YAKE
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

# Perform sentiment analysis using TextBlob
sentiment = TextBlob(text).sentiment

# Write the analysis results to a formatted text file
with open('output.txt', 'w') as f:
    f.write('Tokenized text:\n{}\n\n'.format(' '.join(tokens)))
    f.write('Part-of-speech tags:\n{}\n\n'.format('\n'.join('{}: {}'.format(tag, tag[1]) for tag in pos_tags)))
    f.write('Named entities:\n{}\n\n'.format('\n'.join('{}: {}'.format(entity, entity[1]) for entity in entities)))
    f.write('Topics:\n{}\n\n'.format('\n'.join('Topic {}: {}'.format(topic, topic[1]) for topic in topics)))
    f.write('Keywords:\n{}\n\n'.format('\n'.join('{}: {}'.format(keyword, keyword[1]) for keyword in keywords)))
    f.write('Sentiment:\n{}\n\n'.format('Polarity: {}, Subjectivity: {}'.format(sentiment.polarity, sentiment.subjectivity)))
    
    # Write a summary of the analysis
    f.write('Summary:\n')
    f.write('The text has been tokenized and normalized using NLTK.\n')
    f.write('Part-of-speech tags have been generated using TextBlob.\n')
    f.write('Named entities have been identified using spaCy.\n')
    f.write('The main topics in the text have been extracted using Gensim.\n')
    f.write('The most important keywords in the text have been extracted using YAKE.\n')
    if sentiment.polarity > 0:
        f.write('The text has a positive sentiment.\n')
    elif sentiment.polarity < 0:
        f.write('The text has a negative sentiment.\n')
    else:
        f.write('The text has a neutral sentiment.\n')
