from flask import Flask , json , jsonify,request
from prediction import get_predict

app = Flask(__name__)

@app.route("/predict-alphabet",methods=["POST"])

def predict_data():
    image = request.files.get("alphabet")
    predict = get_predict(image)
    return jsonify({
        "prediction":predict
    }),200
    

if __name__ =="__main__":
    app.run(debug=True)