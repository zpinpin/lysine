from flask import Flask, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask import request
from r import essentialAminoAcid,energyfunc,carbfunc,fiberfunc,fatfunc,calciumfunc,sugarfunc,proteinfunc,lysinefunc,argininefunc,essentialAminoAcid
from nutriWatch import getProfiles,findOne,findAll,update

webapp = Flask(__name__)

#from flask import Flask, request,jsonify

#webapp = Flask(__name__)
#api = Api(webapp)


class phprocessor():
    myFoodPH=dict()
    avoidSet=set()
    alkalineSet=set()
    acidSet=set()
    ph=0
    totalList = [] 
    phsList = []
    alkalineList = []
    acidList = []
    class food():
        def __init__(self,w,ph):
            self.ph=float(ph)
            self.weight = float(w)

    def doStuff(self):
        data = open("avoid.txt","r")
        lines = data.readlines()
        for line in lines:
            self.avoidSet.add(line.strip())
        print(list(dict.fromkeys(self.avoidSet)))
        data = open("alkaline.txt","r")
        lines = data.readlines()
        for line in lines:
            self.alkalineSet.add(line.strip())
        print(list(dict.fromkeys(self.alkalineSet)))
        data = open("acid.txt","r")
        lines = data.readlines()
        for line in lines:
            self.acidSet.add(line.strip())
        print(list(dict.fromkeys(self.acidSet)))
        data = open("ph5.txt", "r")
        lines = data.readlines()
        for line in lines:
            temp = line.split(",")
            if len(temp) > 1: 
                temp2 = ""
                for position in range(len(temp)-1):
                    temp2 += temp[position]
                try:
                    self.myFoodPH[temp2.strip()] = float(temp[len(temp)-1].strip())
                except ValueError:
                    pass

