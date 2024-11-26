from flask import Flask, jsonify, request 

app = Flask(__name__) 

@app.route('/hello', methods=['GET']) 
def helloworld(): 
    data = {"name": "Hello Somnath"}
    return jsonify(data) 


if __name__ == '__main__': 
	app.run(debug=True, host="0.0.0.0", port=5001) 
