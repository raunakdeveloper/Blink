from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

# In-memory storage for shortened URLs
url_mapping = {}

# Function to generate a random 4-character string
def generate_random_string(length=4):
    characters = string.ascii_letters  # Contains both lowercase and uppercase letters
    return ''.join(random.choice(characters) for _ in range(length))

# Root route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to shorten the URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    
    # Generate a random 4-character string for the URL
    random_string = generate_random_string()
    short_url = request.host_url + random_string
    
    # Store the mapping
    url_mapping[random_string] = original_url
    
    return render_template('shortened.html', short_url=short_url)

# Route to redirect to the original URL
@app.route('/<short_hash>')
def redirect_url(short_hash):
    original_url = url_mapping.get(short_hash)
    if original_url:
        return redirect(original_url)
    else:
        return "URL not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
