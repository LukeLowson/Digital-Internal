from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note, Music
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route("/upload_music", methods=['GET', 'POST'])
def upload_music():
    if request.method == 'POST':
        file = request.form.get('file')
        
        if not file:
            flash('Please select a music file.', category='error')
        else:
            music = Music(file=file, user_id=current_user.id)
            db.session.add(music)
            db.session.commit()
            flash('Music posted!', category='success')
        
    return render_template("music.html", user=current_user)