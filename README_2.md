# Just Ramen Website #
---
[View the live project here.](https://ms3-online-cookbook.herokuapp.com/)

This is the Just Ramen website. It is designed to be responsible and accessible on multiple devices, making it easy to navigate for users on every device.

![Hero Screenshot](static/img/readme/hero.png)

## Contents ##
---

* UX
    * [Project Summary](#project-summary)
    * [User Stories](#user-stories)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Icons](#icons)
        * [Colors](#colors)
* [Wireframing](#wireframing)
* [Features](#features)
    * [Features that have been developed](#developed)
    * [Features that will be implemented in the future](#implemented)
* [Technologies](#technologies)
* [Defensive Design](#defensive)
    * [Feature Testing](#ftest)
    * [Defensive Design Testing](#dtest)
* [Issues](#issues)
* [Deployment](#deployment)
* [Credit](#credits)

## User Experience (UX) ##
---
<a name="project-summary"></a>
### Project Summary ###

* Santé! is a collaborative platform where registered users can share cocktail recipes from all around the world, discover new cocktails and upgrade their knowledge and skills about mixology.
* Santé! is also accessible to guest users without the possibility to post their own recipes or "like" a cocktail recipe.

<a name="user-stories"></a>
### User Stories ### 

Guest user

* As a guest user of Santé! I want to find this website when I search for cocktail recipes.
* As a guest user of Santé! I want to browse and understand the concept of the website easily.
* As a guest user of Santé! I want to be able to access this website from different devices easily.
* As a guest user of Santé! I want be entertained and discover/search for new cocktail recipes.
* As a guest user of Santé! I want to find out more about the website on social media.
* As a guest user of Santé! I want to see the popularity of the cocktail recipes.
* As a guest user of Santé! I want to suscribe to the newsletter.
* As a guest user of Santé! I want the clear possibility to register to the website.

Registered user

* As a registered user of Santé! I want be able to log in with my username and password.
* As a registered user of Santé! I want to get a visual confirmation when I am logged in.
* As a registered user of Santé! I want to be able to create and add cocktail recipes to the website.
* As a registered user of Santé! I want to get a visual confirmation when I added a recipe.
* As a registered user of Santé! I want to be able to search for specific recipes.
* As a registered user of Santé! I want to be able to "like" a cocktail recipe.
* As a registered user of Santé! I want to be able to edit my cocktail recipes.
* As a registered user of Santé! I want to be able to edit my profile.
* As a registered user of Santé! I want to get a visual confirmation when I edited my cocktail.
* As a registered user of Santé! I want to get a visual confirmation when I edited my profile.
* As a registered user of Santé! I want to be able to delete my cocktail recipes.
* As a registered user of Santé! I want to be able to delete my profile.
* As a registered user of Santé! I want to see who has published a cocktail recipe that isn't mine.
* As a registered user of Santé! I want to be able to add a picture and relevant informations to my profile.
* As a registered user of Santé! I want to be able to delete my profile.

Admin

* As an admin of Santé! I want all of the above options but I would also be able to access and delete all the recipes from other users.
* As an admin of Santé! I want to be able to create and delete cocktail categories.
* As an admin of Santé! I want to be able to view how many users are registered on the website and delete users if necessary.

<a name="requirements"></a>

### Research ###

* To create Santé! I researched several popular Food and Beverages websites such as [**Epicurious**](https://www.epicurious.com/), [**Delish**](https://www.delish.com/) and [**Cocktail Flow**](https://cocktailflow.com/).
* I also checked which website had the most interesting cocktail recipes (classics and originals) and my choice went to: **Goop**, **Liquor.com** and **TheSpruceEats**.
* The language of the website is English with a few words in French to stick with the French origin of the app's name. The french used is grammatically correct as I am French.
* Most of these websites usually include a story around the cocktail and I decided to turn it only in a small description as I as a user usually skip most of the text and prefer to have the ingredients right away. I did a small poll among my friends on **Instagram** about the Story vs. No Story topic on recipe website and results showed 89% (on 145 people) in favor of No Story. The people have spoken, No story it is.

<a name="design-choices"></a>

### Design Choices ##
---

<a name="framework"></a>

### Frameworks ###

* Bootstrap 4 to build the front-end. I used the [**Small Business Template**](https://startbootstrap.com/template/small-business) for the landing page structure as well as the [**Business Template**](https://startbootstrap.com/template/business-frontpage) for the profile page. I wanted to learn more about Bootstrap and its classes. I tried to implement these as much as possible.
* Micro framework [**Flask**](https://flask.palletsprojects.com/en/1.1.x/), to build the backend.

<a name="fonts"></a>

### Fonts ###

* For the titles and the website logo I decided to go for the [**Goggle Fonts**](https://fonts.google.com/) cursive "Lobster" for a playful and sophisticated look and paired it with my all-time favourite sans-serif Google fonts 'Montserrat' for readability on all other elements.

<a name="icons"></a>

### Icons and Images ###

* All icons used on this website are taken from [**Font Awesome**](https://fontawesome.com/).
* I have decided to choose icons for the buttons Edit/View/Delete on the cocktail cards in the profile and in recipe template for a better user understanding.
* The Favicon used for this website is from [Favicon.io](https://favicon.io/).

<a name="colors"></a>

### Colors ###

* I choose to work with a very momocromatic color scheme of light and dark yellows, inspired by the palette below. 
* The **warning** Bootstrap color class fits perfectly with that color scheme, so I used it for the buttons and some titles.
* I choose yellow because it is a color that increase cheerfulness and stimulate the user mentally. This website is all about a positive and fun message in these pretty dark times, and I thought yellow was the right amount of playfulness.
* The buttons have their own color code: Red for all delete functionnalities, Green for all Edit functionnalities, Yellow for the Add functionnalities as well as the View cocktail buttons. Only the admin has a blue "Add Category" button and a black "Check users" buttons as these are functionnalities only the Admin has.
* The gradients used for the background of the Newsletter section, the detail section of the cocktail recipe pages and the category section is the **Citrus Peel** gradient from [**UiGradients**](https://uigradients.com/).
![Color Scheme](static/img/readme/color_scheme.png) 

<a name="responsive"></a>

### Responsiveness ###
 
![responsive](static/img/readme/responsive.png) 

* Santé is completely responsive thanks to **Bootstrap** and custom CSS media queries. I also used the website [**Am I Responsive**](http://ami.responsivedesign.is/) to test on all major sizes as well as **Google Chrome Dev** to check all other devices available.
* I also tested this project on several devices : 
    - Macbook Air 13'
    - Iphone 6s
    - Ipad Pro
    - Samsung Galaxy S10
    - Desktop screen Dell 2560x1440
    - Lenovo Legion Performance 15'6

<a name="wireframing"></a>

## Wireframing ##
---
For **wireframing** I used the tool [**Balsamiq**](https://balsamiq.com/).

View my wireframes [here](static/img/wireframe.pdf).

* As one can see, my wireframe changed quite a bit (but not completely) since I started. I added the following features:
    - Pagination
    - Manage users
    - Profile panel and CRUD

* A few design sections have changed for a better user experience:
    - I removed the search box in the navigation bar and left it only in the All cocktails page.
    - The navigation bar is not centered anymore.
    - The featured cocktails section contains 6 cocktails and not 8.
    - I removed the newsletter from the footer and gave it it's own section on the landing page.
    - The footer is social media oriented as the navigation bar is fixed, there is no need for repetition (in my opinion).
    - The layout of the cocktail recipes is different.
    - I changed the rating functionnality for a like functionnality.

<a name="features"></a>
## Features ## 
---

<a name="developed"></a>
### Implemented Features ###

*Features for all users (guest/registered/admin)*

**Navigation bar**

* The navigation bar is completely responsive and is not made with Bootstrap as this is part of a [**Youtube tutorial by Bedimcode**](https://www.youtube.com/watch?v=Lf6zONwYeec).
* The Navigation Bar displays the logo of the website and the options "Home", "Cocktail Recipes", "Log In" and "Register" when the user is not logged in.

**Animated landing page**

![Hero animation](static/img/readme/hero_animation.gif)

* For this feature I coded along and adapted this [**Youtube tutorial by Bedimcode**](https://www.youtube.com/watch?v=Lf6zONwYeec). I made my own elements to animate using [**Maya**](). You can see in my CSS/HTML/JS files that I have credited the owner of the tutorial as well as I've left the CSS and SASS classes  as they are in the tutorial.
* I wanted to implement this feature because I wanted to learn a bit more about the GSAP library and I really enjoyed coding along this tutorial.

**It's Apero Time**

* This feature is a pretty straightforward section of the website explaining the goal and concept of Santé!. 
* I added a Bootstrap carousel that display images on demand or automatically for a visually more engaging user experience.

**Newsletter**

![newsletter](static/img/readme/newsletter.png)

* This feature allows the user, no matter if he is registered or not, to subscribe to the website's newsletter. The email given by the user is registered in the database in a collection called "subscriptions" and is separate from the "users" collection.
* The user needs to enter a valid email address for the registration.

**Featured Recipes**

![featured](static/img/readme/featured.png)

* This feature is an introduction to some of the cocktail recipes showcased on the website and are cocktail recipes created in the database by the admin only. (6 firsts only)
* The recipes are displayed on responsive cards with a hover effect (not available on mobile).

**Suggested Cocktails**

![suggested](static/img/readme/suggested.png)

* This feature is placed at the bottom of a cocktail recipe page and suggests to the user 3 random cocktails of the same category as the cocktail currently being checked by the user.


**Cocktail Recipes**

![Cocktails](static/img/readme/cocktails.gif)

* The recipe page showcases all the recipes submitted by the registered users and the admin. All recipes are displayed in responsive cards including a picture, a category and a name all submitted by the user/author of the recipe.
* If the user is the author of the recipe or the admin and is logged in, the buttons "edit and "delete" appears. They are not visbible if the author or admin is not logged in.
* The recipes are displayed on responsive cards with a hover effect (not available on mobile).

**Search box**

![Search Box](static/img/readme/search_box.png)

* This feature allows the user to search through keywords specific cocktails in the Cocktails.html.
* It allows the user to search through text and/or categories combined.
* When no results match the search, the text "No Result Found" is displayed.

**Pagination**

![pagination](static/img/readme/pagination.png)

* This feature helps to display the cocktail cards on several pages to avoid crowding the page with too much content.
* Pagination is also present on the admin user list for the same reasons. It displays 10 users per page.
* Each page displays 9 cocktail cards maximum per page in the all cocktails page and 6 on the profile page.

**Individual Recipe Page**

![cocktail](static/img/readme/cocktail.gif)

* This page allows the user to view a custom recipe including
    - Cocktail Name 
    - Category Name
    - Cocktail date
    - Cocktail Description 
    - Cocktail Image 
    - Cocktail Image Credentials 
    - Cocktail Preparation Time 
    - Cocktail Level 
    - Cocktail Ingredients 
    - Cocktail Instructions
    - Cocktail Date Submission
    - Cocktail Likes
    - Cocktail Author's Name

* All the data is stored in collections on MongoDB Atlas database and passed thropugh HTML using flask.
* The user needs to be registered to "like" a recipe

**Register**

* The registration form takes the informations of the user to create an account : 
    - the user's email address,
    - The user's username,
    - The user's password,
    - The user's picture,
    - The user's location,
    - The user's level.
* Only the user image input is optional. If the field is left blank or has an invalid/broken image url, a default image will be displayed.
* The passwords  are hashed and protected using the import "generate_password_hash, check_password_hash" from werkzeug security.
* All that data is stored in the collection "users" on MongoDB Atlas database.

**Log In**

* When a user is already registered, he/she/them uses the log in form to access their account. The user needs their password and username to log in.

*Features visible for registered users*

**Profile**

![Profile](static/img/readme/profile.png)

* The user's profile showcases their personal informations: username, profile picture, level and location.
* The section "Your cocktails" displays the cocktail recipes submitted by the user. The user can also create a recipe by clicking on a specified button next to the recipe cards.
* Each recipe card has 3 buttons : View, Edit, Delete.

**Edit Profile (CRUD)**

![Edit Profilew](static/img/readme/edit_profile.png)

* The user can edit their profile informations by clicking on the green "Edit" button in the dedicated profile card.
* This feature allows the user to edit their picture, level and location. The user cannot edit their username and password (yet)
* The user needs to click on the yellow "Submit" button to edit the changes.
* After clicking on the button the user will be redirected towards their updated profile page with an alert confirming the changes made.

**Delete Profile (CRUD)**

![Delete Profile](static/img/readme/delete_profile.png)

* The user can delete their profile by clicking on the red "Delete" button in the dedicated profile card.
* This feature allows the user to permanently delete their profile.
* When the button is clicked a modal will ask for confirmation to avoid any unfortunate mistake to be made.
* If the confirmation button is clicked, the profile is permanently deleted and the now guest user will be redirected to the registration page with an alert confirming the changes.

**Add a Cocktail (CRUD)**

![Add Cocktail](static/img/readme/add_cocktail.png)

* This feature allows the user to submit a custom recipe through a form including the following required blank fields and options:
    - Cocktail name (blank)
    - Category (option)
    - Cocktail Description (blank)
    - Cocktail Image (blank)
    - Cocktail Image Credentials (blank)
    - Cocktail Preparation Time (option)
    - Cocktail Level (option)
    - Cocktail Ingredients (blank)
    - Cocktail Instructions (blank)

* The date is automatically generated through the Python import datetime and is not to be selected in the form.
* If the image url is broken or invalid, a default image will be displayed.
* After clicking on the submit button, the user can see the new recipe page topped with a validation flash message. The recipe will then appear in the user's profile.
* This feature is accessible through the navigation bar and the user's profile.

**Edit a Cocktail (CRUD)**

![Edit Cocktail](static/img/readme/edit_cocktail.png)

* The user can edit the choosen recipe only when logged in.
* The form passes the informations previously submitted for more clarity and can all be changed.
* To submit these new information, the user needs to click on the "submit" button at the bottom of the page.
* After clicking on the submit button, the user can see the updated recipe page topped with a validation flash message. The recipe will be updated in the user's profile.
* The user cannot edit the date on which the recipe was created.
* The edit  functionnality can be accessed through the recipe cards on the cocktails.html page, profile.html and the specific cocktail/cocktail_id.html.

**Delete a Cocktail (CRUD)**

![Delete Cocktail](static/img/readme/delete_cocktail.png)

* The user can delete the choosen recipe only when logged in.
* The delete functionnality can be accessed through the recipe cards on the cocktails.html page, profile.html and the specific cocktail/cocktail_id.html.
* When the delete button is clicked, a modal asks confirmation to prevent the user from accidentally deleting the recipe.
* If confirmed, the recipe is deleted forever.

**Like a Cocktail (CRUD)**

![Like](static/img/readme/like_button.gif)

* The user can only like a recipe when logged in.
* The user can only like a recipe once.
* When clicked the recipe page reloads and adds to the like count.
* A message on top of the recipe confirms the "like" to the user.

**Log Out**

![Logout](static/img/readme/logout.png)

* The user can access this functionnality through the navigation bar.
* When clicked, a modal appears and ask for confirmation.
* If confirmed, the user is redirected towards the landing page with an alert confirming that the user is logged out.

*Features only for the admin (all of the above plus the following)*

**Manage Categories (CRUD)**

![category](static/img/readme/categories.png)
![Add Catergory](static/img/readme/add_category.png)
![Edit Category](static/img/readme/edit_category.png)
![Delete Category](static/img/readme/delete_category.png)

* The admin can edit, delete and view all cocktail categories through buttons displayed on the category cards.
* The admin can access the Categories through their profile.

**Manage Users (CRUD)**

![userslist](static/img/readme/users_list.png)
![delete user](static/img/readme/delete_user.png)
![delete confirmation](static/img/readme/delete_confirmation.png)

* The admin can view how many users are registered on the website and check them by username.
* The admin is excluded from the list.
* The admin can delete any of the users and their associated cocktail recipes registered through a red delete button displayed next to the user name on the list.
* The admin can access the Categories through their profile.

**Profile**

* All recipes are displayed on the admin dashboard.
* The admin can view and delete any of the recipe. 
* The admin cannot edit a recipe.
* The admin can edit their profile information like a registered user.

<a name="implemented"></a>

### Future implemented features ###

* "Unlike" functionnality
* Comment section for registered user
* Functionnality to consult other member profiles for registered user
* Share recipe functionnality.
* Possibility to have more than one admin.
* Reverse search from ingredients to cocktails.

<a name="technologies"></a>

## Technologies, libraries and tools used ##

**Front-End**
* [Bootstrap](https://bootstrap4.com/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Font-Awesome](https://fontawesome.com/)
* [Google fonts](https://fonts.google.com/)
* [GSAP](https://greensock.com/gsap/)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [Javascript](https://www.javascript.com/)
* [Maya](https://www.autodesk.com/products/maya/overview)
* [SCSS](https://sass-lang.com/)

**Back-end**
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [MongoDB](https://www.mongodb.com/1)
* [Python](https://www.python.org/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)

**Deployment**
* [Heroku](https://dashboard.heroku.com/)
* [Git](https://git-scm.com/)
* [Github](https://github.com/)
* [Gitpod](https://gitpod.io/)

**Testing**
* [JSHint](https://jshint.com/) (JS file passed validator)
* [PEP8 online](http://pep8online.com/)
* [W3C HTML Validator](https://validator.w3.org/) (all pages passed validator)
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) (css file passed validator)


<a name="defensive"></a>

## Defensive Design  ##
---
### Feature Testing ###
---
<a name="ftest"></a>

**GSAP Animation and Navigation Bar**

*  As any user, navigate to the landing page of Santé! Is the "index" template correctly rendered?
*  Are all text elements and images appearing on the screen?
* Move the cursor of your mouse over the navigation bar links. Are the images in the hero section moving?
* Move the cursor of your mouse over the hero image. Is the image moving in 3D?

**Featured Cocktails**

* As any user, scroll down to the bottom of the index page, are the "Featured cocktails" cards rendered?
* Are the pictures, name, category and username rendered?
* If yes, click on the yellow "try" button, is the cocktail template correctly rendered?
* Are all informations displayed on the page?

**All Cocktails**

* As a guest user, navigate to the "All cocktail" page through the navigation bar. Is the all cocktail template rendered correctly?
* Is the search box and the Category dropdown present?
* Are all cocktail cards rendered correctly and display these informations:
    - the cocktail picture
    - the cocktail name
    - the cocktail category
    - the cocktail author.
* If yes, log into your account as an admin or registered user and re-navigate to the All cocktails page.
* Is the search box and the Category dropdown present?
* Are all cocktail cards rendered correctly and display these informations:
    - the cocktail picture
    - the cocktail name
    - the cocktail category
    - the cocktail author.
* On the cocktails you have previously created, are the "edit" and "delete" icons present?

**Pagination**

* As a guest/registered user, navigate to the All cocktails page. Is the template rendered correctly?
* Is there 9 cocktail cards on the page?
* Go to the bottom of the page. Is the pagination section correctly rendered?
* Click on all pages. Are the cocktail cards correctly rendered?
* Is there 9 cocktail cards per pages?


**Cocktail Recipe**

* As a guest user, select a cocktail card from the All Cocktails page and click on the "try" button. Is the cocktail template rendered correctly?
* Are all these informations rendered correctly:
    - the cocktail name
    - the cocktail author
    - the date
    - the category name
    - the cocktail picture
    - the cocktail picture credits
    - the cocktail description
    - the like button
    - the preparation time
    - the servings
    - the level
    - the instructions
    - the ingredients.
* As a registered user, select a cocktail card from the All Cocktails page and click on the "try" button. Is the cocktail template rendered correctly?
* Are all these informations rendered correctly:
    - the cocktail name
    - the cocktail author
    - the Date
    - the category name
    - the cocktail picture
    - the cocktail picture credits
    - the cocktail description
    - the like button
    - the preparation time
    - the servings
    - the level
    - the instructions
    - the ingredients.
* Are the "Delete" and "Edit" buttons displayed and clickable?
* As a registered user, select one of your cocktail card from your profile page and click on the "try" button. Is the cocktail template rendered correctly?
* Are all these informations rendered correctly:
    - the cocktail name
    - the cocktail author
    - the Date
    - the category name
    - the cocktail picture
    - the cocktail picture credits
    - the cocktail description
    - the like button
    - the preparation time
    - the servings
    - the level
    - the instructions
    - the ingredients.
* Are the "Delete" and "Edit" buttons displayed and clickable?
* At the bottom of the recipe page, is the suggested cocktails section displayed ?
* Is there 3 recipes or less displayed ?
* Are they all from the same category than the recipe being checked ?
* Is the cocktail currently being reviewed excluded from that list ?
* If yes, refresh the page, have the cocktails changed (if there are more than 3 cocktails in that category)?
* If yes, is the cocktail currently being reviewed still excluded ?

**Search box**

* As any user, navigate to the All cocktail page through the navigation bar. Is the All cocktails template rendered correctly?
* If yes, is the search box present?
* Enter a word in the search box and click on the yellow search button. Is the result of your search showing in the card section?
* If no result was found, is the next "No result found" showing?
* Reset your search. Is the All cocktails template rendered correctly?
* Select an option in the category option menu. Are all categories displayed?
* If yes, select a category. Is the result of the search correctly displayed?
* If no result was found, is the text "No result found" displayed?
* Reset your search. Is the All cocktails template rendered correctly?
* Type a word in the search text box and select a category in the menu and click on the search button. Is the result of the search correctly displayed?
* If no result was found, is the text "No result found" displayed?

**Log In and Profile**

* If the user is already registered, access the Login page through the navigation bar.
* Is the login form and background correctly rendered?
* Try to submit an empty form. Is the bootstrap form validation tooltip shows in the empty fields?
* Try to fill the fields with a password and username under 5 characters or above 15 characters. Is the Bootstrap form validation tooltip showing in the incorrectly filled fields?
* Try to fill the form with a wrong password/username. Is an alert informing you that your password/username is incorrect?
* Fill the form with correct password/username. Is your profile page displayed correctly?
* Is your profile card displaying your profile picture, username, level and location?
* If the Image url input field was left blank, is the default profile picture displayed?
* Is the dashboard correctly displaying the "Your cocktails" with its content and "Add cocktail" sections?
* Click on the green "Edit Profile" button. Is the Edit Profile template rendered correctly?
* Make one change in one of the fields and click submit. Are you redirected towards your profile page?
* Is the alert present?
* Is the change made in your profile displayed?
* Click the red "Delete profile". Is the modal rendered? 
* Click the "Cancel" modal button. Are you back on your profile page?
* Reclick on "Delete Profile". On the modal, click the "Delete" button. Is the register page rendered?
* Is the delete alert present?

**Register**

* Navigate to the Register page through the navigation bar and click. Is the registration form and its background correctly rendered?
* Try to submit an empty form. Is the bootstrap form validation tooltip shows in the empty fields?
* Try to fill the fields with a password and username under 5 characters or above 15 characters. Is the Bootstrap form validation tooltip showing in the incorrectly filled fields?
* Try to fill the form with an already existing username. Is an alert informing you that the username already exists?
* Fill the form correctly and click on the "Register" button. Is the Profile page correctly rendered?
* Is the "Your cocktail" section empty?

**Your cocktails**

* In your profile page, is the "Your cocktail" section displayed?
* As a registered user, if you have submitted cocktails previously, are the cocktail cards showing?
* Are the buttons "View"(yellow), "Edit"(green), and "Delete"(red) displayed?
* Is the picture, name and category of the cocktal showing?
* is the pagination displayed at the bottom of the page if you have more than 6 cocktails submitted?
* As an admin, are your cocktails as well as all registered user cocktails showing in "Your cocktail" section?
* As an admin, do you haven "View","Edit" and "Delete" buttons on your cocktail recipes and "View" and "Delete" buttons for other users cocktail recipes?

**Submit a cocktail (Admin/Registered user)**

* Navigate to the form through your profile page. Is the yellow button "Add a cocktail" rendered?
* Click on the button, is the "Add a cocktail" form correctly?
* Are all fields empty, except for the option fields?
* Try to submit the form with empty fields. Is the Bootstrap form validation tooltip showing ?
* Fill the form accordingly and respecting the instructions. Click on the submit button. Is the cocktail page rendered correctly?
* Is the alert present?
* Are all informations previously entered displayed?

**Edit a cocktail**

*Method 1*
* When logged in, go to your profile. If the cocktail cards are correctly rendered, is the green "Edit" icon correctly rendered?
* If yes, click on it. Is the "Edit your cocktail" template correctly rendered?
* Are all fields filled with previous informations about the cocktail?
* If yes, try to make a change and click on "Save Changes". Is the cocktail template correctly rendered?
* Is the confirmation alert present?
* Did the change occur?

*Method 2*

* When logged in go to the "All cocktails" page through the navigation bar. Is the "All Cocktails" template correctly rendered?
* If all cocktail cards are rendered, is the green "Edit" Icon present?
* If yes, click on it. Is the "Edit your cocktail" template correctly rendered?
* Are all fields filled with previous informations about the cocktail?
* If yes, try to make a change and click on "Save Changes". Is the cocktail template correctly rendered?
* Is the confirmation alert present?
* Did the change occur?

*Method 3*

* When logged in go to the "All cocktails" page through the navigation bar. Is the "All Cocktails" template correctly rendered?
* If all cocktail cards are rendered, select one of your cocktail and click on the try button. Is the cocktail correctly rendered?
* If yes, is the green "Edit" button rendered?
* If yes, click on it. Is the "Edit your cocktail" template correctly rendered?
* Are all fields filled with previous informations about the cocktail?
* If yes, try to make a change and click on "Save Changes". Is the cocktail template correctly rendered?
* Is the confirmation alert present?
* Did the change occur?

**Delete a cocktail**

*Method 1*
* When logged in, go to your profile. If the cocktail cards are correctly rendered, is the red "Delete" icon correctly rendered?
* If yes, click on it. Is the modal "Delete your cocktail" correctly rendered?
* If yes, click on cancel. Did the nodal disappear and no change happened?
* Click again on the red "Delete" Icon. Is the modal correctly rendered?
* If yes, click on delete. Is the "all cocktail" template correctly rendered?
* If yes, is the confirmation alert present?
* Did the cocktail disappear?

*Method 2*

* When logged in go to the "All cocktails" page through the navigation bar. Is the "All Cocktails" template correctly rendered?
* If all cocktail cards are rendered, is the red "Delete" Icon present?
* If yes, click on it. Is the modal "Delete your cocktail" correctly rendered?
* If yes, click on cancel. Did the nodal disappear and no change happened?
* Click again on the red "Delete" Icon. Is the modal correctly rendered?
* If yes, click on delete. Is the "all cocktail" template correctly rendered?
* If yes, is the confirmation alert present?
* Did the cocktail disappear?

*Method 3*

* When logged in go to the "All cocktails" page through the navigation bar. Is the "All Cocktails" template correctly rendered?
* If all cocktail cards are rendered, select one of your cocktail and click on the try button. Is the cocktail template correctly rendered ?
* Is the red "Delete" button rendered ?
* If yes, click on it. Is the modal "Delete your cocktail" correctly rendered ?
* If yes, click on cancel. Did the nodal disappear and no change happened ?
* Click again on the red "Delete" Icon. Is the modal correctly rendered?
* If yes, click on delete. Is the "all cocktail" template correctly rendered ?
* If yes, is the confirmation alert present ?
* Did the cocktail disappear ?

**Manage Categories (Admin only)**

* As an admin, log into your profile. Is the profile template rendered?
* If yes, is the "Manage category" section present?
* If yes, click on the green "Check it" button. is the "Categories" template correctly rendered?
* Are all category cards displayed including name and "Edit" / "delete" buttons?
* If yes click on "Edit". Is the "Edit Category" template rendered correctly?
* Is the previous category name present?
* Change the name and click on "save changes". Is the "Categories" template correctly rendered?
* Is the confirmation alert present?
* Did the change occur in the selected cotegory card?
* If yes, select another category card and click on the red "Delete" button. Is the modal correctly rendered?
* If yes, click on cancel. Did the modal disappear and no change happened?
* Click again on the red "Delete" Icon. Is the modal correctly rendered?
* If yes, click on delete. Is the "categories" template correctly rendered?
* If yes, is the confirmation alert present?
* Did the category disappear?

**Manage Users (Admin only)**

* As an admin, log into your profile. Is the profile template rendered?
* If yes, is the "Manage users" section present?
* If yes, click on the black "Check users" button. is the "Users_list" template correctly rendered?
* Is the number of registered user correctly displayed?
* Are usernames and delete buttons displayed?
* Is the admin excluded from the list?
* Is the pagination displayed if more than 10 users are registered ?
* If yes click on the red trashcan, is the delete modal correctly displayed?
* Is the username, text,"cancel" button and "delete" button correctly displayed?
* If yes, click on cancel. Did the modal disappear and no change happened?
* Click again on the red "Delete" Icon. Is the modal correctly rendered?
* If yes, click on delete. Is the "users_list" template correctly rendered?
* If yes, is the confirmation alert present?
* Did the user disappear from the list?
* Did the user count display the right number?
* Navigate to the all cocktails page. Are the cocktails submitted by the deleted user deleted as well?

**Like a cocktail (View for all/ Action only for registered user and Admin**

* As a guest user, navigate to the "All cocktails" page through the navigation bar and select a cocktail of your choice. Is the cocktail template rendered correctly ?
* Scroll down, is the grey outline "like" button with like count rendered correctly?
* Try to click on it, are you correctly redirected to the login page ?
* Is the form displayed correctly?
* As a registered user or Admin,  navigate to the "All cocktails" page through the navigation bar and select a cocktail of your choice. Is the cocktail template rendered correctly ?
* Scroll down, is the grey outline "like" button with like count rendered correctly?
* Click on it. Is the cocktail template refreshed correctly?
* Is the confirmation alert present ?
* Is the like count updated with your vote ?
* Did the button changed color ?
* Is the click function disabled?

<a name="dtest"></a>

### Defensive Design Testing ###

**Register and Log In**
![Username Error](static/img/readme/username_error.png)
![Email Error](static/img/readme/email_error.png)
![Username exist](static/img/readme/username_exist.png)
![Incorrect ](static/img/readme/incorrect_password.png)

* If any field is left empty after the button is clicked, the form will request a valid entry.
* It is impossible to register or log in without filling all the fields.
* If the username already exists, the message "username already exists" will appear to prevent duplication.
* All usernames and passwords must be minimum 5 characters or the form will require the user a valid entry.
* In Log In specifically, if the user submit with the wrong password or username, the message "Incorrect password/username" will appear on the page.

**Newsletter**

* If the user (registered or not) attempt to fill the Newsletter email field with a invalid address, the form will display an error tooltip.
![Newsletter Error](static/img/readme/newsletter_error.png)

**Category**

* Only the admin can access the category pages :
    - categories.html
    - add_category.html
    - edit_category.html
* When a guest user and/or a registered user try to access the pages edit_category and add_category by typing the url, they are redirected to the "Login" page.
* When a guest user and/or a registered user try to access the pages categories by typing the url, they are redirected to the index page.
![Error](static/img/readme/error.png)

**Add and Edit cocktail**

* Only registered users can add, edit and delete cocktails. 
* When a non registered-user tries to enter the url manually, they will be redirected towards the login page.

**Manage user list**

* Only the admin can view the userlist and have access to the delete user functionnality.
* When a user that is not the admin try to access the url manually they are directed to the index page.

**Like Button**

* Only a registered user can like a cocktail.
* If a non-registered user tries to like a cocktail, they will be redirected to the login page.
* For registered user: the like button is disabled after the it is clicked once to avoid like multiplication from the same user.

<a name="issues"></a>

## Issues ##
---

**During development**

**Errors in console**

* Since I am only using on Javascript file, the console was showing a few error message when the user is not on index.html because the hero animation isn't used on any other page.
* I fixed my problem by using and if window.location statement for the animation functions.

**Accessibility**

* The theme of the website is pretty monochromatic (except for the delete/edit button). I liked the white text on bright yellow background. Unfortunately it didn't pass the accessibility test.
* I then changed the white text color for a dark yellow-brown to meet the standards.

**Search box**

* Initially my search function was only allowing text search and wasn't returning categories as a result.
* I upgraded the search text box with a category option menu and fixed my search function to allow separate and combined search.

**Footer**

* My footer refused to stick to the bottom. I tried to fix it with the fixed-footer Bootstrap class. It sticked to the bottom but then covered any content at the bottom of the page.
* I then fixed the height of the body and html tags in CSS. I removed the Bootstrap class and attempted a fixed position with a bottom of 0 with no luck. It was still covering my content.
* As a quick fix I removed the bottom of 0 and gave the wrapping section of each page a minimum width of 100vh.

**Modal button**

* My delete cocktail/category function is linked to a confirmation modal. At first that modal was displaying as many buttons as there was category/cocktail cards when clicked.
* I fixed it by including the modal in the for loop and it now generates just two buttons as it is supposed to.

**Pagination**

* My first pagination function was not displaying the last page if it wasn't full.
* I fixed it by changing the interger value to a float to get the decimal.

**SSL**

* Santé started acting out (maybe because it's hosted on Heroku) and was requesting and HTTP rather than an HTTPS.
* I installed **flask_sslify** to force HTTPS on the app and never encountered that problem again.

**User Authentification**

* As I was manually testing the profile pages of Santé! it occured to me that as long as a user was logged in they could access any profile if the route was entered manually in the url.
* Much head scratching I did. I fixed it by creating a utility function that checks if the logged user matches with the username and redirects to the login page if it doesn't match.

# Deployment<hr>

***Requirements to deploy:***

- An IDE: I used Gitpod but will use a IDE that is not online for my next project. I choose Gitpod as this is the recommended IDE at Code Institute.
- Python3: In order to to run the application and use Flask.
- PIP3: To install all application imports (such as Flask and OS).
- A template folder: To link with the app routes.
- A database: I choose MongoDB Atlas. 


## Local Deployment<hr>

* Open browser of choice.
* Copy/Paste the address of [**Santé! repository**](https://github.com/AudreyLL88/MS3__Sante) in your search box.
* When on the page, click on the "Code" button.
* Copy the the |**HTTPS link**](https://github.com/AudreyLL88/MS3__Sante.git).
* Open your IDE and in your terminal, create a virtual environement supporting python and flask and activate it.
* Type "git clone" and paste the [**HTTPS Link**](https://github.com/AudreyLL88/MS3__Sante.git).
* Create an environement file called "env.py" and add :
    - MONGO_URI=mongodb+srv://...
    - SECRET_KEY= [Your Secret key]
* Add your env.py to .gitignore. to avoid it being uploaded.
* In app.py, switch **debug=False** to **debug=True**
* Upgrade pip locally with the command "pip install -U pip".
* Install the modules used to run the application using "pip freeze > requirements.txt" in your terminal.
* In parallel, create a MongoDB account and create a database called **"sante_project"**.
* These are the following collections in the database:

***categories***
```
_id:<ObjectId>
category_name:<string>
```
***subscriptions***
```
_id:<ObjectId>
sub_email:<string>
```

***users***
```
_id:<ObjectId>
username:<string>
password:<string>
user_img:<string>
user_level:<string>
user_loc:<string>
liked_cocktail:<Array>

```

***cocktails***
```
_id:<ObjectId>
category_name:<string>
cocktail_name:<string>
cocktail_description:<string>
cocktail_img:<string>
cocktail_ingredients:<string>
cocktail_instructions:<string>
cocktail_prep: <decimal128>
cocktail_diff:<string>
cocktail_serv:<decimal128>
cocktail_img_cred:<string>
created_by:<string>
cocktail_like:<decimal128>
cocktail_date:<string>
```

![Entity](static/img/readme/diagram.png)

* You can now run your application locally by typing the command "python3 app.py" or "run app.py" in your terminal.
* You can visit the website at http://127.0.0.1:5000

## Deploying on Heroku<hr>

- Create a requirements.txt file using the command **pip3 freeze --local > requirements.txt** in your CLI.
- Create a Procfile (always with an uppercase P) through the command **echo web: python app.py > Procfile**. Commit and Push.
- Create an account on [**Heroku**](https://www.heroku.com/home).
- Create a new app with **unique name**.
- Select your **nearest region**.
- Create a **new python project** within the project.
- Link that project through your **Github repository** in the **deployment** section.
- Navigate to Haroku Settings and set up the following in **Config Vars**

```
_IP = 0.0.0.0
MONGO_DBNAME = [Name of DB]
MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
PORT = 5000
SECRET_KEY = [Your Secret key]

```
* Go back to the Deploy section, select the master branch and deploy the project. 


<a name="credits"></a>
## Credits ##
---

**Text Credits:**

* All cocktail recipes are taken from the following websites:
    - [**The Spruce Eats**](https://www.thespruceeats.com/)
    - [**Goop**](https://goop.com/)
    - [**Liquor**](https://www.liquor.com/)
    - [**Ties**](https://www.ties.com/)

**Image Credits:**

* * All cocktail recipe images are taken from the following websites:
    - [**The Spruce Eats**](https://www.thespruceeats.com/)
    - [**Goop**](https://goop.com/)
    - [**Liquor**](https://www.liquor.com/)
    - [**Ties**](https://www.ties.com/)
    - [**Pexel**](https://www.pexels.com/)

* All images used in the **It's Apero Time** index.html section are from [**Pixabay**](https://pixabay.com/)
* The elements used on the hero section of index.html are all made by **Ivar Dahlberg**.
* The image used for the profile picture of Audrey88 is my portrait.
* The image used for the profile picture of LeBarman, Admin and user default image are from [**Pexel**](https://www.pexels.com/)
* The image user for the error page is from **MemeGenerator**.

**Many thanks to:**

* My mentor **Ignatius Ukwuoma** for his advice.
* **Kasia** for her very inspiring ReadME.
* **Sean** who will dislike being mentionned but his time was precious.
* **Anthony and Jim** for their advice on use of doctstring and comments.
* **Code Institute Slack community** for the technical and emotional support.
* **Ivar Dahlberg**, for all the beautiful designs he created and his assistance.

**Site for educational purposes only!** (for now)