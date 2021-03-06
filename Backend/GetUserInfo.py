from GetUserId import *
from GetNumberOfPublications import *
from GetUserPublications import *
import json


class GetUserInfo():
    surname = ""
    name = ""
    def __init__(self, surname, name):
        self.surname = surname.capitalize()
        self.name = name.capitalize()
    
    def getInfo(self):
        data = {}
        userInfoInstance = GetUserId()
        print("get user id")
        userId = userInfoInstance.getId(self.surname, self.name)
        if userId == None:
            data['id'] = 'None'
            json_data = json.dumps(data)
            return json_data
        else:
            data['id'] = userId
            numberOfPubInstance = GetNumberOfPublications()
            print("get user publications number")
            pubNumber = numberOfPubInstance.getNumberOfPublications(userId)
            data['pubNumber'] = pubNumber
            json_data = json.dumps(data)
            userPubInstance = GetUserPublications()
            print("Get user publications list")
            title, typeName, form, date, mniswPoints = userPubInstance.getAllPublications(userId, pubNumber)
            publications = []
            pubNumber = int(pubNumber)
            sumOfPoints = 0
            for i in range(pubNumber):
                row = {}
                row['title'] = title[i]
                row['type'] = typeName[i]
                row['form'] = form[i]
                row['date'] = date[i]
                row['points'] = mniswPoints[i]
                if mniswPoints[i] != 'None':
                    sumOfPoints+=int(mniswPoints[i])
                publications.append(row)
            data['publications'] = publications
            data['allPoints'] = sumOfPoints
            json_data = json.dumps(data, skipkeys=True) 
            return json_data
            
