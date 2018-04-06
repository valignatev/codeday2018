from csv import DictReader

movies = []
with open('title.basics.tsv', 'r') as basics_file:
    basics = DictReader(basics_file, delimiter='\t')
    with open('title.ratings.tsv') as ratings_file:
        ratings = DictReader(ratings_file, delimiter='\t')

        for rating in ratings:
            b = next(basics)
            while b['tconst'] != rating['tconst']:
                b = next(basics)
            movies.append({
                'id': rating['tconst'],
                'title': b['primaryTitle'],
                'year': b['startYear'],
                'rating': float(rating['averageRating']),
                'votes': int(rating['numVotes']),
                'genres': b['genres'],
            })

# Files are here:
# https://datasets.imdbws.com

# Usage example
# import random
# random.choice(
#     [
#         m for m in movies
#         if m['rating'] > 9 and m['votes'] > 1000 and 'Sci-Fi' in m['genres']
#     ],
# )
