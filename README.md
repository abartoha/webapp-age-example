# Webapp, Age, Example
This is a very bad way to start a web app, or at least to present it to the people, asking for their age and such. But here we are! it's deployed in [**this Heroku link**](http://hobby-age-4lr4zi.herokuapp.com);
# Overview
This web app has used a couple of frameworks and methods to run.
## Core
* Python
## Web Framework
* flask
## Database
* Flask_SQLAlchemy
* psycopg2
* postgreSQL
## Build and Deploy
* gunicorn
# How to test locally
It's fun to do a local test of the webapp. But provided you don't have any requisite and there's no error or internet lag, it'll take **an hour** for even the simplest way to make it all come together.

1. Install python **BUT** check [heroku](https://devcenter.heroku.com/articles/python-support#supported-runtimes) for the runtimes that heroku allows to run.
	>**TIP**: If you can't install the version on Windows, just try to find the closest possible thing you can. *For example*:- I had trouble with Heroku running only 3.6.14, 3.7.11, 3.8.11 and 3.9.6, there was no windows installer for any other version except 3.9.6 and It had *NO WINDOWS 7 SUPPORT*, but there was binary for 3.8.10 so I went with that. Always try your best to match the best version of python.

	and also start downloading [postgreSQL](https://www.postgresql.org/download/), we'll visit that at *step 3*.

2. Install virtual envirnment in python,
	```
	pip install virtualenv
	```
	and then go make a virtualenv in the project directory,
	```
	# might not work for some of you, check the internet for that
	python -m virtualenv <env_name>
	```
	after that install all the requirements from requirements.txt,
	```
	pip install -r requirements.txt
	```
	and yes in some cases, especially in **Linux** or **macOS** you might have to use `python3` and `pip3` instead of `python` and `pip`
3. install postgreSQL, providing it has already been downloaded.
	and **please**, do check the box for pgAdmin4 or whatever version currently might be there. The tutorial I checked had pgAdmin3
4. Open a new database in a new server, take note of every password and username you meet on the way, and add postgreSQL to the PATH, in Windows it's something like `C:/Program Files/PostgreSQL/<versionNumber>/bin` and then open pgAdmin. Here's where the database creation will happen. Then you can modify the DATABASE_URI in the code according to the commented section, don't replace that line! might come in handy when you mess up. **LOL**
5. Open a terminal in the directory and run python interpreter to run these lines one after another,
	1. `from app import db`
	2. `db.create_all()`
	3. after running these and closing the interpreter, you can run `python app.py` or something, the console will turn into a baby hacker console (*debugging console, lol*) and that's where the fun begins! find some link that looks like http://127.0.0.1:5000 and go to it. See if the thing is working or not. Most liekly it won't because you're a software developer now! Nothing will work! Never!
6. Don't close pgAdmin until you're done. Have fun, get to sleep, it's **0510** hours.

# ADIOS AMIGOS!