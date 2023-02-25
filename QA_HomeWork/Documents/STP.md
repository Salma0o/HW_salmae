# *Software Test Plan Document*

_****Recipe Web Application using Flask****_

## Description:
This web application allows users to browse, upload, and view recipe information. Users can view recipe details and reviews, and add reviews for a specific recipe. This web application is developed using Flask, a Python web framework. The application also uses SQLAlchemy for database management, and Flask-Migrate to manage database migrations. The application also includes file uploading for images of the recipe.

### Endpoints:

* / : Home route for displaying all available recipes.
* /add_data: route for adding a new recipe.
* /add: route for handling the submission of a new recipe.
* /display/<filename>: endpoint for displaying the uploaded image.
* /recipe_info/<recipe_id>: endpoint for displaying recipe information.
* /add_review: endpoint for managing the adding of reviews.
* /delete/<recipe_id>: route for deleting a recipe.
### Data Models:

* Recipes: A model for recipe information, including recipe name, description, ingredients, instructions, publisher, publish date, and filename for image of the recipe.
* Reviews: A model for review information, including the recipe id, name, review text, and rating.
### Dependencies:

* Flask: A Python web framework for building web applications.
* Flask-SQLAlchemy: A Flask extension for integrating SQLAlchemy with Flask.
* Flask-Migrate: A Flask extension for managing database migrations.
* SQLite: A lightweight and easy-to-use SQL database engine.
* os: A Python module for interacting with the operating system.
### Functionality:

* Home route: Displays all available recipes in the database.
* Add recipe route: Renders a form for adding a new recipe.
* Upload file: Enables uploading of images for each recipe.
* Display image endpoint: Enables display of the uploaded image.
* Display info endpoint: Enables display of the name and title on the image.
* Recipe info endpoint: Displays specific recipe details, including reviews and images.
* Add review endpoint: Enables users to add reviews for a specific recipe.
* Add rating endpoint: Enables users to add rating for a specific recipe.
* Delete recipe route: Allows a user to delete a specific recipe from the database.
* Alter recipe route: Allows a user to alter a specific recipe in the database.