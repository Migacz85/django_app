#!/usr/bin/env bash
#  █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗
# ██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║
# ███████║██║  ██║██╔████╔██║██║██╔██╗ ██║
# ██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║
# ██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║
# ╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝
# ████████╗ ██████╗  ██████╗ ██╗     ███████╗
# ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
#    ██║   ██║   ██║██║   ██║██║     ███████╗
#    ██║   ██║   ██║██║   ██║██║     ╚════██║
#    ██║   ╚██████╔╝╚██████╔╝███████╗███████║
#    ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
############################################ 
# In order to run first option in this script you need to have dependecies like:
# git, heroku, sed
echo "Warning: Please run this only in root folder of your project"
echo "|========================================"
echo "|1. Start new project?"                 
echo "|This will: "	
echo "|- Install Django,"
echo "|- Make admin"
echo "|- Setup default settings.py file"
echo "|- Initialize git, (Can be skipped)"
echo "|- Make first commit (Can be skipped)"
echo "|========================================"
echo "|2. Create remote repository on heroku?"
echo "|This will: "
echo "|- Push project on heroku and setup env 
| variables there"
echo "|========================================"
echo "|3. Run server and develop locally"
echo "|- New SECRET-KEY will be setup to new 
| secret key that can be accessed in 
| secret2.key  file"
echo "|- Vim plugin for accessing will be turn on"
echo "|- Synchronize your github repository with 
| the heroku app"
echo "|- At the end your deployed link will be 
| automatically open in your browser."
echo "|Note! If you want run 3 you need to 
| source this script"
echo "|========================================"
echo "|4. Set all(with secrets) env variables on heroku"
echo "|========================================"
echo "|========================================"
echo "|5. Update coverage"
echo "|========================================"
echo "|This will: "
echo "|- run tests"
echo "|- update coverage html"
echo "|- update python dependency requirements "  
echo "|- make commit and push changes on remote server"  
echo "|Choose 1 or 2 or 3 or 4 or 5?"

decision='n'
read decision

# LOCALHOST
if [ $decision == 3 ]; then
    clear
    port=5000 # Port number on localhost
    username="Migacz85" # Github login
    secrets=0 # Show value of environmental variables (with secrets)?

    # unset DEVELOPMENT
    export DEVELOPMENT=0
    
    export HOSTNAME='localhost' 
    export PORT=$port
    # If you will want to connect locally to external db:
    # unset DATABASE_URL
    # export DATABASE_URL='postgres://qkstunpbcqehkk:01159572c3775a94c96eaa7e4665b94375046d2c53491b602d4ae6a2e7834994@ec2-79-125-2-142.eu-west-1.compute.amazonaws.com:5432/dd37t2r0frb70k'

    # Create new secret key if is not present
	if [ ! -f secret.key ]; then
            rand="$( strings /dev/urandom | tr -d '\n' |  tr -d ' '  | head -c50 )" 
            echo "$rand" > secret.key
        fi
    source secret.sh # Keeping secret env variables here
    alias r="python manage.py runserver localhost:$port"
    alias m="python manage.py makemigrations && python manage.py migrate"
    alias v="source venv/bin/activate"	
    alias sa="python manage.py startapp"	
    alias s="python manage.py createsuperuser"	
    alias s3sync="aws s3 sync --acl public-read --sse --delete staticfiles s3://$AWS_STORAGE_BUCKET_NAME/$STATICFILES_LOCATION"
    alias pfl="pip3 freeze --local > requirements.txt"

    echo "" 
    if [[ secrets -eq 1 ]]; then
      echo "Your environmental variables are as follow:"
      echo "--------------------------------------------------"
      echo "AWS_STORAGE_BUCKET_NAME"  $AWS_STORAGE_BUCKET_NAME
      echo "AWS_S3_REGION_NAME"       $AWS_S3_REGION_NAME
      echo "AWS_ACCESS_KEY_ID"        $AWS_ACCESS_KEY_ID
      echo "AWS_SECRET_ACCESS_KEY"    $AWS_SECRET_ACCESS_KEY
      echo "EMAIL_USER"               $EMAIL_USER
      echo "EMAIL_PASSWORD"           $EMAIL_PASSWORD
      echo "SECRET_KEY"               $SECRET_KEY
      echo "STRIPE_PUBLISHABLE"       $STRIPE_PUBLISHABLE
      echo "STRIPE_SECRET"            $STRIPE_SECRET
      echo "--------------------------------------------------"
    fi
    echo " " 
    echo "Following aliasses are avaliable:" 
    echo "--------------------------------------------------"
    echo "r - run the server again"
    echo "m - make migrations"
    echo "sa - django-admin startapp"
    echo "s - create super user"
    echo "v - enter virtual env"
    echo "s3sync - sync static files with your aws s3 server"
    echo "Type 'deactivate' to quit virutal env"
    echo "--------------------------------------------------"
    echo ""
    echo "Virtual environment init... "
    python -m venv venv 
    source venv/bin/activate
    echo "Starting Django server... " 
    echo "--------------------------------------------------"
    echo "" 
    
    python manage.py runserver localhost:$port
