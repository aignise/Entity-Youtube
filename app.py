from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_trending_videos(language, country, section):
    url = "https://youtube-v2.p.rapidapi.com/trending/"
    querystring = {"lang": language, "country": country, "section": section}
    headers = {
        "X-RapidAPI-Key": "10293c49f1mshad7aa6bc1165ce9p19aed4jsnb7a764a892f7",
        "X-RapidAPI-Host": "youtube-v2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        trending_results = response.json()
        return trending_results
    else:
        return {"error": response.text}

def search_videos(query, language, order_by, country):
    url = "https://youtube-v2.p.rapidapi.com/search/"
    querystring = {"query": query, "lang": language, "order_by": order_by, "country": country}
    headers = {
        "X-RapidAPI-Key": "10293c49f1mshad7aa6bc1165ce9p19aed4jsnb7a764a892f7",
        "X-RapidAPI-Host": "youtube-v2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        search_results = response.json()
        return search_results
    else:
        return {"error": response.text}

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
