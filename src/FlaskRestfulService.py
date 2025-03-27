from flask import Flask, request,jsonify
from flask_restful import Api, Resource 

webapp = Flask(__name__)
api = Api(webapp)
myFood=dict()
ratioLA = 0
lys = 0
arg = 0
totalRatio = 0

class processor():
    class food():
        def __init__(self, w, l, a):
            self.lysine = float(l)
            self.argenine = float(a)
            self.weight = float(w)


    def doStuff(self):
        data = open("data.txt", "r")
        lines = data.readlines()
        print("Available Food:")
        for line in lines:
            temp = line.split(",")
            print(temp[0])
            myFood[temp[0]] = processor.food(temp[1], temp[2], temp[3])
    
@api.resource('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'name':'Hello - this is GET'}
    
    def post(self):
        #Retrieve the JSON data from the Request and store it in local variable
        jsonData = request.get_json(cache=False)
        #Iterate over the JSON Data and print the data on console
        for key in jsonData:
            print(key,' = ',jsonData[key] )
        #for ky,val in myFood.items():
        #    print(ky,";",val)
                
        temp = myFood[key]
        temp2 = jsonData[key]
        global lys,arg
        lys += temp.lysine * (temp2/temp.weight)
        arg += temp.argenine * (temp2/temp.weight)

        #reference to Global Variable
        global ratioLA
        ratioLA = lys/arg
        ratioLA = totalRatio + ratioLA
        #Converting the response to JSON and returning back to user
        return jsonify(totalRatio = ratioLA)
    
    def put(self):
        return 'Hello world - this is PUT'
    
    def delete(self):
        return 'Hello  - this is DELETE'

if __name__ == '__main__':
    worker=processor()
    worker.doStuff()  
    webapp. run(debug=True)
