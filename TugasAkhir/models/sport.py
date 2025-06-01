from extensions import db

class Sport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    teams = db.relationship('Team', backref='sport', lazy=True)
    events = db.relationship('Event', backref='sport', lazy=True)

    def __repr__(self):
        return f'<Sport {self.name}>' 