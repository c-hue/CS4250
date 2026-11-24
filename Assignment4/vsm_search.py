#-------------------------------------------------------------------------
# AUTHOR: Caitlyn Hue
# FILENAME: vsm_search.py
# SPECIFICATION: Builds Vector Space Model search engine and evaluates performance using test documents and queries
# FOR: CS 4250 - Assignment #4
# TIME SPENT: 40min
#-----------------------------------------------------------*/

# importing required libraries
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------------------------------
# 1. Load the input files
# ---------------------------------------------------------
# --> add your Python code here
docs = pd.read_csv("docs.csv")
queries = pd.read_csv("queries.csv")
judgments = pd.read_csv("relevance_judgments.csv")


# ---------------------------------------------------------
# 2. Build the TF-IDF matrix for the documents
# ---------------------------------------------------------
# Requirement: remove stopwords only
# --> add your Python code here
vectorizer = TfidfVectorizer(stop_words="english")
doc_vectors = vectorizer.fit_transform(docs["text"])


# ---------------------------------------------------------
# 3. Process each query and compute AP values
# ---------------------------------------------------------
# --> add your Python code here
ap_scores = []

for i, query in queries.iterrows():
    query_id = query["query_id"]
    query_vector = vectorizer.transform([query["query_text"]])
    scores = cosine_similarity(query_vector, doc_vectors)[0]
    
    ranked_indices = []
    for index in range(len(scores)):
        position = 0
        while position < len(ranked_indices) and scores[ranked_indices[position]] >= scores[index]:
            position += 1
        ranked_indices.insert(position, index)

    relevant_docs = set(judgments[(judgments["query_id"] == query_id) & (judgments["judgment"] == "R")]["doc_id"])

    # -----------------------------------------------------
    # 4. Compute Average Precision (AP)
    # -----------------------------------------------------
    relevant_count = 0
    precision_sum = 0

    for rank, doc_index in enumerate(ranked_indices, start=1):
        if docs.iloc[doc_index]["doc_id"] in relevant_docs:
            relevant_count += 1
            precision_sum += relevant_count / rank
    ap = precision_sum / len(relevant_docs) if relevant_docs else 0

    # store the AP value for this query (use any data structure you prefer)
    ap_scores.append((ap, query_id))

# ---------------------------------------------------------
# 5. Sort queries by AP in descending order
# ---------------------------------------------------------
# --> add your Python code here
ap_scores.sort(reverse=True)


# ---------------------------------------------------------
# 6. Print the sorted queries and their AP scores
# ---------------------------------------------------------
print("====================================================")
print("Queries sorted by Average Precision (AP):")
# --> add your Python code here
for ap, query_id in ap_scores:
    print(f"{query_id}: {ap:.4f}")

map_score = sum(ap for ap, query_id in ap_scores) / len(ap_scores)
print(f"Mean Average Precision (MAP): {map_score:.4f}")