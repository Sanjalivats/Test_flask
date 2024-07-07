from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(sentence1, sentence2):
    # Create the TfidfVectorizer and fit_transform the sentences
    vectorizer = TfidfVectorizer().fit_transform([sentence1, sentence2])
    
    # Convert the sparse matrix to dense
    vectors = vectorizer.toarray()
    
    # Compute the cosine similarity
    similarity = cosine_similarity(vectors)
    
    # Return the similarity between the two sentences
    return similarity[0][1]

