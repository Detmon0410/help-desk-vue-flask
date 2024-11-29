from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from views import ticket_blueprint

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Apply CORS globally to all routes, but restrict to certain origins
CORS(app, origins=["http://localhost:8080"])

# Automatically create the tables if they do not exist
with app.app_context():
    db.create_all()

# Register blueprints (MVC routing)
app.register_blueprint(ticket_blueprint)

@app.route('/')
def index():
    return "Welcome to the Ticket API!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
