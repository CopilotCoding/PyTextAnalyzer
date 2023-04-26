#!/bin/bash

# Install packages from requirements.txt
pip3 install -r requirements.txt

# Install textblob corpora
python -m textblob.download_corpora

# Install spacy efficient english trained model
python -m spacy download en_core_web_sm

# Wait for user input
read -p "Press Enter to exit"

# Exit the script
exit
