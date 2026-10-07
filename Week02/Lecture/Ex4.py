f1 = open("hotels.txt")

ids_to_hotelNames = dict()

for line in f1:
    line = line.strip()
    info = line.split("\t")
    hotel_id = info[0]
    hotel_name = info[1]
    ids_to_hotelNames[hotel_id] = hotel_name

f1.close()


ids_to_ratings = dict()

f2 = open("reviews.txt")

for line in f2:
    line = line.strip()
    info = line.split("\t")
    hotel_id = info[1]
    rating = int(info[2])
    if hotel_id not in ids_to_ratings:
        ids_to_ratings[hotel_id] = [rating]
    else:
        ids_to_ratings[hotel_id].append(rating)

f2.close()

for k, v in ids_to_ratings.items():
    ids_to_ratings[k] = sum(v) / len(v) 


while len(ids_to_ratings) > 0:
    maxRating = max(ids_to_ratings.values())
    for k, v in ids_to_ratings.items():
        if v == maxRating:
            bestHotelID = k
            break
    print(ids_to_hotelNames[bestHotelID], maxRating)
    ids_to_ratings.pop(bestHotelID)