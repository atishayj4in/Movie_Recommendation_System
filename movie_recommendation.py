import streamlit as st
import pickle
import pandas as pd
import requests
st.set_page_config(layout="wide")
def fetch_poster(movie_name):
    response = requests.get('http://www.omdbapi.com/?t={}&apikey=b99ee9b9'.format(movie_name))
    data=response.json()

    return data['Poster']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    similar_movie = []
    similar_movie_poster = []
    for i in movies_list:
        similar_movie_id = i[0]
        similar_movie.append(movies.iloc[i[0]].title)
        similar_movie_poster.append(fetch_poster(movies.iloc[i[0]].title))
    return similar_movie, similar_movie_poster


movies_dict = pickle.load(open('./movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("./similarity.pkl", 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Choose a movie to get similar recommendations.",
    movies['title'].values,
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
