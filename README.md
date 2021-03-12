# REST-API-flask

Simple REST API created on Python using flask.

## Objective:

Create an API that contains the information of a collection of Stores.
- Each Store has a 'name', and a list of 'items'. 
- Each item has a 'name' and a 'price'.

## Following endpoints are available:

1. POST: /new_store
- Adds a new store to the collection.
- Info required: {"name": "<store_name>"}
- Return store created

2. POST: /stores/<store_name>/new_item
- Adds a new items to an specific store.
- Info required: {"name": " <item_name> ", "price": float }
- Return item created.
- Handle error if store not found.




3. GET: /stores
- Reads all stores

4. GET: /stores/<store_name>
- Reads a store by name

5. GET /stores/<store_name>/items
- Reads all items in a store by name

Extra:
- Test GET endpoints with javascript.
- Use render_template to render 'index.html' as home route.
- Alert results.