class processor():
    myFood=dict()
    lys = 0
    arg = 0
    protein = 0
    sugar = 0
    calcium =0
    carb = 0
    fiber = 0
    fat = 0
    cal = 0
    energy = 0
    totalList = []
    class food():
        def __init__(self, id, w, l, a, p, c, f,fat,energy,sugar,calcium):
            self.id = id
            self.protein = float(p)
            self.sugar = float(sugar)
            self.calcium = float(calcium)
            self.carb = float(c)
            self.fiber = float(f) 
            self.fat=float(fat)
            self.energy=float(energy)
            self.lysine = float(l)
            self.argenine = float(a)
            self.weight = float(w)


    def addFood(self):
        self.myFood.update({"Sesame seeds": self.food('170150', 0, 0, 1,0,0,0,0,0,0,0)}) 
        self.myFood.update({"sesame seeds": self.food('170150', 0, 0, 1,0,0,0,0,0,0,0)}) 
        self.myFood.update({"Carrots": self.food('170393', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"carrots": self.food('170393', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"Carrot": self.food('170393', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"carrot": self.food('170393', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"Cheerio": self.food('173884', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"cheerio": self.food('173884', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"Date": self.food('168191', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"date": self.food('168191', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"dates": self.food('168191', 1, 1, 1,0,0,0,0,0,0,0 )})
        self.myFood.update({"Apple, raw, without skin":self.food('171689', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"apple":self.food('171689', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Celery":self.food('169988', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"celery":self.food('169988', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Parmasan Cheese":self.food('171247', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"parmasan Cheese":self.food('171247', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Broccoli":self.food('747447', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"broccoli":self.food('747447', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"English Muffins":self.food('172761', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"English Muffin":self.food('172761', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"English muffin":self.food('172761', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"english muffin":self.food('172761', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"zucchini":self.food('168291', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Zucchini":self.food('168291', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"millet":self.food('169702', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Millet":self.food('169702', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"honey":self.food('169640', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Honey":self.food('169640', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"yogurt":self.food('576215', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"kefir":self.food('718974', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Kefir":self.food('718974', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"bagel":self.food('172666', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"bagels":self.food('172666', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Bagel":self.food('172666', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Bagels":self.food('172666', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"cheese bread":self.food('167944', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"cheese bread":self.food('167944', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Blue cheese":self.food('172175', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"blue cheese":self.food('172175', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"creamcheese":self.food('1514835', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Creamcheese":self.food('1514835', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Blueberry":self.food('171711', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"blueberry":self.food('171711', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Shrimp":self.food('174210', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"shrimp":self.food('174210', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"peanut":self.food('174263', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Peanut":self.food('174263', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Tomato":self.food('170463', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"tomato":self.food('170463', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Walnut oil":self.food('171030', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"walnut oil":self.food('171030', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Oatmeal":self.food('172972', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"oatmeal":self.food('172972', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Egg":self.food('747997', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"egg":self.food('747997', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Green Chili Pepper":self.food('168577', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"green chili pepper":self.food('168577', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Swiss Chard":self.food('169991', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"swiss chard":self.food('169991', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Strawberry":self.food('167762', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"strawberry":self.food('167762', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Kale":self.food('168421', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"kale":self.food('168421', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"almond":self.food('170567', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Almond":self.food('170567', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Tofu":self.food('172461', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"tofu":self.food('172461', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Mango":self.food('169910', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"mango":self.food('169910', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Orange":self.food('169918', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"orange":self.food('169918', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"American Cheddar Cheese":self.food('169901', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"american cheddar cheese":self.food('169901', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Quail":self.food('169902', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"quail":self.food('169902', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"pheasant":self.food('169903', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Pheasant":self.food('169903', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"dove":self.food('169905', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Dove":self.food('169905', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Mulberries":self.food('169913', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"mulberries":self.food('169913', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"nectarines":self.food('169914', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"nectarines":self.food('169914', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Black Bean":self.food('173734', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"blackbean":self.food('173734', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Cucumber":self.food('168409', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"cucumber":self.food('168409', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Pork":self.food('172931', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"pork":self.food('172931', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Beef":self.food('168630', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"beef":self.food('168630', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Chicken Tender":self.food('173321', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"chicken tender":self.food('173321', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Chicken":self.food('173613', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"chicken":self.food('173613', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Turkey":self.food('171505', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"turkey":self.food('171505', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Corn":self.food('168920', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"corn":self.food('168920', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Rice":self.food('167967', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"rice":self.food('167967', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Salmon":self.food('173688', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"salmon":self.food('173688', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Spinach":self.food('168462', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"spinach":self.food('168462', 1, 1, 1,0,0,0,0,0,0,0) })
        self.myFood.update({"Romaine Lettuce":self.food('169247', 1, 1, 1,0,0,0,0,0,0,0) })

    def doStuff(self):
        data = open("data.txt", "r")
        lines = data.readlines()
        print("Available Food:")
        for line in lines:
            temp = line.split(",")
            print(temp[0])
            self.myFood[temp[0]] = processor.food(temp[1], temp[2], temp[3])
    
@webapp.route('/find-profile/<argument>/<value>/',methods=['GET'])
def findProfile(argument,value):
        myprofile=findOne(argument,value).json;
        mybmi=myprofile["weight"]/int(myprofile["height"])/int(myprofile["height"]) * 703
        return render_template('profileTemplate.html',name=myprofile["name"],age=myprofile["age"],weight=myprofile["weight"],height=myprofile["height"],bmi=mybmi,gender=myprofile["gender"],maxprotein=myprofile["profile"]["maxprotein"],maxcalcium=myprofile["profile"]["maxcalcium"],maxenergy=myprofile["profile"]["maxenergy"],email=myprofile["email"])

@webapp.route("/ph",methods=["GET","POST","PUT","DELETE"])
def phFinder():

    if request.method == "GET":
        return redirect(url_for('static',filename='staticHTMLFile.html'))

    if request.method == "POST":
        if request.form.get('submit_r') == 'REFRESH':
            phworker.phsList=[]
            phworker.totalList=[] 
            phworker.alkalineList=[]
            phworker.acidList=[]
            return render_template('dynamicPhTemplate.html',foodname='',foodlist=phworker.totalList,phvalue=0,phslist=phworker.phsList,alkaline=phworker.alkalineList,acid=phworker.acidList,akRatio=0)
        temp= request.form.get("foodname")
        temp2 = int(request.form.get("serving"))
        #temp2 = 1
        phworker.totalList.append(request.form.get("foodname"))
        print("post request for food")
        print(temp)
        print(phworker.myFoodPH)
        if temp in phworker.avoidSet:
            phValue=-1
        else:
            phValue=phworker.myFoodPH.get(temp,3)
        if temp in phworker.alkalineSet:
            phworker.alkalineList.append(temp)
        if temp in phworker.acidSet:
            phworker.acidList.append(temp)
        phworker.phsList.append(phValue)
        aRatio=0
        aRatio=str(len(phworker.alkalineList))+' : '+str(len(phworker.acidList))
        return render_template('dynamicPhTemplate.html',foodname=temp,foodlist=phworker.totalList,phvalue=phValue,phslist=phworker.phsList,alkaline=phworker.alkalineList,acid=phworker.acidList,akRatio=aRatio)
 
@webapp.route("/nutri",methods=["GET","POST","PUT","DELETE"])
def HelloWorld():
    
    if request.method == "GET":
        return redirect(url_for('static',filename='staticHTMLFile.html'))
                
    if request.method == "POST":

        if request.form.get('submit_r') == 'REFRESH':
            totalRaio=0
            lysineworker.protein=0
            lysineworker.sugar=0
            lysineworker.calcium=0
            lysineworker.carb=0
            lysineworker.fiber=0
            lysineworker.fat=0
            lysineworker.cal=0
            lysineworker.energy=0
            lysineworker.lys=0
            lysineworker.arg=0
            lysineworker.totalList=[]
            return render_template('dynamicTemplate.html',profilename=request.form.get("profile"), names=getProfiles(),foodlist='',calcium=0,sugar=0,protein=0,carb=0,fiber=0,fat=0,cal=0,name=0)
        msg=[]
        print(request.form.get("profile"))
        try:
            temp = lysineworker.myFood[request.form.get("foodname")]
        except KeyError:
            temp = 0
            msg.append(f'Error:  {request.form.get("foodname")} is not in the database.')
            msg.append(f'Existing foods in the database are listed as follows:')
            msg.append(', '.join([str(key) for key in lysineworker.myFood.keys()]))
        except:
            raise
        if (temp == 0):
            return render_template('dynamicTemplate.html',profilename=request.form.get("profile"), names=getProfiles(),messages=msg,foodlist='',calcium=0,sugar=0,protein=0,carb=0,fiber=0,fat=0,cal=0,name=0)
              
        temp2 = float(request.form.get("serving"))
        lysineworker.totalList.append(request.form.get("foodname"))
        lysineworker.lys += lysinefunc(temp.id) * (temp2/temp.weight)
        lysineworker.arg += argininefunc(temp.id) * (temp2/temp.weight)
        lysineworker.fat += fatfunc(temp.id) * (temp2/temp.weight)
        lysineworker.protein += proteinfunc(temp.id) * (temp2/temp.weight)
        lysineworker.sugar += sugarfunc(temp.id) * (temp2/temp.weight)
        lysineworker.calcium += calciumfunc(temp.id) * (temp2/temp.weight)
        lysineworker.carb += carbfunc(temp.id) * (temp2/temp.weight)
        lysineworker.fiber += fiberfunc(temp.id) * (temp2/temp.weight)
        lysineworker.cal += lysineworker.protein * 4 +lysineworker.fat * 9 + lysineworker.carb *4
        lysineworker.energy += energyfunc(temp.id) * (temp2/temp.weight)
        if lysineworker.arg:
             ratioLA = lysineworker.lys/lysineworker.arg
        else:
             ratioLA = 0
        totalRatio=ratioLA
        str1 = " "
        strlist = ' '.join([str(elem) for elem in lysineworker.totalList])
        print(strlist)
        me=findOne("name",request.form.get("profile")).json;
        goodC=0
        if (lysineworker.calcium > me["profile"]["maxcalcium"]):
            goodC=1
        goodP=0
        if (lysineworker.protein > me["profile"]["maxprotein"]):
            goodP=1
        goodS=0
        if ((lysineworker.sugar*3.82)<(lysineworker.energy*0.1)):
            goodS=1
        return render_template('dynamicTemplate.html',profilename=request.form.get("profile"), names=getProfiles(),fdname=request.form.get("foodname"),sugar=lysineworker.sugar,maxsugar=int(lysineworker.energy/3.824),calcium=lysineworker.calcium,goodCalcium=goodC,goodSugar=goodS,goodProtein=goodP,amino=essentialAminoAcid(temp.id),foodlist=lysineworker.totalList,protein=lysineworker.protein,carb=lysineworker.carb,fiber=lysineworker.fiber,fat=lysineworker.fat,cal=lysineworker.energy,name=totalRatio)

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


@webapp.route("/boneHealth", methods=['GET'])
def showBoneStaticFiles():
    
    return " Hello World!"


@webapp.route("/phFinder/<name>")
def renderPhDynamicContent(name=None):
    return render_template('dynamicPhTemplate.html',name=name)

@webapp.route("/lysineFinder/<name>")
def renderDynamicContent(name=None):
    return render_template('dynamicTemplate.html',profile=request.form.get("profile"), names=getProfiles(),name=name)

if __name__ == '__main__':
    phworker=phprocessor()
    phworker.doStuff()  
    lysineworker=processor()
    lysineworker.addFood() 
    #lysineworker.doStuff()  
    #print(phworker.myFoodPH)
    webapp.run(host='0.0.0.0',port=8999,debug=True)
