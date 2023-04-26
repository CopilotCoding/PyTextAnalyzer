#!/bin/bash

# Install packages from requirements.txt
pip3 install -r requirements.txt

# Install textblob corpora
python3 -m textblob.download_corpora

# Wait for user input
read -p "Press Enter to exit"

# Exit the script
exit
