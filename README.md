<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Unicorn Attractor](#unicorn-attractor)
  - [Implemented features](#implemented-features)
  - [Technologies used](#technologies-used)
  - [UX](#ux)
  - [Writing automated tests:](#writing-automated-tests)
  - [Developing this project](#developing-this-project)
  - [Deployment on external servers (like heroku)](#deployment-on-external-servers-like-heroku)
  - [Quick new Django project](#quick-new-django-project)
  - [Interesting errors I noticed during development](#interesting-errors-i-noticed-during-development)
  - [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

[![Build Status](https://travis-ci.org/Migacz85/django_app.svg?branch=master)](https://travis-ci.org/Migacz85/django_app)
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
of whole documentation. 

## Implemented features 

1.  Upvoting bugs 
2.  Upvoting feature requests
	- To upvote a feature request, users need to pay 
3. Create tickets, 
4. Comments on tickets, 
5. Showing the status of the ticket  
	1. to do,
	2. doing, 
	3. done.
6. Cart
7. Authentication of the users
8. Pagination for comments and issues

## Technologies used

This project is build mostly on Python with Django framework using bootstrap to style it. 
List of all technologies can be found in [technologies](http://github.com/Migacz85/django_app/wiki/Technologies)
section that is on wiki. 

## UX 

Project was planned early on the beginning when I was creating wireframes with
documentation and strategy.  I clearly see that this extra time spent early in
project really helped after, when project was implemented. The organisation of the
features and wireframes can be found on wiki page in [UX section](http://github.com/Migacz85/django_app/wiki/UX)

## Writing automated tests:

Users stories and functional specification were converted to manual and automated 
tests and can be found in [testing](http://github.com/Migacz85/django_app/wiki/Testing)
section of wiki page.

## Developing this project 

If you want to improve this project or build something else on it, 

1. Simply clone this repo first in your virtual environment,
2. Set your environmental variables that are in `secrets.sh` and install requirements,
4. Run `source deploy.sh` script that is in repository and choose third option.

The really detailed steps can be found of course on wiki in section [developing this project](http://github.com/Migacz85/django_app/wiki/Start-developing-this-project) 

## Deployment on external servers (like heroku)

When you will have your project working locally and you will make some changes
to this existing project you can upload your site to your external server(for
example heroku).

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

Please check my: 
* [Notes](http://github.com/Migacz85/django_app/wiki/Notes)

## Credits

* [Credits](http://github.com/Migacz85/django_app/wiki/Credits)
