def check_movie_year(movie):
    if movie["year"] < 2000:
        print("This movie was released before 2000")
        return None
    else:
        print("This movie was released after 2000")
        return movie["name"]

recent_movies = []

# my fav movies from command line assignment
movies_list = [
    {"name": "Into the Spider-Verse", "year": 2018},
    {"name": "Across the Spider-Verse", "year": 2023},
    {"name": "La La Land", "year": 2016},
    {"name": "Everything Everywhere All At Once", "year": 2022}
    {"name": "Fight Club", "year": 1999} #plus some movies from pre-2000
    {"name": "The Matrix", "year": 1999} ]

for movie in movies_list:
    result = check_movie_year(movie)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)
