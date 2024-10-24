from flask import Flask, render_template

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # This will look for 'index.html' in the 'templates' folder

if __name__ == '__main__':
    app.run(debug=True)