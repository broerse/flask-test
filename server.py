# file backend/api.py
from flask import Flask
from flask import request, send_from_directory

app = Flask(__name__)

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
