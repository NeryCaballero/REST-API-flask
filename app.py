from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

stores = [
    {
        'name': 'Store1',
        'items': [
            {
                'name':  'Item1',
                'price': 115.99
            }
        ]
    },
    {
        'name': 'Store2',
        'items': [
            {
                'name':  'Item2',
                'price': 56.99
            }
        ]
    }
]


# POST /new_store data: {name:}
@app.route('/new_store', methods=['POST'])
def create_store():
    request_data = request.get_json()       # get_json() transforms json to dict
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# POST /stores/<store_name>/item{name:, price:}
@app.route('/stores/<string:name>/new_item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()  # get_json() transforms json to dict
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':  request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# GET /stores
@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})      # jsonify transforms our dict into a json str


# GET /stores/<store_name>
@app.route('/stores/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /stores/<store_name>/items
@app.route('/stores/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


# Extra :
# GET /
@app.route('/')
def home():
    return render_template('index.html')


app.run(port=5000)
