from movie_list import movies
from to_refer import category
from to_refer import avr

name = input()
category_movie = category(name)
imbd = []
for i in category_movie:
    imbd.append(i)
print(avr(imbd))