fi

# STARTNEWPROJECT
if [ $decison == 1 ]; then
	if [ ! -f secret.key ]; then
		rand="$( strings /dev/urandom | tr -d '\n' | head -c50 )" 
          echo	"$rand" > secret.key
	fi
    export DEVELOPMENT=1
    export SECRET_KEY=$(<secret.key)
    export HOSTNAME='localhost'
    echo "Give your project name"
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
    pip3 install psycopg2-binary 	    						   		# postgre sql
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
    # python -V > runtime.txt
    source venv/bin/activate
    echo "Move static files to one folder"
    python manage.py collectstatic
    echo "Make migrations" 
    python3 manage.py migrate
    echo "Creating admin..."
	python3 manage.py createsuperuser
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
    echo "*.pyc" >> .gitignore
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

# HEROKU DEPLOYMENT
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
    echo "Setting environment variables on remote server"
    # Don't make spaces betwen = and variables, because it won't work
    # It's heroku default format for setting env variables.
    heroku config:set HOSTNAME=$project_name.herokuapp.com
    heroku config:set DEVELOPMENT=1
    heroku config:set SECRET_KEY="{$random}"	
    echo "Setting secrets on heroku:"
    source secret.sh 
    heroku config:set AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
    heroku config:set AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
    heroku config:set SECRET_KEY=$SECRET_KEY 	
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
    echo "If you created app on heroku that you dont want just type:" 
    echo "heroku apps:destroy"
    echo ""
    echo "Deployment on heroku is done! Here is heroku response: "
    echo "Ctrl + c to quit"
    heroku logs --tail	
fi

# SETTING ENV VARIABLES ON HEROKU
if [ $decision == 4 ]; then 
    echo "Starting setting secrets on heroku..."
    source secret.sh 
    # Create new secret key if is not present
	if [ ! -f secret2.key ]; then
		rand="$( strings /dev/urandom | tr -d '\n' |  tr -d ' '  | head -c50 )" 
    echo	"$rand" > secret2.key
	fi
    export SECRET_KEY2=$(<secret2.key)
    echo "Setting environment variables on remote server"
    heroku config:set SECRET_KEY="$SECRET_KEY2"
    heroku config:set AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
    heroku config:set AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
    heroku config:set EMAIL_USER=$EMAIL_USER
    heroku config:set EMAIL_PASSWORD=$EMAIL_PASSWORD
    heroku config:set STRIPE_SECRET=$STRIPE_SECRET
    heroku config:set STRIPE_PUBLISHABLE=$STRIPE_PUBLISHABLE
    heroku config:set AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME  
    echo "done" 
fi

# UPDATE COVERAGE 
if [ $decision == 5 ]; then 

      pip3 freeze --local > requirements.txt 
      coverage run --omit='*migrations*' --source=Home,cart,bugs,charts,checkout manage.py test
      coverage report

      echo "Build html coverage and push it on github? y/n"
      read decision
      if [ $decision == y ]; then 
      coverage html 
      git add . 
      git commit -m "Update: html Coverage"
      git push 
      fi 
fi
