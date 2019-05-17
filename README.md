Building a log parser with Python
===================
> Learning how to use Python by building a log parser.

Setting up the app
-------------
>Install `pipenv` with the command:
```
pip3 install pipenv
```
>Create the *virtural environment* for the project. From within the project directory. Run the command:
```
pipenv shell
```
This will create a `Pipfile`, which will hold all your project's *dependencies*.
>Install the *dependencies*. From within the project directory. Run the command:
```
pipenv install flask flask-sqlalchemy flask-marshmallow-sqlalchemy
```
>After the *dependencies* have finished installing, you can check the `Pipfile`, it should look like this:
```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
flask = "*"
flask-sqlalchemy = "*"
flask-marshmallow = "*"
marshmallow-sqlalchemy = "*"

[requires]
python_version = "3.6"
```
>Create an `app.py` file, which will hold the *server side* code. From within the project. Run the command:
```
touch app.py
```
>From the `app.py` file, *import* dependencies and modules:
```
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
```
>Initialize the application and run the *server*
```
# Init app
app = Flask(__name__)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)

```
>To run the server, from the *terminal* run the command:
```
python app.py
```
>If successful, the terminal output should look like the following:
```
$ python app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 268-311-121
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
