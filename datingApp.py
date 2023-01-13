import requests

api_key = '3ce4ee1f53be94e2efdddc3ba1cb3f0d'

username1 = str(input("Enter your last.fm username: "))

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
print(f'{most_overlap_username} is the best match for you!')
