from movie_list import movies

def score(movies):
    if movies["imdb"] > 5.5:
        return True
    else:
        return False
    
print(score(movies[4]))
print(score(movies[5]))
print(score(movies[7]))
print(score(movies[0]))