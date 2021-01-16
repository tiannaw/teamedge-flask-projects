from flask import Flask, render_template, request, json, jsonify, current_app as app
from datetime import date
import os
import requests

app = Flask(__name__)

@app.route('/')
def about():
    return '<p>Main Flask Page</p>'

@app.route('/api/v1/tianna', methods = ['GET'])
def tianna_json():
    tianna_info = os.path.jon(app.static_folder, 'data', 'Tianna.json')
    with open(tianna_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)

@app.route('api/v1/movies')
def all_movies():
    movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_path, 'r') as raw_json:
        json_info = json.load(raw_json)
        return jsonify(json_info)

@app.route('/api/v1/movies/search_title', methods = ['GET'])
def search_title():
    json_info = ''
    movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_path, 'r') as raw_json:
        json_info = json.load(raw_json)
    results = []
    if 'title' in request.args:
        title = requests.args['title']

        for movie in json_info:
            if title in movie['title']:
                results.append(movie)

    if len(results) < 1:
        return "No Results Found"
    return render_template("index.html", results = results)

@app.route('/index')
def index():
    return render_template('/index.html')



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')




