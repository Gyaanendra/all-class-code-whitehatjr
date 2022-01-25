from flask import Flask
# to create constructor for flask class
app = Flask(__name__)
# to create a decorator to tell which url should call the function
@app.route("/")

def helloworld() :
    return "Hello people"
    
#  to run the application 
if __name__ == "__main__":
    app.run(debug=True)
    
    
    
# set FLASK_APP=app.py
# flask run