import streamlit as st
import pickle
import pandas as pd
import os
import requests


def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/500x750?text=No+Image"


current_dir = os.path.dirname(os.path.abspath(__file__))
models_path = os.path.join(os.path.dirname(current_dir), 'models')

movies = pickle.load(open(os.path.join(models_path, 'movies.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(models_path, 'similarity.pkl'), 'rb'))


def recommend(movie_title):
    idx = movies[movies['title'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]
    
    rec_names = []
    rec_posters = []
    
    for i in scores:
        movie_id = movies.iloc[i[0]].id 
        rec_names.append(movies.iloc[i[0]].title)
        rec_posters.append(fetch_poster(movie_id))
        
    return rec_names, rec_posters


st.title("Movie Recommender")

selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    st.subheader("You might also like:")
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.caption(names[i])