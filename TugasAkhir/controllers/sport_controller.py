from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.sport import Sport
from extensions import db

sport_bp = Blueprint('sport', __name__)

@sport_bp.route('/sports')
def index():
    sports = Sport.query.all()
    return render_template('sports/index.html', sports=sports)

@sport_bp.route('/sports/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        
        sport = Sport(name=name, description=description)
        db.session.add(sport)
        db.session.commit()
        
        flash('Sport created successfully!', 'success')
        return redirect(url_for('sport.index'))
    
    return render_template('sports/create.html')

@sport_bp.route('/sports/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    sport = Sport.query.get_or_404(id)
    
    if request.method == 'POST':
        sport.name = request.form['name']
        sport.description = request.form['description']
        
        db.session.commit()
        flash('Sport updated successfully!', 'success')
        return redirect(url_for('sport.index'))
    
    return render_template('sports/edit.html', sport=sport)

@sport_bp.route('/sports/<int:id>/delete', methods=['POST'])
def delete(id):
    sport = Sport.query.get_or_404(id)
    db.session.delete(sport)
    db.session.commit()
    
    flash('Sport deleted successfully!', 'success')
    return redirect(url_for('sport.index')) 