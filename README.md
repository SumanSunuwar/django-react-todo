### todo app
todo application for creating task.

backend is built with python-django serving api, and

frontend is built using react js library which consumes backend api

clone in the git repo to get both backend and fronted source code

#backend
install requirements.txt in the virtual environment

run makemigrations and migrate commands / [default database is sqlite / can switch to postesql db]

django postgresql setting configuration for switching from sqlite to postgresql


DATABASES = {

    'default': {
    
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        
        'NAME': config('DB_NAME'),
        
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        
        'HOST': config('DB_HOST'),
        
        'PORT': '',
        
    }
}


then run the django server to start api backend.

"by default django server will start in the port 8000"

#frontend 

install the app dependencies

commands:

cd frontend

npm install

npm start

"by default react app will start in the port 3000" if already in use it might start 3001

'''check the proxy variable in the package.json file settle to  => "proxy": "http://127.0.0.1:8000/",'''


cors allowing are set in the settings of drf-api

if the react server starts in other host than following api request might not be successfull

django project setting file.

CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",
    
    "http://127.0.0.1:3000",
    
    "http://localhost:3001",
    
    "http://127.0.0.1:3001",
    
]

#backend installation summery:

Set python environment 

clone the code in machine

Install all the dependencies in machine from requirements.txt file from the backend for drf-api dependencies

create .env file and copy the code from .env.example file

Make all the environment set and run the api

#frontend installation summery:

install npm dependecies

run the app
