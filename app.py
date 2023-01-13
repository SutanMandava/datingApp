from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    api_key = '3ce4ee1f53be94e2efdddc3ba1cb3f0d'
    username1 = request.form['username1']
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={username1}&api_key={api_key}&format=json'
    response = requests.get(url)
    data = response.json()
    artist_list1 = []
    for artist in data['topartists']['artist']:
        artist_list1.append(artist["name"])
    overlapping_artists = {}
    while True:
        username2 = input("Enter a last.fm username to match with or type 'q' to quit: ")
        if username2 == 'q':
            break
        url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={username2}&api_key={api_key}&format=json'
        response = requests.get(url)
        data = response.json()
        artist_list2 = []
        for artist in data['topartists']['artist']:
            artist_list2.append(artist["name"])
        overlapping_artists[username2] = len(set(artist_list1).intersection(artist_list2))
    most_overlap_username = max(overlapping_artists, key=overlapping_artists.get)
    return render_template('match.html', most_overlap_username=most_overlap_username)

if __name__ == '__main__':
    app.run()
