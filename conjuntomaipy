from flask import Flask, jsonify, request
from setrest01 import setrest01

app = Flask(__name__) 

# Servicios REST
app.register_blueprint(setrest01)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(host='0.0.0.0', debug=True, port=5000)
