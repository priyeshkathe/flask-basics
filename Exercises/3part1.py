# Exercise 1.3: Add a second route
#   - Add another function with @app.route('/about')
#   - Return something like "This is the about page"
#   - Visit http://localhost:5000/about in your browser

from flask import Flask  

app = Flask(__name__)  


@app.route('/')  
def home():
    return "Priyesh Kathe"  

@app.route('/about')
def new():
    return "This is the About Page"

if __name__ == '__main__':
    app.run(debug=True) 