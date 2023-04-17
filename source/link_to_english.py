# Import requests and BeautifulSoup modules
import requests
from bs4 import BeautifulSoup

# Define the web page url
url = input("Enter the URL to extract english from: ")

# Get the web page content using requests
response = requests.get(url)

# Parse the web page content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all the paragraphs in the web page
paragraphs = soup.find_all("p")

# Initialize an empty list to store the text
text = []

# Loop through the paragraphs and append their text to the list
for p in paragraphs:
  text.append(p.text)

# Join the text list with newlines
text = "\n".join(text)

# Open a file named input.txt in write mode
with open("input.txt", "w") as f:
  # Write the text to the file
  f.write(text)
  # Close the file
  f.close()
