import streamlit as st
import pickle
import requests
import time

# Load movie data and similarity matrix
movies_df = pickle.load(open('movies.pkl', 'rb'))  # Ensure this is a DataFrame
similarity = pickle.load(open('similarity.pkl', 'rb'))  # Cosine similarity matrix

# TMDb API details
API_KEY = "5528de46eee10fe55e11d4f1ea5c9bd7"
BASE_URL = "https://api.themoviedb.org/3/movie/"

# Create a session to reuse connections
session = requests.Session()


def fetch_poster(movie_id):
    """Fetches the poster URL for a movie using its ID."""
    url = f"{BASE_URL}{movie_id}?api_key={API_KEY}"

    for attempt in range(3):  # Retry up to 3 times
        try:
            response = session.get(url, timeout=10)  # Use session for connection pooling
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()
            poster_path = data.get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500/{poster_path}"
            else:
                return "https://via.placeholder.com/300x450?text=No+Poster+Available"
        except requests.exceptions.RequestException as e:
            if attempt < 2:  # Retry on first 2 attempts
                st.warning(f"Retrying fetching poster for movie ID {movie_id}... ({attempt + 1}/3)")
                time.sleep(1)  # Short delay before retrying
            else:
                st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
                return "https://via.placeholder.com/300x450?text=Error+Fetching+Poster"


def recommend(movie):
    """Recommends movies based on a given movie title."""
    try:
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        similar_movies = sorted(
            list(enumerate(distances)), reverse=True, key=lambda x: x[1]
        )[1:6]

        recommended_movies = []
        posters = []

        for i in similar_movies:
            movie_id = movies_df.iloc[i[0]].id
            recommended_movies.append(movies_df.iloc[i[0]].title)
            posters.append(fetch_poster(movie_id))
            time.sleep(0.5)  # Throttle requests to avoid rate limiting

        return recommended_movies, posters
    except IndexError:
        st.error("Movie not found in the dataset. Please check your selection.")
        return [], []
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return [], []


# Extract movie titles for the dropdown
movies_list = movies_df['title'].values

# Streamlit App
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations", movies_list
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    if names and posters:
        st.write("Recommended Movies:")
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            if idx < len(names):
                with col:
                    st.text(names[idx])
                    st.image(posters[idx], use_container_width=True)
