This is a repo for a Flask template using the application factory pattern.

/*
https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/
*/

To create the database:

>> python
>> from app import db, create_app
>> db.create_all(app=create_app('default'))

To run the app:

>> set FLASK_APP=flask_app.py
>> set FLASK_DEBUG=1
>> flask run

