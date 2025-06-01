from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.team import Team
from models.sport import Sport
from extensions import db
from datetime import datetime

team_bp = Blueprint('team', __name__)

@team_bp.route('/teams')
def index():
    teams = Team.query.all()
    return render_template('teams/index.html', teams=teams)

@team_bp.route('/teams/create', methods=['GET', 'POST'])
def create():
    sports = Sport.query.all()
    
    if request.method == 'POST':
        name = request.form['name']
        sport_id = request.form['sport_id']
        coach = request.form['coach']
        founded_year = request.form['founded_year']
        
        team = Team(
            name=name,
            sport_id=sport_id,
            coach=coach,
            founded_year=founded_year
        )
        db.session.add(team)
        db.session.commit()
        
        flash('Team created successfully!', 'success')
        return redirect(url_for('team.index'))
    
    return render_template('teams/create.html', sports=sports, now=datetime.now())

@team_bp.route('/teams/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    team = Team.query.get_or_404(id)
    sports = Sport.query.all()
    
    if request.method == 'POST':
        team.name = request.form['name']
        team.sport_id = request.form['sport_id']
        team.coach = request.form['coach']
        team.founded_year = request.form['founded_year']
        
        db.session.commit()
        flash('Team updated successfully!', 'success')
        return redirect(url_for('team.index'))
    
    return render_template('teams/edit.html', team=team, sports=sports, now=datetime.now())

@team_bp.route('/teams/<int:id>/delete', methods=['POST'])
def delete(id):
    team = Team.query.get_or_404(id)
    db.session.delete(team)
    db.session.commit()
    
    flash('Team deleted successfully!', 'success')
    return redirect(url_for('team.index')) 