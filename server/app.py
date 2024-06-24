from flask import Flask
from flask_migrate import Migrate
from models import db

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Migrate for database migrations
migrate = Migrate(app, db)

# Initialize Flask-SQLAlchemy
db.init_app(app)

# Index route
@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

# Run the application
if __name__ == '__main__':
    app.run(port=5555, debug=True)
