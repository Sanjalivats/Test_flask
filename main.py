from flask import Flask, request, jsonify
from senetncesimilarity import calculate_similarity

app = Flask(__name__)

# @app.route("/get-user/<user_id>", methods=["GET"])
# def get_user(user_id):
#     user_data = {
#         "user_id": user_id,
#         "name": "John Doe",
#         "email": "john.doe@example.com"
#     }
#     extra = request.args.get("extra")
#     if extra:
#         user_data["extra"] = extra

#     return jsonify(user_data), 200

# @app.route("/create-user",methods=["POST"])
# def create_user():
#     data = request.get_json()

#     return jsonify(data),201

@app.route('/')
def home():
    return"Welcome to the Flask API!"

@app.route("/calculate_score",methods=["POST"])
def calculate_score():
    data = request.get_json()
    sentence1=data["sentence1"]
    sentence2=data["sentence2"]
    similarity = calculate_similarity(sentence1, sentence2)
  
    return jsonify({"score":similarity}),201

if __name__ == "__main__":
    app.run(debug=True)
    
