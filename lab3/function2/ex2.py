from movie_list import movies

def sublist(movies):
    sub = []
    for i in movies:
        if i["imdb"] > 5.5:
            sub.append(i)
    return sub  

sub = sublist(movies)
    
for i in sub:
    print(i)