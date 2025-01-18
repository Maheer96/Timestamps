from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name', 'World')
    return f'Hello People, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
