from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models1 import connect_db, Pet,db
from forms1 import AddPet, EditPet

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///WTForms_Exercise"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def get_homepage():
    """Return a homepage listing all the pets"""
    pets = Pet.query.all()
    return render_template('/pet_list.html', pets = pets)

@app.route('/pets/new', methods = ['GET', 'POST'])
def add_new_pets():
    """handling pets submission and getting form"""
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        species = form.species.data
        photo_url = form.photo_url.data
        notes = form.notes.data
        new_pet = Pet(name = name, age = age, species = species,
        photo_url = photo_url, notes = notes)

        with app.app_context():
            db.session.add(new_pet)
            db.session.commit()
            flash(f"{new_pet.name} Added")
            return redirect('/')

    else:
        return render_template('pet_add_form.html', form = form)

@app.route('/<int: pet_id>', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    """Edit a pet"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPet()
    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        
        with app.app_context():
            db.session.commit()
            flash (f'{pet.name} edited.')
        return redirect('/')
    
    else:
        return render_template('pet_edit_form.html', form = form)
