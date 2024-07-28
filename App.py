import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Sample data
books = pd.DataFrame({
    'book_id': [1, 2, 3, 4, 5],
    'title': ['Book A', 'Book B', 'Book C', 'Book D', 'Book E'],
    'author': ['Author A', 'Author B', 'Author C', 'Author D', 'Author E']
})

ratings = pd.DataFrame({
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5],
    'book_id': [1, 2, 3, 1, 2, 1, 2, 4, 3, 4, 5, 2, 3],
    'rating': [5, 4, 3, 4, 5, 5, 4, 2, 5, 4, 3, 5, 4]
})

# Function to get book title from book_id
def get_title(book_id):
    return books.loc[books['book_id'] == book_id, 'title'].values[0]

# Function to recommend books based on user ratings
def recommend_books(user_id, num_recommendations=3):
    # Create a pivot table
    user_book_ratings = ratings.pivot(index='user_id', columns='book_id', values='rating').fillna(0)

    # Compute cosine similarity between users
    user_similarity = cosine_similarity(user_book_ratings)

    # Get the index of the given user_id
    user_idx = user_id - 1

    # Get the similarity scores for the given user_id
    sim_scores = list(enumerate(user_similarity[user_idx]))

    # Sort the users based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top similar users
    sim_scores = sim_scores[1:num_recommendations+1]

    # Get the book ids of the top similar users
    similar_users = [i[0]+1 for i in sim_scores]
    similar_users_ratings = ratings[ratings['user_id'].isin(similar_users)]

    # Calculate the mean rating for each book
    book_recommendations = similar_users_ratings.groupby('book_id')['rating'].mean().sort_values(ascending=False).head(num_recommendations)
    recommended_books = book_recommendations.index.tolist()

    return [get_title(book_id) for book_id in recommended_books]

# Streamlit application
st.title("Book Recommendation System")

user_id = st.number_input("Enter User ID:", min_value=1, max_value=5, step=1)

if st.button("Recommend"):
    recommendations = recommend_books(user_id)
    st.write("Recommended Books:")
    for book in recommendations:
        st.write(book)
