from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def similarity(file1,file2):
     file1 = file1
     file2 = file2
     documents = ()
     documents = documents + (file1,)
     documents = documents + (file2,)
    
     tfidf_vectorizer = TfidfVectorizer(stop_words = 'english')
     tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
     a =  cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
     return int(a[0][1]*100)
