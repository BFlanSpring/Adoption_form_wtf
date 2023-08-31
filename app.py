from flask import Flask, render_template, redirect, request  # Import the redirect function
from models import db, Pets, connect_db

from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secrete"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["WRF_CSRF_ENABLED"] = False

db.init_app(app)
connect_db(app)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/", methods=["GET"])
def redirect_to_list():
    """Redirect to list of pets"""

    return redirect("/pets")

@app.route("/pets", methods=["GET"])
def show_pet_list():
    """render list of pets"""
    pets = Pets.query.all()
    return render_template("pet_list.html", pets = pets)


@app.route('/pets/new', methods=['GET'])
def show_add_form():
    form = AddPetForm()  # Create an instance of the form
    return render_template("add_pet_form.html", form=form)



@app.route("/pets/new", methods=["POST"])
def process_add_form():
    """Process the add form, adding a new pet and going back to /pets"""
    
    form = AddPetForm()

    if form.validate_on_submit():
        name = request.form['name']
        species = request.form['species']
        image_link = request.form['image_link']
        age = request.form['age']
        available = request.form.get('available') == 'on'  
        notes = request.form['notes']

        pet = Pets(name=name, species=species, image_link=image_link, age=age, available=available, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect("/pets")
    else:
        return render_template("add_pet_form.html", form=form)

@app.route("/pets/<int:pet_id>", methods=["GET", "POST"])
def show_pet_info(pet_id):
    pet = Pets.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        form.populate_obj(pet)
        db.session.commit()
        print("Form submitted and database updated")  
        return redirect("/")
    else:
        print("Form validation failed:", form.errors) 
        return render_template("pet_info.html", pet=pet, form=form)




