from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Bright welcome to your first Flask app!"

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
    
=======
    app.run(debug=True)
>>>>>>> 0b61d0b (quick save 💾)
