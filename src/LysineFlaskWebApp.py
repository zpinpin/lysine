from flask import Flask, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask import request

webapp = Flask(__name__)

#from flask import Flask, request,jsonify

#webapp = Flask(__name__)
#api = Api(webapp)
myFood=dict()
ratioLA = 0
lys = 0
arg = 0
totalRatio = 0
totalList = []

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
    
@webapp.route("/hello",methods=["GET","POST","PUT","DELETE"])
def HelloWorld():

    if request.method == "GET":
        return redirect(url_for('static',filename='staticHTMLFile.html'))
                
    if request.method == "POST":
        temp = myFood[request.form.get("foodname")]
        temp2 = int(request.form.get("serving"))
        global totalList,lys,arg
        totalList.append(request.form.get("foodname"))
        lys += temp.lysine * (temp2/temp.weight)
        arg += temp.argenine * (temp2/temp.weight)
        #reference to Global Variable
        global ratioLA,totalRatio
        ratioLA = lys/arg
        totalRatio=ratioLA
        str1 = " "
        strlist = ' '.join([str(elem) for elem in totalList])
        print(strlist)
        return render_template('dynamicTemplate.html',foodlist=strlist,name=totalRatio)

    if request.method == "PUT":
        return redirect(url_for('static',filename='staticHTMLFile.html'))
    
    if request.method == "DELETE":
        return redirect(url_for('static',filename='staticHTMLFile.html'))

@webapp.route("/")
def hello():
    return " Hello World!"

@webapp.route("/static", methods=['GET'])
def showStaticFiles():
    
    return redirect(url_for('static',filename='staticHTMLFile.html'))

@webapp.route("/showDynamic/<name>")
def renderDynamicContent(name=None):
    return render_template('dynamicTemplate.html',name=name)


if __name__ == '__main__':
    worker=processor()
    worker.doStuff()  
    webapp.run(host='0.0.0.0',port=8999,debug=True)
