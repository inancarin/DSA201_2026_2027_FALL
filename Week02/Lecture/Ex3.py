f = open("movies.txt")

allLines = f.readlines()

f.close()

movies = set()
for line in allLines:
    line = line.strip() # remove "\n" character from the end
    info = line.split(", ")
    for movie in info[1:]:
        movie = movie.strip()
        movies.add(movie)

print("The number of unique movies is:", len(movies))

for i in range(5):
    if len(movies) == 0:
        break
    minElem = min(movies)
    print(minElem)
    movies.remove(minElem)