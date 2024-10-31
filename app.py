from flask import Flask, render_template, request, redirect, url_for
import hashlib

app = Flask(__name__)

# In-memory storage for shortened URLs
url_mapping = {}

# Root route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to shorten the URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form['url']
    
    # Generate a short hash for the URL
    short_hash = hashlib.md5(original_url.encode()).hexdigest()[:6]
    short_url = request.host_url + short_hash
    
    # Store the mapping
    url_mapping[short_hash] = original_url
    
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
