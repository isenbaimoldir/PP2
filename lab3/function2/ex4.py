from movie_list import movies

def avr(movies):
    imdb_score = []
    total = 0
    for i in movies:
        imdb_score.append(i["imdb"])
    for i in range(len(imdb_score)):
        total += imdb_score[i]
    return total / len(imdb_score)

print(avr(movies))