
# PostgreSQL Integration with Django Application
Django is a flexible framework for quickly creating Python applications. By default, Django applications are configured to store data into a lightweight SQLite database file. While this works well under some loads, a more traditional DBMS can improve performance in production.

That's why we are use using PostgreSQL here in our project.

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



