#-------------------------------------------------------------------------
# AUTHOR: Caitlyn Hue
# FILENAME: index.py
# SPECIFICATION: returns inverted index of a collection
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 10min
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd

# Reading the document collection
data = pd.read_csv("collection.csv")

# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    "homes": "home",
    "increases": "increase",
    "rising": "rise",
    "increasing": "increase",
    "sales": "sale", 
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    text = text.lower()
    text = text.replace(".", "")

    # Tokenizing the document
    # --> add your Python code here
    tokens = text.split()

    # Applying lemmatization
    # --> add your Python code here
    for token in range(len(tokens)):
        if tokens[token] in lemmas:
            tokens[token] = lemmas[tokens[token]]


    # Building the inverted index
    # --> add your Python code here
    for term in tokens:
        if term not in invertedIndex:
            invertedIndex[term] = []

        if docID not in invertedIndex[term]:
            invertedIndex[term].append(docID)


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here

for term in sorted(invertedIndex):
    print(term, ":", invertedIndex[term])