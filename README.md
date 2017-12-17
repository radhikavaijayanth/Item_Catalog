# Item_Catalog
  # RestaurantMenu App
  1. This app is created using Python module which inturn generates a website and a JSON API for a list of restaurants. 
  2. Each restaurant displays their menus.
  3. Oauth 2.0 is provided using google authentication.
  4. Users should register to create their own restaurants and edit and delete the menus only for the restaurants 
     that they have created.
  5. The tech stack used in creating this app includes Flask,SQL Alchemy, JQuery,CSS, Javascript, and OAuth2.
# Softwares to be installed for this project
    1. Virtual Box
    2. Vagrant
    3. Pythob 2.7
    4. Flask and SQL Alchemy 

# Steps to Run The Project 

  # Setting up OAuth 2.0
    1. You will need to signup for a google account and set up a client id and secret.
    2. Visit http://console.developers.google.com for google setup.

  # Setting up the Environment
    1. clone or download the repo into vagrant environment.
    2. Type command vagrant up,vagrant ssh.
    3. In VM, cd /vagrant/catalog
    4. Run python database_setup.py to create the database.
    5. Run Python lotsofmenus.py to add the menu items
    6. Run python 'project.py'
    7. open your webbrowser and visit http://localhost:8000/

# Sources referred
  The code for the demo project in this lesson was referred to complete this project
  


