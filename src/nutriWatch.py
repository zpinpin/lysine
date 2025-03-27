from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
import certifi

connection_url = 'mongodb+srv://id:password@clusterNumber.ocn1y.mongodb.net/nutriWatch?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url, tlsCAFile=certifi.where())

# Database
Database = client.get_database('crosspantry')
# Table
users = Database.users

def getProfiles():
    query = users.find({},{'name':1})
    output = {}
    names=[]
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        names.append(output[i]["name"])
        i += 1
    return names

# To insert a single document into the database,
# insert_one() function is used
@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
    queryObject = {
        'Name': name,
        'ID': id
    }
    query = users.insert_one(queryObject)
    return "Query inserted...!!!"

# To find the first document that matches a defined query,
# find_one function is used and the query to match is passed
# as an argument.
@app.route('/find-one/<argument>/<value>/', methods=['GET'])
def findOne(argument, value):
    queryObject = {argument: value}
    query = users.find_one(queryObject)
    query.pop('_id')
    return jsonify(query)

# To find all the entries/documents in a table/collection,
# find() function is used. If you want to find all the documents
# that matches a certain query, you can pass a queryObject as an
# argument.
@app.route('/find/', methods=['GET'])
def findAll():
    query = users.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)


# To update a document in a collection, update_one()
# function is used. The queryObject to find the document is passed as
# the first argument, the corresponding updateObject is passed as the
# second argument under the '$set' index.
@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['GET'])
def update(key, value, element, updateValue):
    queryObject = {key: value}
    updateObject = {element: updateValue}
    query = users.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"


if __name__ == '__main__':
    app.run(debug=True)


