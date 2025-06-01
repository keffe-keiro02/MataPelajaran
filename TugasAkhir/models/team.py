from extensions import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sport_id = db.Column(db.Integer, db.ForeignKey('sport.id'), nullable=False)
    coach = db.Column(db.String(100))
    founded_year = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    events = db.relationship('Event', backref='team', lazy=True)

    def __repr__(self):
        return f'<Team {self.name}>' 