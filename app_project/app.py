from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
import os

# initialize Flask application
app = Flask(__name__)

# enable debug mode
app.debug = True

# database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'

# upload folder path
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# maximum file size to upload
app.config['MAX_CONTENT'] = 16 * 1024 * 1024

# allowed file extensions for upload
ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg', 'gif']


# helper function to check if a file is allowed for upload
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# initialize SQLAlchemy database object
db = SQLAlchemy(app)


# create Recipe model
class Recipes (db.Model):
    # define columns
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)
    ingredients = db.Column(db.String, unique=False, nullable=False)
    instructions = db.Column(db.String, unique=False, nullable=False)
    publisher = db.Column(db.String(20), unique=False, nullable=False)
    publish_date = db.Column(db.Integer, unique=False, nullable=False)
    filename = db.Column(db.String(100), unique=False, nullable=True)

    # display representation of the object
    def __repr__(self):
        return f"Title: {self.recipe_name}, Publisher: {self.publisher}"


# create Review model
class Reviews(db.Model):
    # define columns
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(20), unique=False, nullable=False)
    review_text = db.Column(db.String, unique=False, nullable=False)
    rating = db.Column(db.Integer, unique=False, nullable=True)

    # display representation of the object
    def __repr__(self):
        return f"Name:{self.name},Content:{self.review_text}"


# initialize Flask-Migrate
migrate = Migrate(app, db)


# home route
@app.route("/")
def home():
    # fetch all recipes from database
    recipes_data = Recipes.query.all()
    # render home page with recipes data
    return render_template("index.html", recipes_data=recipes_data)


# Route for adding a new recipe
@app.route("/add_data")
def add_data():
    # Render the add_profile.html template
    return render_template("add_profile.html")

# Route for handling the submission of a new recipe
@app.route("/add", methods=["POST","GET"])
def recipes_management():
    if request.method =="POST":
        # Get the recipe information from the form
        recipe_name = request.form.get("recipe_name")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        publisher = request.form.get("publisher")
        publish_date = request.form.get("publish_date")
        file = request.files.get("filename")
        # Check if the file is an allowed type
        if allowed_file(file.filename):
            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        # Create a new recipe row in the database
        recipe_row = Recipes(recipe_name=recipe_name, description=description, ingredients=ingredients,
                             instructions=instructions,publisher=publisher,publish_date=publish_date,
                             filename=file_name)
        db.session.add(recipe_row)
        db.session.commit()
        return redirect("/")


# Define the endpoint to display the uploaded image
@app.route("/display/<filename>")
def display_image(filename):
    # redirect the user to the static folder to retrieve the image
    return redirect(url_for('static', filename='uploads/' + filename))


# Define the endpoint to display the recipe information
@app.route('/recipe_info/<recipe_id>')
def recipe_info(recipe_id):
    # retrieve the specific recipe and its reviews from the database
    recipe_specific = Recipes.query.get(recipe_id)
    # Retrieve the reviews for the recipe based on the recipe id
    reviews_specific = Reviews.query.filter(Reviews.recipe_id == recipe_id)
    # render the recipe_info.html template with the specific recipe and reviews information
    return render_template("recipe_info.html", recipe_specific=recipe_specific, reviews_specific=reviews_specific)


# Define the endpoint to manage the adding of reviews
@app.route("/add_review", methods=["POST"])
def review_management():
    # check if the request method is POST
    if request.method == "POST":
        # retrieve the name, review text, and recipe id from the form data
        name = request.form.get("name")
        # Retrieve the review text from the form
        review_text = request.form.get("review_text")
        # Retrieve the rating  from the form
        rating = request.form.get("rating")
        # Retrieve the recipe id from the form
        recipe_id = request.form.get("recipe_id")
        # Create a new review instance with the name, review text, and recipe id
        review_row = Reviews(name=name, review_text=review_text, recipe_id=recipe_id, rating=rating)
        # Add the review instance to the database session
        db.session.add(review_row)
        # Commit the changes to the database
        db.session.commit()
        return redirect("/")


@app.route("/delete/<int:id>")
def erase(id):
    data = Recipes.query.get(id)
    filename = data.filename
    os.remove(f"{app.config['UPLOAD_FOLDER']}{filename}")
    db.session.delete(data)
    reviews_specific = Reviews.query.filter(Reviews.recipe_id == id)
    for review in reviews_specific:
        db.session.delete(review)
    db.session.commit()
    return redirect("/")


@app.route("/alter_recipe/<int:id>",methods=["POST","GET"])
def alter_recipe(id):
    if request.method == "POST":
        data = Recipes.query.get(id)
        recipe_name = request.form.get("recipe_name")
        description = request.form.get("description")
        ingredients = request.form.get("ingredients")
        instructions = request.form.get("instructions")
        publisher = request.form.get("publisher")
        publish_date = request.form.get("publish_date")
        file = request.files.get("filename")
        if allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file_name = file.filename
        if request.form.get("recipe_name"):
            data.recipe_name = recipe_name
        if request.form.get("description"):
            data.description = description
        if request.form.get("ingredients"):
            data.ingredients = ingredients
        if request.form.get("instructions"):
            data.instructions = instructions
        if request.form.get("publisher"):
            data.publisher = publisher
        if request.form.get("publish_date"):
            data.publish_date = publish_date
        if request.files.get("file_name"):
            data.filename = file_name
        db.session.commit()
        return redirect(url_for('recipe_info', recipe_id=id))
    else:
        return render_template("alter_recipe.html")


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        search = request.form["searchbar"]
        recipe_specific = Recipes.query.filter(Recipes.recipe_name.ilike(search)).all()[0]
        reviews_specific = Reviews.query.filter(Reviews.recipe_id == recipe_specific.id)
    return render_template("recipe_info.html", recipe_specific=recipe_specific, reviews_specific=reviews_specific)


if __name__ == "__main__":
    app.run()

