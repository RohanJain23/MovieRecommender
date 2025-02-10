import streamlit as st
import pickle

movies_df = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = movies_df['title'].values

# Recommendation function
def recommend(movie_name):
    index = movies_df[movies_df['title'] == movie_name].index[0]
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_indices:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

st.title('Movie Recommender System')

movie_name = st.selectbox(
    'What is your preferred movie?',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(movie_name)
    st.subheader("Recommended Movies:")
    for rec in recommendations:
        st.write(rec)
