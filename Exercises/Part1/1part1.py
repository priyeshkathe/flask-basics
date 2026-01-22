# Exercise 1.1: Change the return message
#   - Modify the return statement to say "Hello [Your Name]!"
#   - Save the file and refresh your browser (server auto-reloads!)

from flask import Flask  

app = Flask(__name__)  


@app.route('/')  
def home():
    return "Priyesh Kathe"  

if __name__ == '__main__':
    app.run(debug=True) 