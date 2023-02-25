 # *Software Test Description Document*

## Introduction:
The purpose of this document is to describe the testing approach and methods used to test the code for a Flask web application that is used to manage a collection of recipes. This document will describe the types of testing to be performed, the test environment, and the expected results of each test.

### The software test will focus on the following components of the web application:

* The Flask application that manages the recipe collection
* The database schema and data access layer
* The review submission feature and rating functionality
* The image upload and display feature
* Testing Objectives:
### The objectives of testing the web application are:

* To ensure that the application works as intended and meets the requirements specified
* To identify and report any issues, bugs, or defects in the application
* To ensure that the application is reliable, robust, and easy to use
* To ensure that the application is secure and does not have any vulnerabilities
* To ensure that the application is scalable and can handle large amounts of data

### Testing Types:
#### The following types of testing will be performed:

* *Unit Testing* : To test the individual components of the application, including the Flask routes and database access methods. This will be done using the PyTest testing framework.
* *Integration Testing* : To test the integration between the Flask application and the database, and to test the review submission and image upload features. This will be done using a combination of manual and automated testing methods.
* *System Testing* : To test the application as a whole, including all of its features and components, to ensure that it works as intended. This will be done using manual testing methods.
* *Security Testing* : To test the application for vulnerabilities and ensure that it is secure. This will be done using manual testing methods and automated tools like OWASP ZAP.

### Test Environment:
#### The following environment will be used for testing:

1. Operating System: Windows 10
2. Python Version: 3.9.5
3. Testing Framework: PyTest 6.2.5
4. Database: SQLite
5. Web Browser: Google Chrome
6. Test Data: Sample recipes, reviews, and images

### Test Cases:
#### The following test cases will be executed for each type of testing:

#####  **Unit Testing**:

------------


#####  *To verify if the home page loads successfully*
- ######  Test Objective : 
To ensure that the home page loads without errors
- ######  Test Steps :
1) Open the web application in the browser
2) Verify that the home page is displayed
Expected Result: The home page should be displayed without any errors or issues.

------------

#####  *To verify if the recipe information loads successfully*

 
######  Test Objective: 
To ensure that the recipe information is displayed without any errors
###### Test Steps:
1) Open the web application in the browser
2) Navigate to a recipe page
3) Verify that the recipe information is displayed correctly
###### Expected Result:
The recipe information should be displayed without any errors or issues.

------------


##### *To verify if the new recipe addition works correctly* 
######  Test Objective:
To ensure that a new recipe can be added to the database without any issues
###### Test Steps:
1) Open the web application in the browser
2) Click on the "Add New Recipe" button
3) Fill in the required information for the new recipe
4) Click on the "Submit" button
5) Navigate to the recipe page
###### Expected Result: 
The new recipe should be displayed on the recipe page without any errors or issues.

------------


#####  *To verify if the alter recipe works and the recipe is updated*
 
######  Test Objective: 
 To ensure that an existing recipe can be updated without any issues
###### Test Steps:
1) Open the web application in the browser
2) Navigate to the recipe page
3) Click on the "Edit" button for an existing recipe
4) Update the recipe information
5) Click on the "Submit" button
6) Navigate to the recipe page
###### Expected Result: 
The updated recipe should be displayed on the recipe page without any errors or issues.

------------


##### Integration Testing:

##### *verify if the info display works correctly when hovering over a picture*
###### Test Objective: 
To ensure that the recipe information is displayed correctly when hovering over a picture
###### Test Steps:
1) Open the web application in the browser
2) Navigate to the recipe page
3) Hover over an image
###### Expected Result: 
The recipe information should be displayed correctly without any errors or issues.

------------
#####   *User rating functionality*
###### Test Objective:
To verify if the user can use the rating functionality and choose 1-5 stars. If the user chooses no rating, one star will be added automatically.
###### Test Steps:
1) Log in to the web application
2) Navigate to a recipe page
3) Click on the rating stars
4) Verify that the selected rating is saved and displayed correctly
5) Repeat step 3 and choose no rating
6) Verify that one star is added automatically
###### Expected Result:
The user should be able to use the rating functionality and choose a rating from 1-5 stars. If the user chooses no rating, one star should be added automatically. The selected rating should be saved and displayed correctly.

------------


##### System Testing:


#####  *Test the search feature to ensure that wanted recipe is displayed correctly.*
###### Test Objective: 
To ensure that the search functionality works correctly
###### Test Steps:
1) Open the web application in the browser
2) Type a search query in the search bar
3) Click on the "Search" button
4) Verify that the search results are displayed correctly
###### Expected Result:
The search results should be displayed correctly without any errors or issues.

------------


##### Security Testing:

##### *Test the application for vulnerabilities and unauthorized files upload /adds a new recipe using different file types/sizes*
###### Test Steps:
1) Open the web application in the browser
2) Click on the "Add New Recipe" button
3) Fill in the required information for the new recipe
4) Attach files of different types and sizes
5) Click on the "Submit" button
6) Navigate to the recipe page
###### Expected Result: 
The new recipe should not be displayed on the recipe page .

------------
