movies = []

def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movie()
        elif user_input == 'f':
            find_movie()
        else:
            print("Unknown command-please try again.")

        user_input = input("\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, 'q' to quit: ")

def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    quality = input("Enter the movie quality: ")
    genre = input("Enter the genre of the movie: ")
    actors = input("Enter the major actors in the movie: "))
    year = int(input("Enter the year the movie was released: "))
    
    movie = {
        'name': name,
        'director': director,
        'quality': quality,
        'genre': genre,
        'actors': actors,
        'year': year
    }

    movies.append(movie)

def show_movie():
    print("These are the available available movies...")
    for display in movies:
        print(f"Name: {display['name']}")
        print(f"Director: {display['director']}")
        print(f"Movie Quality: {display['quality']}")
        print(f"Genre: {display['genre']}")
        print(f"Main Actors: {display['actors']}")
        print(f"Year of Release: {display['year']}")
        print("\n")

menu()
