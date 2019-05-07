[![Build Status](https://travis-ci.org/Migacz85/django_app.svg?branch=master)](https://travis-ci.org/Migacz85/django_app)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Unicorn Attractor](#unicorn-attractor)
  - [Implemented features](#implemented-features)
    - [For users](#for-users)
    - [For Admins of the site](#for-admins-of-the-site)
    - [For Developers](#for-developers)
  - [Not implemented features](#not-implemented-features)
  - [Technologies used](#technologies-used)
  - [UX](#ux)
  - [Testing & Bugs](#testing--bugs)
  - [Developing this project](#developing-this-project)
  - [Deployment on external servers (like heroku)](#deployment-on-external-servers-like-heroku)
  - [Quick new Django project](#quick-new-django-project)
  - [Interesting errors I noticed during development](#interesting-errors-i-noticed-during-development)
  - [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Unicorn Attractor

Project was build as an exercise for getting more familiar with Django framework.
The idea of this project was to build an issue tracker with ticket system.
Where people can easy vote for issues. Idea of voting is to simply show which 
of bugs should be fixed first. Also features should be  connected with payment
 system.  The [main goal of this project ](http://github.com/Migacz85/django_app/wiki/Goal-of-this-project)
as well with [guidelines](http://github.com/Migacz85/django_app/wiki/Guidelines) 
and [checklist](http://github.com/Migacz85/django_app/wiki/Checklist) that was 
required from Code institute to build this project can be found in the links of
wiki of this project. And all detailed information are there. This file is just a simplified version
of whole documentation that is showing a bigger picture in smaller form.

If you want to see how admin panel is implemented here is account to test it:

login: test_account
password: 1Testthis


## Implemented features 

### For users

1. Upvoting button allows regular user to add/remove vote to bug or feature by simply clicking on it.
	- To upvote a feature request, users need to pay
2. Create ticket button allows regular user to add bug or feature by clicking on it.
4. Comments on tickets, 
5. Each ticket is showing the status of the ticket so the user knows in what state it is.
	1. to do,
	2. doing, 
	3. done.
6. Cart with checkout and payment allows user to add vote features to the cart so he can after pay for them.
7. Authentication of the users allows regular user to set up account and gain access to creating issues and creating comments.
8. Resetting passwords allows regular user in case when he forget his password so he will be emailed with link for the page to reset the password.
9. If the number of comments or issues grow above 5 pagination for comments and issues will be turned on so users can navigate in content more easily.
10. When creating an issue user can add image so other users will understand better what he want to explain.

### For Admins of the site

1. Admin can set up state of the ticket by logging in to admin panel so he can indicate to the user in what state current issue is. 
2. Admin have separately `Bugs` and `Feature` section so he can easily navigate to the Features that are paid from the users.
3. Admin can change everything what is on webpage by admin page. 

### For Developers

1. Project is configured to store Images on external aws s3 server so service can grow to big sizes and this will be cost effective to store huge amount of data.
2. Project logic is configured to be executed on heroku servers so it will be not disrupted to store data from the users.
3. Project have integrated `deploy.sh` scripts so it will help developers with:
    1. Creating new Django project
    2. Creating new remote repository on heroku and setup there all necessary environmental variables and settings.
    3. Creating local environment, and setup useful productivity aliases when developing in Django to speed up process of:
        - `r` running the server
        - `m` making migrations 
        - `sa` starting new django application
        - `s` creating super user
        - `v` entering virtual environment
        - `s3sync` synchronising static files with s3 server
    4. Setting environmental variables on heroku
    5. Updating coverage and pushing 

## Not implemented features

1. User Profile
2. Charts that are showing summary for each month

## Technologies used

This project is build mostly on Python with Django framework using bootstrap to style it. 
List of all technologies can be found in [technologies](http://github.com/Migacz85/django_app/wiki/Technologies)
section that is on wiki. 

## UX 

Project was planned early on the beginning when I was creating wireframes with
documentation and strategy.  I clearly see that this extra time spent early in
project really helped after, when project was implemented. The organisation of the
features to be implemented and wireframes can be found on wiki page in [UX section](http://github.com/Migacz85/django_app/wiki/UX)

## Testing & Bugs

Users stories and functional specification were converted to manual and automated 
tests and can be found in [testing](http://github.com/Migacz85/django_app/wiki/Testing)
section of wiki page.

## Developing this project 

If you want to improve this project or build something else on it, 

1. Simply clone this repo first in your virtual environment,
2. [Set your secrets.sh](#https://github.com/Migacz85/django_app/wiki/Setup-your-secrets) and install requirements,
4. Run `source deploy.sh` script that is in repository and choose third option.

The really detailed steps can be found of course on wiki in section [developing this project](http://github.com/Migacz85/django_app/wiki/Start-developing-this-project) 

## Deployment on external servers (like heroku)

When you will have your project working locally with some changes 
you can upload your site to your external server(for example heroku).

You can do this using 2 methods, one manually clicking and setting up. Or
simply use provided script `deploy.sh` and select second option. I recommend to
use the script because is speeding the process greatly.  Detailed information
how to run, and what exactly will be done using provided script can be found in
section: [Deploy your project on heroku](http://github.com/Migacz85/django_app/wiki/Deploy-on-heroku) on wiki page.

Because setting aws3 was part of deployment process I spent extra time on checking how to configure it
using shell as well. Mostly because of feature possibility of automation process. During this time 
I wrote documentation and finding can be found in 
[Configuring AWS s3](http://github.com/Migacz85/django_app/wiki/Connecting-with-AWS-s3-cli)
section 

## Quick new Django project

Because I was thinking about my feature self coming back to Django I also implemented 
in script `deploy.sh` setting new Django project.
And there is lots of things that need to be setup before actual coding so I also 
created automated process of it that is speeding up the process greatly.   

To start new django project simply run `bash deploy.sh` and choose option one. 
Check what exactly need to be setup when starting new django project in section 
[Create new django project](http://github.com/Migacz85/django_app/wiki/Create-new-django-project)
on wiki page 


## Interesting errors I noticed during development

Because I was developing on linux and I had latest Python, I discovered
issues with version that was showed in the course. I tested lot of different
versions Django but only the latest one was working without any warnings.
Please check my additional [notes](http://github.com/Migacz85/django_app/wiki/Notes)
that i attached to this project.

## Credits
-  My mentor Moosa Hassan 
-  Thank you for helping with travis integration to: 
  @teraspora
-  Great thanks to @robinz_alumni from slack channel for a lot of voluntary help
- Thank you to my teachers and people from slack channel
-  @NielMc, @aaronsnig501, @lechien73, @nazarja, @10xOXR, @Sonnerz, @Wings30306 

