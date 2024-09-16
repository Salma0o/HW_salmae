# Recipe Management System
A web application for managing and storing recipes. 
In this app I used Flask,
SQLAlchemy and Flask-Migrate for managing a
SQLite database and file uploads.
## `Features`
* Add a recipe with its name, description, ingredients, instructions, publisher, publish date and image.
* Display all the recipes and each recipe's detailed information including reviews.
* Add a review for a specific recipe.
* alter a specific field in the recipe.

## `Tests`
* manually check if added recipes appear in home page
* When deleting a recipe check if data is deleted from db
* check if reviews and rating are appearing in db
* check if recipe info appearing in db
* run tests after each debug in order to check how the app is affected
* ran the app and checked that it works as it supposed to
* search for recipes that exists and don't exist 
## `Usage`
* Clone the repository
* Install the required dependencies using pip install -r requirements.txt
* Run the following command to initiate the database flask db init
* Run the following command to perform migrations flask db migrate
* Run the following command to upgrade the database flask db upgrade
* Run the following command to start the application flask run
* The application will be running at http://localhost:5000/

## `html files`
### _index_
#### _Features:_
a home page using HTML, CSS and Jinja. The page features a navigation bar with two links, one to add a recipe and the other to search for a recipe. The center of the page displays a welcome message and an image grid of available recipes. 
### _add_profile_
#### _Features:_
managing and storing recipes. It allows users to add new recipes, view existing recipes, and edit or delete existing recipes.
### _recipe_info_
#### _Features:_
* Viewing a list of all recipes
* Viewing the details of a single recipe including ingredients, instructions, and reviews.
* Adding a new recipe
* Updating an existing recipe
* Deleting a recipe
* Adding a review to a recipe
### _alter_recipe_
#### _Features:_
The purpose of this file is 
to allow users to update existing recipe 
information such as the recipe name, description,
ingredients,
instructions, publisher, and publish date.

## `Notes`

* The allowed image extensions are .png, .jpeg, .jpg and .gif.
* The max content size for uploading an image is 16 MB.
