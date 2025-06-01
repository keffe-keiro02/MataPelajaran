from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.event import Event
from models.sport import Sport
from models.team import Team
from extensions import db
from datetime import datetime

event_bp = Blueprint('event', __name__)

@event_bp.route('/events')
def index():
    events = Event.query.all()
    return render_template('events/index.html', events=events)

@event_bp.route('/events/create', methods=['GET', 'POST'])
def create():
    sports = Sport.query.all()
    teams = Team.query.all()
    
    if request.method == 'POST':
        title = request.form['title']
        sport_id = request.form['sport_id']
        team_id = request.form['team_id']
        event_date = datetime.strptime(request.form['event_date'], '%Y-%m-%dT%H:%M')
        location = request.form['location']
        description = request.form['description']
        
        event = Event(
            title=title,
            sport_id=sport_id,
            team_id=team_id,
            event_date=event_date,
            location=location,
            description=description
        )
        db.session.add(event)
        db.session.commit()
        
        flash('Event created successfully!', 'success')
        return redirect(url_for('event.index'))
    
    return render_template('events/create.html', sports=sports, teams=teams)

@event_bp.route('/events/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    event = Event.query.get_or_404(id)
    sports = Sport.query.all()
    teams = Team.query.all()
    
    if request.method == 'POST':
        event.title = request.form['title']
        event.sport_id = request.form['sport_id']
        event.team_id = request.form['team_id']
        event.event_date = datetime.strptime(request.form['event_date'], '%Y-%m-%dT%H:%M')
        event.location = request.form['location']
        event.description = request.form['description']
        
        db.session.commit()
        flash('Event updated successfully!', 'success')
        return redirect(url_for('event.index'))
    
    return render_template('events/edit.html', event=event, sports=sports, teams=teams)

@event_bp.route('/events/<int:id>/delete', methods=['POST'])
def delete(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    
    flash('Event deleted successfully!', 'success')
    return redirect(url_for('event.index')) 