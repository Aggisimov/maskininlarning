import sys
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def build_model():
    movies = pd.read_csv("movies.csv")

    movies["genres_list"] = movies["genres"].apply(lambda x: x.split("|"))
    
    # Convert genres into binary matrix
    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(movies["genres_list"])
    
    return movies, genre_matrix


def recommend(movie_title, movies, genre_matrix, top_n=5):
    
    matches = movies[movies["title"].str.contains(movie_title, case=False)]
    
    if len(matches) == 0:
        print("Film not found")
        return
    
    
    idx = matches.index[0]
    
    # Get vector for selected movie
    movie_vector = genre_matrix[idx].reshape(1, -1)

    # Compute similarity
    similarity = cosine_similarity(movie_vector, genre_matrix)[0]
    
    # Sort movies by similarity, best match at the top
    similar_indices = np.argsort(similarity)[::-1]
    
    # Remove the selected movie
    similar_indices = similar_indices[similar_indices != idx][:top_n]
    
    print("\nInput:", movies.iloc[idx]["title"])
    print("\nRecommendations:")
    
    for i in similar_indices:
        print("-", movies.iloc[i]["title"])


if __name__ == "__main__":
    # Check input
    if len(sys.argv) < 2:
        print("Usage: python main.py 'movie name'")
    else:
        movie_name = sys.argv[1]

        
        movies, genre_matrix = build_model()
        recommend(movie_name, movies, genre_matrix)