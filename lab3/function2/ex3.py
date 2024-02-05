from movie_list import movies

def category(category_name):
   return [i for i in movies if category_name == i["category"]]

name = input()
category_movie = category(name)
for i in category_movie:
    print(i)