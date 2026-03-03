# Define dictionary of movies and their information
import json

movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}
def add_movie():
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the name of the director: ")
    year = input("Enter the release date of the movie (YYYY): ")
    actors = input("Enter the names of the actors (separated by commas) : ")
    actors_list = actors.split(", ")
    movies[title] = {
        "genre": genre,
        "director": director,
        "year": int(year),
        "actors": actors_list
    }
    print(f"{title} has been added to the database. ")

#Edit movie information

def edit_movie():
    title = input("Enter the movie name you want to edit: ")
    if title in movies:
        print("What information do you want to edit?")
        print("1. Genre")
        print("2. Director")
        print("3. Release Date")
        print("4. Actors")
        choice = input("Enter your choice: ")

        if choice == "1":
            new_genre = input("Enter the new genre: ")
            movies[title]["genre"] = new_genre
            print(f"{title}'s genre has been updated. \n")
        elif choice == "2":
            new_director = input("Enter the new director: ")
            movies[title]["director"] = new_director
            print(f"{title}'s director has been updated. \n")
        elif choice == "3":
            new_release_date = input("Enter the new release date: ")
            movies[title]["year"] = new_release_date
            print(f"{title}'s new release date has been updated. \n")
        elif choice == "4":
            new_actor = input("Enter the new actor: ")
            movies[title]["actors"] = new_actor
            print(f"{title}'s actor has been updated. \n" )
        else:
            print("invalid.\n")
    else:
        print("Movie not found.\n")

def delete_movie():
    title = input("Enter the movie title for deletion: ")

    if title in movies:
        del movies[title]
        print(f"{title} has been deleted from the database.\n")
    else:
        print("Movie not found.\n")

# view all movies
def view_movies():
    if len(movies) == 0:
        print("No movies found.\n")
    else:
        for movie in movies:
            print(f"Movie: {movie}")
            for key, value in movies[movie].items():
                print(f"{key}: {value}")
            print()

#search movies database
def search_movie():
    title = input("Enter the movie title: ")

    if title in movies:
        print(f"Movie: {title}")
        for key, value in movies[title].items():
            print(f"{key}: {value}")
        print()
    else:
        print("No movies found.\n")

def save_data():
    with open("movies.json", "w") as file:
        json.dump(movies, file, indent=4)
    print("Movie data has been saved.\n")

def load_data():
    global movies
    try:
        with open("movies.json", "r") as file:
            movies = json.load(file)
        print("Data has been loaded.\n")
    except FileNotFoundError:
        print("No saved file found.\b")

#start menu
def menu():
    while True:
        print("Movie Management")
        print("1. Add Movie")
        print("2. Edit Movie")
        print("3. Delete Movie")
        print("4. View all movies")
        print("5. Search Movie")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")

        choice = input("Enter choice: ")
        print()

        if choice == "1":
            add_movie()
        elif choice == "2":
            edit_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            view_movies()
        elif choice == "5":
            search_movie()
        elif choice == "6":
            save_data()
        elif choice == "7":
            load_data()
        elif choice == "8":
            print("exiting program.")
            break
        else:
            print("invalid\n")

menu()