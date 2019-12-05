# file backend/api.py
from flask import Flask
from flask import jsonify
from flask import request, send_from_directory

app = Flask(__name__)

# this function returns an object for one user
def u(user_id):
    return {
        "type": "users",                    # It has to have type
        "id": user_id,                      # And some unique identifier
        "attributes": {                     # Here goes actual payload.
            "info": "data" + str(user_id),  # the only data we have for each user is "info" field
        },
    }

# routes for individual entities
@app.route('/api/users/<user_id>')
def users_by_id(user_id):
    return jsonify({"data": u(user_id)})

# route for all entities
@app.route('/api/users')
def users():
    return jsonify({
        "data": [u(i) for i in range(0,10)]
        })

# default route.
# flask has to serve a file that will be generated later with ember
# relative path is dist/index.html
@app.route('/')
def root():
    return send_from_directory('./dist/', "index.html")

# route for other static files
@app.route('/<path:path>')
def send_files(path):
    try:
      return send_from_directory('./dist/', path)
    except:
      return send_from_directory('./dist/', "index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
