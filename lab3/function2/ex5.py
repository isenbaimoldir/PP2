from movie_list import movies
from ex3 import category
from ex4 import avr

name = input()
category_movie = category(name)
imbd = []
for i in category_movie:
    imbd.append(i)
print(avr(imbd))