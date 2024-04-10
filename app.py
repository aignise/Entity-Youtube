from flask import Flask, render_template, request
from function import get_trending_videos, search_videos
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trending', methods=['POST'])
def trending():
    language = request.form['language']
    country = request.form['country']
    section = request.form['section']
    trending_results = get_trending_videos(language, country, section)
    return render_template('results.html', results=trending_results, query_type='Trending Videos')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    language = request.form['language']
    order_by = request.form['order_by']
    country = request.form['country']
    search_results = search_videos(query, language, order_by, country)
    return render_template('results.html', results=search_results, query_type='Search Results')

if __name__ == '__main__':
    app.run(debug=True)
