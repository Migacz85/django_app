#!/usr/bin/env bash
############################################
# Run Django or install new project script.#
############################################
# If you have already installed django and
# you want to run project just run this script
# from shell typing:
# source run.sh
# you need to install before 

# In order to run this script you need to have dependecies like:
# git, heroku, sed

echo "1. Start new project?"
echo "This will: "	
echo "-Install Django,"
echo "-Make admin"
echo "-Setup default settings.py file"
echo "-Initialize git, (Can be skipped)"
echo "-Make first commit (Can be skipped)"
echo "2. Create remote repository on heroku?"
echo "This will: "
echo "-Push project on heroku and setup env variables there"
echo "3. Run server and develop locally"
echo "===================="
echo "Note! If you want run 3 you need to source this script"
echo "Type 1 or 2 or 3?"

decision='n'
read decision

if [ $decision == 3 ]; then
	port=5003
	username="Migacz85"

	export DEVELOPMENT=1
	export HOSTNAME='localhost'
  export SECRET_KEY=$(<secret.key)

  # Create new secret key if is not present
	if [ ! -f secret.key ]; then
		rand="$( strings /dev/urandom | tr -d '\n' | head -c50 )" 
    echo	"$rand" > secret.key
	fi

  # Test exteran databases here	
  # export DATABASE_URL='postgres://xizoquvzyhrnks:714f3fd7bf7b889c25812494c20268cbe390b5e08706ca774b8fbdd96bdea926@ec2-46-137-121-216.eu-west-1.compute.amazonaws.com:5432/dbuhbf894gokvm'
  unset DATABASE_URL

  echo "Your temporary environmental variables are as follow:"
  echo "DEVELOPMENT - " $DEVELOPMENT
  echo "HOSTNAME -"	$HOSTNAME	
	echo "SECRET_KEY -" $SECRET_KEY
  echo "DATABASE_URL -" $DATABASE_URL 	
  echo " "	
	echo "Following aliasses are avaliable:" 
	echo "r - run the server again"
	echo "m - make migrations"
	echo "s - create super user"
	alias r="python manage.py runserver localhost:$port"
	alias m="python manage.py migrate"
	alias v="source venv/bin/activate"	
	alias s="python manage.py createsuperuser"	
	echo ""
	echo "virtual environment init"
	python -m venv venv 
	source venv/bin/activate
	echo "Type 'deactivate' to quit virutal env"
  python manage.py runserver localhost:$port
fi

if [ $decision == 1 ]; then

	if [ ! -f secret.key ]; then
		rand="$( strings /dev/urandom | tr -d '\n' | head -c50 )" 
    echo	"$rand" > secret.key
	fi
 
	export DEVELOPMENT=1
  export SECRET_KEY=$(<secret.key)
	export HOSTNAME='localhost'
	unset DATABASE_URL
  # export DATABASE_URL='postgres://ltfitfkpxjxcsg:656b7a6bdf2de4b5fea0860236200585c225c4e3ed8a7143e1870da8405d933e@ec2-54-247-82-210.eu-west-1.compute.amazonaws.com:5432/dcp131rtk26hf9'

 	echo "Give your project name"
	echo ""
  echo "Note: Name must start with a letter, end with a letter" 
	echo "or digit and can only contain lowercase letters, digits, and dashes."
	read project_name
  echo "Install dependencies with django" 

  python -m venv venv 
  source venv/bin/activate

	pip3 install --upgrade pip
	pip3 install django
	# Specify version of djnago  
	# pip3 install django==1.11.17
  pip3 install gunicorn 											 	# for running app on the server
  pip3 install psycopg2-binary 									# postgre sql
  pip3 install dj_database_url 	
  pip3 install whitenoise
  echo "Save requirements" 
  pip3 freeze --local > requirements.txt
  echo "Start new project"
	django-admin startproject $project_name .

  echo "Create standart settings.py for django"
  wget https://gist.githubusercontent.com/Migacz85/d4439b5de616bc4d329917370be85c3f/raw/558998897e3bcd8f1fa2fb9f3a29825a6f2181e4/gistfile1.txt -O $project_name/settings.py

  sed -e "s/unicorn/$project_name/g" "$project_name/settings.py" > tmpfile
  mv	tmpfile "$project_name/settings.py"
  rm tmpfile

	echo "Saving current python version - Heroku will respect this"
  python -V > runtime.txt

  source venv/bin/activate
	echo "Creating admin..."
	python3 manage.py createsuperuser
  echo "Move static files to one folder"
	python manage.py collectstatic
  echo "Make migrations" 
	python3 manage.py migrate

	# Create Procfiles for external server
  echo "Create Procfile"
  echo "web: gunicorn $project_name.wsgi:application " > Procfile 

  echo "Initialize git in this project  ? y/n "
	read decision
  if [ $decision == y ]; then 
  echo "Initialization of git and first commit"
	git init

  echo "secret.key" > .gitignore
  echo "secret2.key" >> .gitignore
  echo "venv/" >> .gitignore
  echo ".gitignore" >> .gitignore
  echo "db.sqlite3" >> .gitignore
  
	git add .
	git commit -m "Initial commit"
  fi  

  echo "Create new repository on github with name of this project? And push it there? y/n"
	read decision

  if [ $decision == y ]; then 

	echo "Your Github login?"
	read username 

	test -z $project_name && echo "Repo name required." 1>&2 && exit 1
	curl -u $username https://api.github.com/user/repos -d "{\"name\":\"$project_name\"}"

  echo "Pushing initial commit on github"
  git remote add origin https://github.com/$username/$project_name.git
  git push -u origin master
 	fi

fi

#### Heroku deployment

if [ $decision == 2 ]; then

  heroku login

	echo "Give your UNIQUE project name"
  echo "Name must start with a letter, end with a letter" 
	echo "or digit and can only contain lowercase letters, digits, and dashes."
  echo " " 
  read project_name

  heroku create $project_name --region eu 
  heroku addons:create heroku-postgresql:hobby-dev
	
	heroku config -a $project_name

  random="$( strings /dev/urandom | tr -d '\n' | head -c50 )" 
  $random > secret2.key 	
	
	echo "Set environment variables on remote server"
  heroku config:set HOSTNAME=$project_name.herokuapp.com
  heroku config:set DEVELOPMENT=1
  heroku config:set SECRET_KEY="{$random}"	


	echo "Install vim on heroku"
  heroku plugins:install heroku-vim

  echo "Connect heroku whit this git"
  heroku git:clone -a $project_name

  echo "Pushing this repository on heroku"
  git push heroku master
  
  echo "Making migrations:"
  heroku run python manage.py migrate
  echo "Creating new admin:"
  heroku run python manage.py createsuperuser

  heroku ps:scale web=1

	git remote -v 
  heroku open

  echo "Deployment on heroku is done! Here is heroku response: "
	echo "Ctrl + q to quit"
  heroku logs --tail	
	
fi


