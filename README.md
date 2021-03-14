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
    - Info required: {"name": "<store_name>"}.
    - Returns store created.


2. POST: /stores/<store_name>/new_item
    - Adds a new items to an specific store.
    - Info required: {"name": " <item_name> ", "price": float }.
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
    - Use render_template() method to render 'index.html' as home.
    - Display an alert with all stores information.
    - Test home endpoint on a browser.
