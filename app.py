from flask import Flask, render_template
from routes import task_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

app.register_blueprint(task_routes)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)