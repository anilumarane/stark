Movie Project

Login Credentials
Role
1.http://127.0.0.1:8000/account/

Signup
1. http://127.0.0.1:8000/account/signup

Signin
2. http://127.0.0.1:8000/account/user_login

Inbuilt api for token generate
1. http://127.0.0.1:8000/account/api/token/




Admin Can
1. add poster
http://127.0.0.1:8000/movie/poster_create
2. update poster
http://127.0.0.1:8000/movie/poster_update/1
3. delete poster
http://127.0.0.1:8000/movie/poster_delete/2
4. add movie
http://127.0.0.1:8000/movie/movie_create
5. update movie
http://127.0.0.1:8000/movie/movie_update/1
6. delete movie
http://127.0.0.1:8000/movie/movie_delete/2



B. User Can
1. search relete movie
http://127.0.0.1:8000/movie/get_movie_list
2. see the movie list
http://127.0.0.1:8000/movie/get_movies?search=Asd

Installation
1. Create a Folder where you want to save the project

2. Create a Virtual Environment and Activate

Install Virtual Environment First

$  pip install virtualenv
Create Virtual Environment

For Windows

$  python -m venv venv
For Mac

$  python3 -m venv venv
Activate Virtual Environment

For Windows

$  source venv/scripts/activate
For Mac

$  source venv/bin/activate
3. Clone this project

$  https://github.com/anilumarane/stark.git
Then, Enter the project

$  cd django-student-management-system
4. Install Requirements from 'requirements.txt'

$  pip install -r requirements.txt
5. Add the hosts

Got to settings.py file
Then, On allowed hosts, Add [‘*’].
ALLOWED_HOSTS = ['*']
No need to change on Mac.

6. Now Run Server

Command for PC:

$ python manage.py runserver
Command for Mac:

$ python3 manage.py runserver



7. import the sql file in stark.sql in folder

8. import the postman collection check the all relate apis
