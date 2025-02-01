# Main entry point to start the Flask app 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/hkrn_recruitment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

# Import routes (to be created)
from routes import initialize_routes
initialize_routes(api)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
