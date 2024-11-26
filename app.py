from flask import Flask, jsonify, request 

app = Flask(__name__) 

@app.route('/hello', methods=['GET']) 
def hello_user(): 
    json_data = {
        "name": "Hello Somnath",
        "email": "somanathg238@gmail.com"
    }
    return jsonify(json_data) 


if __name__ == '__main__': 
	app.run(debug=True, host="0.0.0.0", port=5001) 
