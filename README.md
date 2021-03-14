# Introduction to REST-API-flask

**VERY** Simple REST API created on Python using flask.
Running on localhost port 5000.

## Objective:

Create an API that contains the information of a collection of Stores.
- Each Store has a 'name', and a list of 'items'. 
- Each item has a 'name' and a 'price'.
- Test endpoints with Postman.

## Following endpoints are available:

1. POST: /new_store
    - Adds a new store to the collection.
    - Info required: ```{"name": "<store_name>"}```.
    - Returns store created.


2. POST: /stores/<store_name>/new_item
    - Adds a new items to an specific store.
    - Info required: ```{"name": "<item_name>", "price": float}```.
    - Returns item created.
    - Handles error if store not found.


3. GET: /stores
    - Returns all stores.


4. GET: /stores/<store_name>
    - Returns a store by name passed on URL.
    - Handles error if store not found.


5. GET /stores/<store_name>/items
    - Returns all items in a store by name passed on URL.
    - Handles error if store not found.


## Extras:
1. GET: /
    - Use ```render_template()``` method to render 'index.html' as home.
    - Display an alert with all stores information.
    - Test endpoints on a browser. 

## Notes:

1. [```Flask```](https://www.kite.com/python/docs/flask.Flask) : The Flask object implements a WSGI (*Web Server Gateway Interface*) application and acts as the central object. It is passed the name of the module or package of the application. Once it is created it will act as a central registry for the view functions, the URL rules, template configuration and much more.
    - ```app = Flask(__name__)``` : Read this [article](https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class).
    - [```Flask.route()```](https://www.kite.com/python/docs/flask.Flask.route) : A decorator that is used to register a view function for a given URL rule. 
    - [```Flask.run()```](https://www.kite.com/python/docs/flask.Flask.run) : Runs the application on a local development server.

2. [```jsonify(*args)```](https://www.kite.com/python/docs/flask.jsonify) : Creates a Response with the JSON representation of the given arguments with an application/json mimetype. 

3. ```request``` is available to every route and contains all the context of a request made to the said route. 
    - [```request.get_json()```](https://www.kite.com/python/docs/flask.request.get_json) : parses the incoming JSON request data and returns it.
    - IMPORTANT: If the request does not attach a JSON payload: *a body* or the request does not have the proper content-type header, **it will give an error.**

4. [```render_template()```](https://www.kite.com/python/docs/flask.render_template) : Renders a template from the template folder with the given context. 


