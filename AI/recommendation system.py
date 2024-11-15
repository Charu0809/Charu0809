# Predefined dataset of movies
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "The Godfather", "genre": "Crime"},
    {"title": "The Dark Knight", "genre": "Action"},
    {"title": "Forrest Gump", "genre": "Comedy"},
    {"title": "Inception", "genre": "Sci-Fi"},
    {"title": "Titanic", "genre": "Romance"},
    {"title": "Gladiator", "genre": "Action"},
    {"title": "The Notebook", "genre": "Romance"},
    {"title": "Pulp Fiction", "genre": "Crime"},
    {"title": "Interstellar", "genre": "Sci-Fi"},
]

def recommend_movies(preferred_genre):
    # Filter movies that match the preferred genre
    recommendations = [movie["title"] for movie in movies if movie["genre"].lower() == preferred_genre.lower()]

    # If there are recommendations, display them
    if recommendations:
        print(f"Based on your preference for {preferred_genre} movies, we recommend:")
        for movie in recommendations:
            print(f"- {movie}")
    else:
        print(f"Sorry, we don't have any {preferred_genre} movies in our database.")

# Main program
def recommendation_system():
    print("Welcome to the Movie Recommendation System!")
    print("Our genres: Drama, Crime, Action, Comedy, Sci-Fi, Romance")
    
    while True:
        preferred_genre = input("Enter your favorite genre (or type 'exit' to quit): ").strip()

        if preferred_genre.lower() == "exit":
            print("Thank you for using the recommendation system. Goodbye!")
            break
        
        recommend_movies(preferred_genre)

# Run the recommendation system
recommendation_system()