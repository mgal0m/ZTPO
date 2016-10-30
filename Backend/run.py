from GetUserId import *
from GetNumberOfPublications import *
from GetUserPublications import *
from GetUserInfo import *
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello():
    return "True"

@app.route('/user', methods=['GET']) #?surname&name
def getUser():
    print("Get user started")
    if 'name' and 'surname' in request.args:
        surname = request.args['surname']
        name = request.args['name']
        getUserInfoInstance = GetUserInfo(surname, name)
        data = getUserInfoInstance.getInfo()
        print("Get user finished")
        return data, {'Access-Control-Allow-Origin': '*'} 
    else:
        return 'Something goes wrong', {'Access-Control-Allow-Origin': '*'} 

    
    
if __name__ == "__main__":
    app.run()
        