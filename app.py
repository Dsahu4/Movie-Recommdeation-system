import streamlit as st


import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_lst = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_lst:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

movies_list = pickle.load(open('movies_dict.pkl','rb'))
movies =  pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie :blue[Recommander]')

Selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

if st.button('Recommend'):
    recommendation = recommend(Selected_movie_name)
    for i in recommendation:
        st.write(i)













