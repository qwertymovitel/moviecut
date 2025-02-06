from flask import Blueprint, render_template, request, jsonify
from app.utils import search_movie_phrases

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    phrase = request.form.get('phrase')
    results = search_movie_phrases(phrase)
    return jsonify(results)