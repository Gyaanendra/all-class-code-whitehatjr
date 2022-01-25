
from flask import Flask,jsonify,request

app =  Flask(__name__)

# to create an array of task 

task = [
    {
        "id":1,
        "title":u"studying",
        "description":u"6 hours of school",
        "done":False,
    
    },
    {
        "id":2,
        "title":u"gaming",
        "description":u"weekends",
        "done":False,
    },
     {
        "id":3,
        "title":u"movies & tv series",
        "description":u"2 hours per day ",
        "done":False,
    },
]

@app.route("/add-task",methods=["POST"])

def addtask() :
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"provide the data",
        },400)
    inputtask =  {
        "id":task[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False,
  
    },   
    task.append(inputtask)
    return jsonify({
            "status":"success",
            "message":"task added successfuly",
        },400)
    
    
@app.route("/get-data")

def gettask() :
    return jsonify ({
        "data":task,
        
    })
    

   
if __name__ == "__main__":
    app.run(debug=True)