# Project 5

One or two paragraphs providing an overview of your project.

Essentially, this part is your sales pitch.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->


- [UX](#ux)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Start developing this project](#start-developing-this-project)
    - [Tip: Quick entering to virtual environment and starting the server](#tip-quick-entering-to-virtual-environment-and-starting-the-server)
    - [Create new Django project](#create-new-django-project)
    - [Managing Database](#managing-database)
- [Deployment](#deployment)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)
- [Acknowledgements](#acknowledgements)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## UX
 
Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:
- As a user type, I want to perform an action, so that I can achieve a goal.

This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

## Features

In this section, you should go over the different parts of your project, and describe each in a sentence or so.
 
### Existing Features
- Feature 1 - allows users X to achieve Y, by having them fill out Z
- ...

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement
- Another feature idea

    
## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.


## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


## Start developing this project 

To start developing the  project locally you need to make following steps:

1. Clone project 
`git clone this_project_link`
2. Initialize new environment
`python -m venv venv`   
3. Enter to the new environment.

`source venv/bin/activate` 

4. Install project dependencies

`pip install -r /path/to/requirements.txt`  

5. Run the server on your localhost
`python3 manage.py runserver localhost:5000` 
6. [Optional] When you will be done, you can quite virtual environment

`deactivate` 

#### Tip: Quick entering to virtual environment and starting the server

If you are often use python this can be a good trick for quick creating and entering to the virtual environment and running the server: (just add this to your .bash_profile or .bashrc) 

```
alias env-init="python -m venv venv"
alias env-enter="source venv/bin/activate"
alias env-show="pip3 freeze --local"
alias env-install="sudo pip3 install -r" 
alias run="python3 manage.py runserver localhost:5000" 
```

Remember to update your shell with new settings (select .zshrc, .bashrc, or whatever file you are currently using to control your shell):

`source ~/.bashrc` 

#### Create new Django project

If you have a complete different idea of web app you can start your own new project by executing this steps: 

1. First enter to virtual environment (You can find this information above)
2. Install Django:
`sudo pip3 install django`
3. Start new project in (the command will generate project in root directory)

`django-admin startproject your_project_name .` 

4. You can now run the server and check if its running
	
 ` python3 manage.py runserver localhost:5000`

5. Create your own app: (Close piece of functionality in django)

`django-admnin startapp your_app_name`

views.py - file that handles request and response to the browser code is organised in classes
urls.py  - You should include your classes from views.py in order to assign them to different urls in urlpatterns list.

6. In settings.py, find this list variable and add name of your app folder:

`INSTALLED_APPS = ['your_app_name' ]`  

7. Don't forget to add your site  to 'ALLOWED_HOSTS' variable.

8. In `your_app_name` create your logic using functions in `views.py` and connect
them with `urls.py` to execute.

#### Testing

All test can be found in directory /master/app_name/
- test_form.py
- test_models.py
- test_views.py
files. 

Test names should start with "test_" string without the quotes. 

1. To run automated tests run in master directory:

`python manage.py test` 

##### Coverage 

1. To be able to write automated test and run them first install coverage:
`pip3 install coverage`
2. Test individual app in your Django project by using command:
`coverage run --source=your_app_name manage.py test`
3. For generating a coverage test in html simply type:
`coverage html` 

#### Managing Database

1. Enter to database
`sqlite3 db.sqlite3`
2. Check what tables you have in db.

`.tables`
3. Show everything in django_migrations

`select * from django_migrations`

4. Migrate 
`python3 manage.py migrate`

5. If you want to see column names with nice formatting
```
.headers on
.mode column
select * from django_migrations
```
6. Use django manage.py script to add admin user:
`python3 manage.py createsuperuser`
  - Type email address
  - Type Password

5. If you want to see column names with nice formatting
```
.headers on
.mode column
select * from django_migrations
```
6. Use django manage.py script to add admin user:
`python3 manage.py createsuperuser`
  - Type email address
  - Type Password
7. Check if user is actually created:

```
sqlite3 db.sqlite3
.tables
.headers on
.mode column
select * from auth_user; 
```

8. You can now enter to django admin panel on website

enter in url of your website /admin

9. Create sqlite.rc file in home directory

```
.headers on
.mode column
```

## Deployment

Before deployment on external server in settings.py this variable need to be updated with link to your website: 

`ALLOWED_HOSTS = ['your_website']`
 
This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Heroku Install vim on heroku:

```bash	
mkdir ~/vim
cd ~/vim

# Staically linked vim version compiled from https://github.com/ericpruitt/static-vim
# Compiled on Jul 20 2017
curl 'https://s3.amazonaws.com/bengoa/vim-static.tar.gz' | tar -xz

export VIMRUNTIME="$HOME/vim/runtime"
export PATH="$HOME/vim:$PATH"
cd -
```

## Credits

## Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

## Media
- The photos used in this site were obtained from ...

## Acknowledgements

- I received inspiration for this project from X
/home/migacz/gifs/markdown-vim-error.gif
