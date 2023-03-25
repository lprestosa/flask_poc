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
        {'title': 'Song 2', 'artist': 'Artist 2', 'album': 'Album 2'}
        ]