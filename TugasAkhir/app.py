from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sportshub.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    # Import models
    from models.sport import Sport
    from models.team import Team
    from models.event import Event

    # Import controllers
    from controllers.sport_controller import sport_bp
    from controllers.team_controller import team_bp
    from controllers.event_controller import event_bp

    # Register blueprints
    app.register_blueprint(sport_bp)
    app.register_blueprint(team_bp)
    app.register_blueprint(event_bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True) 