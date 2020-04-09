# Flask but Twitter

Flask but Twitter is an implementation of better Flask Structures of mine. This Flask Structures is combination between 2 structures that I adore because of the beauty of its structures.

This structures also support some popular libs/application such as:
- MySQL as relational database
- Redis as message broker to support running background job
- Easiy Deployment Configuration using Gunicorn ( I haven't tried but you could run this project on Docker too )

## Application Features
Flask but Twitter contains minimum requirement for a social media needs, such as:
- Register => common checking if username already registered, it will return a message to user about the error.
- Login => common checking if username and hashed password if equal to given data on form, it will store the user information on session so other features can used it as well.
- Reading available tweets => by querying to database using SQLAlchemy, it's something that won't hurt your head, don't worry.
- Posting a new tweet => well retrieving data from a form about tweet that will be posted, reading the session about user data, and after all condition passed it will ask background job to run a function. So the process will finished quickly before the new tweet stored to database, and the user will go to the page that displaying all tweets without his recent tweet. But, when user reloaded the page, his new tweet will appears because it's running on background. ( It's only a sample use of using background job, you can simply use Javascript and a simple rest api to obtain this without any background job. Background job mostly used on a function that gotta proccess lot of stuff with lot of time, such as generating report. So the user can wait the process to be done by using other features instead of waiting it's loading. )

### Install Requirements Apps
We are using MySQL and Redis, so make sure you already installed them. Installing redis were something new for me, so I'll write it down here.
Go to a directory you used to store downloaded / installed app.

#### Installation
```bash
 $ wget http://download.redis.io/releases/redis-5.0.8.tar.gz
 $ tar -xvf redis-5.0.8.tar.gz
 $ cd redis-5.0.8/
 $ make
 $ sudo make install
```

#### Configuration
after installation finished, we have to configure so the Redis could run properly and can be used from our app.
```bash
$ cd utils/
$ ./install_server.sh
```
you will be asked some questions, keep entering for using default configuration (yes, recommended using this if you are not familiar with changing app port)

#### Check if Redis running properly
```bash
$ sudo service redis_6379 status
```
If it's not running yet, you can run by executing syntax below
```bash
$ sudo service redis_6379 start
```

If running service status give you out Active (running) stuff, let's check out for real by using Redis CLI
```bash
$ redis-cli
```
and it will turn out to be
```bash
127.0.0.1:6379> 
```

Let's try stuff, type 'ping' there
```bash
127.0.0.1:6379> ping
```
and it will return 
```bash
PONG
```
means your Redis is running properly now!

### Project Installation (Linux)
```bash
$ git clone https://github.com/ridhof/twitter-but-flask.git
$ cd twitter-but-flask

$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ python install -r requirements.txt
```

### Setup Environment Secret (env)
Copy .env.example as .env, and fill out the data needed there. Especially database credentials such as database name, user and password for flask to access the database, etc.

#### Setup Database
Before running syntax below, make sure you already created a new database that its name already you filled in env file.
```bash
(venv) $ python manager.py db init
(venv) $ python manager.py db migrate
(venv) $ python manager.py db upgrade
```

#### Running the RQ for Background Job
Execute this syntax on different terminal
```bash
$ rq worker
```

#### Running in Debug Mode
```bash
(venv) $ python manager.py debug
```

#### Running in Production Mode
```bash
(venv) $ python manager.py run
```

### Deployment
Make sure you already installed NGINX Gunicorn etc, check References/Acknowledges how to install it because it's too long to write here.

Say we already installed them, and we already cloned our app to our server on `/home/www`, let's get things started.

```bash
$ cd /home/www/twitter-but-flask
$ source venv/bin/activate
(venv) $ gunicorn manager:app -b localhost:8000
```
And also run another apps, which is Redis Queue or RQ that helps our background job running well. Open a new terminal and go to the same path and run syntax below.
```bash
$ rq worker
```

now check at `youripaddress/` on browser, if it's running well, congratulations!

it was for testing, let's make gunicorn run on background by running syntax below
```bash
$ sudo vim /etc/supervisor/conf.d/twitter-but-flask.conf
```
and copy stuff below to that file
```vim
[program:twitter-but-flask]
command = gunicorn manager:app -b localhost:8000
directory = /home/www/twitter-but-flask
user = your_user
```

don't forget to also add our Redis Queue (RQ) to supervisor too
```bash
$ sudo vim /etc/supervisor/conf.d/rq-worker.conf
```
and copy this
```vim
[program:rq-worker]
command = rq worker
directory = /home/www/twitter-but-flask
user = your_user
```

and now run it
```bash
$ sudo supervisorctl reread
$ sudo supervisorctl update
$ sudo supervisorctl start twitter-but-flask
$ sudo supervisorctl start rq-worker
```
Congratulations, your server is running your Flask properly!

### Acknowledges
- [Flask Restful Structures by @lalala223](https://github.com/lalala223/flask-restful-example)
- [Digital Ocean Large Flask Sturctures](https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications)
- [How to use Database on Flask using SQLAlchemy](https://www.learndatasci.com/tutorials/using-databases-python-postgres-sqlalchemy-and-alembic/)
- [Ubuntu Setup and Deployment for Flask](https://realpython.com/kickstarting-flask-on-ubuntu-setup-and-deployment/)
- [Installing Redis from Source](https://devopsmyway.com/install-redis-on-linux-from-source/)
- [Basic Explanation about Background Job on Flask](https://pythonise.com/series/learning-flask/flask-rq-task-queue)
- [Advance Example about Background Job on Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)

