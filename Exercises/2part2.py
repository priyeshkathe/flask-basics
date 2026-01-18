# Exercise 1.2: Return HTML instead of plain text
#   - Change the return to: return "<h1>Hello Flask!</h1><p>This is HTML</p>"
#   - Notice how the browser renders it as formatted HTML

from flask import Flask  

app = Flask(__name__)  


@app.route('/')  
def home():
    return "<h1>Hello Flask!</h1><p>This is HTML</p>"

if __name__ == '__main__':
    app.run(debug=True)