from starbase import Connection

c = Connection("127.0.0.1", "8001")

ratings = c.table('ratings')

if (ratings.exists()):
    print("dropping")
    ratings.drop()

ratings.create('rating')

print("parsing data")
ratingFile = open("/ml-100k/u.data", "r")

batch = ratings.batch()

for line in ratingFile:
    (userID, movieID, ratings, tiemstamp) = line.split()
    batch.update(userID, {'rating': {movieID: rating}})

ratingFile.close()

print("commiting to HBASE")
batch.commit(finalize=True)

print("done")
print("user 1")
print(ratings.fetch("1"))
print("user 33")
print(ratings.fetch("33"))
