from flask import Flask,jsonify

app = Flask(__name__)
stores = [
    {
        "name": "Dmart",
        "items": [
            {
                "name": "Snikers",
                "price": 25
            }
        ]
    }
]

@app.route('/')
def index():
    return 'OK!'

@app.route('/store')
def get_stores():
    return jsonify({"stores": stores})

if __name__ == '__main__':
    app.run()

