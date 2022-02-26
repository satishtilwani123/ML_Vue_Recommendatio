from flask import Flask, jsonify, request
import pickle
import os
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np

# pip install -U flask-cors

# initialize our Flask application
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cosine_sim = pickle.load(open('cosine_similarity.pickle', 'rb'))

# Import & Load File
movies = pd.read_csv('MovieGenre.csv', sep=',', encoding='latin-1')

# Get Indices
titles = movies['Title']
indices = pd.Series(movies['Title'].index, index=movies['Title'])


@app.route("/")
@cross_origin()
def helloWorld():
    return "Recommendation System!"

def genre_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return movie_indices

@app.route("/recommend", methods=["GET"])
def Movies_Recommend():
    arr = []
    if request.method == 'GET':
        movie_name = str(request.args.get('MovieName'))
        recommendlist = genre_recommendations(movie_name)
        for i in recommendlist:
            arr.append({"id": i, "name": movies['Title'][i], "rating": movies['IMDB Score'][i], "poster": movies['Poster'][i], "genre": movies['Genre'][i]})

    return jsonify(arr)


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)


