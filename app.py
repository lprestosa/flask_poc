from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    # Sample contact information
    first_name = 'John'
    last_name = 'Doe'
    email = 'johndoe@example.com'
    phone = '555-555-1234'
    return render_template('contact.html', first_name=first_name, last_name=last_name, email=email, phone=phone)

@app.route('/songs')
def songs():
    # Sample song data
    songs = [
        {'title': 'Song 1', 'artist': 'Artist 1', 'album': 'Album 1'},
        {'title': 'Song 2', 'artist': 'Artist 2', 'album': 'Album 2'},
        {'title': 'Song 3', 'artist': 'Artist 3', 'album': 'Album 3'}
    ]
    return render_template('songs.html', songs=songs)

@app.route('/albums')
def albums():
    # Sample album data
    albums = [
        {'title': 'Album 1', 'artist': 'Artist 1', 'year': 2020},
        {'title': 'Album 2', 'artist': 'Artist 2', 'year': 2019},
        {'title': 'Album 3', 'artist': 'Artist 3', 'year': 2018}
    ]
    return render_template('albums.html', albums=albums)

@app.route('/artists')
def artists():
    # Sample artist data
    artists = [
        {'name': 'Artist 1', 'genre': 'Pop'},
        {'name': 'Artist 2', 'genre': 'Rock'},
        {'name': 'Artist 3', 'genre': 'Country'}
    ]
    return render_template('artists.html', artists=artists)

if __name__ == '__main__':
    app.run(debug=True)
