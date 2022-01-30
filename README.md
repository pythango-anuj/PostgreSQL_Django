# PostgreSQL Integration with Django Application
Django is a flexible framework for quickly creating Python applications. By default, Django applications are configured to store data into a lightweight SQLite database file. While this works well under some loads, a more traditional DBMS can improve performance in production.

That's why we are use using PostgreSQL here in our project.

So our First task is to Integrate PostgreSQL with a Django Application.

Note: All commands are being run on ubuntu terminal.
# STEP1: Install the Components from the Ubuntu Repositories

The following apt commands will get you the packages you need:

sudo apt-get update

sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

# STEP2: CREATING THE PostgreSQL DATABASE

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. We need to change to this user to perform administrative tasks:

sudo su - postgres

You should now be in a shell session for the postgres user. Log into a Postgres session by typing:

psql

Now run the following commands to create the whole setup for our database(myproject) with username(myprojectusername)
 and password(password):

CREATE DATABASE myproject;

CREATE USER myprojectuser WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';

ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';

ALTER ROLE myprojectuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

Exit the SQL prompt to get back to the postgres user’s shell session:

/q

Exit out of the postgres user’s shell session to get back to your regular user’s shell session:

exit

# STEP3: Install Django within a Virtual Environment

sudo pip install virtualenv

mkdir ~/myproject

cd ~/myproject

virtualenv myprojectenv

source myprojectenv/bin/activate

pip install django psycopg2

django-admin.py startproject myproject 

# STEP4: Configure the Django Database Settings

Open the main Django project settings file located within the child project directory:

nano ~/myproject/myproject/settings.py

Towards the bottom of the file, you will see a DATABASES section that looks like this:

. . .


DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

. . .

 We’ll add and leave blank the port option so that the default is selected:

. . .

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

. . .

When you are finished, save and close the file.

# STEP5: Migrate the Database and Test your Project

cd ~/myproject

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

http://server_domain_or_IP:8000

By accessing the admin interface, we have confirmed that our database has stored our user account information and that it can be appropriately accessed.

# Conclusion

In this guide, we’ve demonstrated how to install and configure PostgreSQL as the backend database for a Django project. While SQLite can easily handle the load during development and light production use, most projects benefit from implementing a more full-featured DBMS.


# PROJECT INSIDE REPOSITORY

# DRF Authentication System (Using dj_rest_auth)
Django REST framework is a powerful and flexible toolkit for building Web APIs. In this project we are 
mainly focussing Authentication APIS.

There are many ways to develop Authenticating apis in DRF but in this project we have designed our own custom user model
and used dj_rest_auth(https://dj-rest-auth.readthedocs.io/en/latest/) for creating our API endpoints.
It provides us almost all authenticating properties requires for any Authentication system like:

Register(Add a new User)

Login

Logout

Password change

Password Reset

and many more include CRUD operations of a user.


Apart from that one another tool that we have used in this project is [drf_yasg(Swagger Generator)](https://drf-yasg.readthedocs.io/en/stable/readme.html) 
for API Documentation which makes our API look awesome.

# PREQUISITES

Following programmes should be installed on your computer to run this project properly:

Python 3.6+

Virtual Environment

To install virtual environment on your system use:

pip install virtualenv

# Installation and Running :

git clone https://github.com/pythango/PostgreSQL_Django.git

virtualenv myenv

source myenv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Open Browser and Type http://127.0.0.1:8000