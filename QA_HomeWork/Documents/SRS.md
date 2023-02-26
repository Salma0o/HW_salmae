# *Software Requirements Specifications*

## Introduction
This Software Requirements Specification (SRS) document outlines the functional and non-functional requirements for a recipe management web application. The recipe management web application is a web-based platform that allows users to upload and store their favorite recipes, view and search other users’ recipes, and leave reviews on the recipes. The application will be developed using the Flask web framework in Python, and SQLAlchemy will be used as the object-relational mapping (ORM) tool.

## Requirements
### Functional Requirements

### Recipe Management

* The application must allow users to upload recipes with information such as recipe name, description, ingredients, instructions, publisher, publish date, and image (optional).
* The application must provide the ability for users to edit and delete their uploaded recipes.
* The application must allow users to view recipes uploaded by other users.
* The application must provide a search functionality to search for recipes based on name.
* The application must allow users to view a recipe's details such as recipe name, description, ingredients, instructions, publisher, publish date, and image (if available).
### Review Management

* The application must allow users to leave reviews on recipes.
* The application must allow users to rate recipes while leaving a review.
* The application must allow users to view reviews left by other users on a recipe.
## Non-functional Requirements
 
### Performance

* The application must handle concurrent users without slowdowns or crashes.
* The application must respond to user actions within a reasonable amount of time.
### Security

* The application must use secure protocols to transmit and store user data.
* The application must not allow unauthorized access to data.
### Usability

* The application must have a user-friendly interface that is easy to navigate.
* The application must have clear and concise error messages when errors occur.
System Design 
### Architecture

* The application will be developed using the Flask web framework in Python.
* SQLAlchemy will be used as the object-relational mapping (ORM) tool to interact with the database.
* The application will use a SQLite database to store user data and recipe information.
### User Interface

* The application will have a user-friendly interface that is easy to navigate.
* The interface will allow users to upload recipes, edit recipes, delete recipes, leave reviews, and view recipes.
### Database Design

* The SQLite database will have two tables: Recipes and Reviews.
* The Recipes table will have columns for id, recipe_name, description, ingredients, instructions, publisher, publish_date, and filename.
* The Reviews table will have columns for id, recipe_id, name, review_text, and rating.
## Conclusion
This SRS document outlines the functional and non-functional requirements for a recipe management web application. The application will allow users to upload and store their favorite recipes, view and search other users’ recipes, and leave reviews on the recipes. The application will be developed using the Flask web framework in Python, and SQLAlchemy will be used as the object-relational mapping (ORM) tool. The application will use a SQLite database to store user data and recipe information.