import requests
import json
import pandas as pd

apiKey = 'IU8EJLbSHgOT278fSbPYMQQ7IyAKZYiE8eaIoANu' 
foodID = '' 

def nutrient_API(apiKey, foodID):
    #calls get api and json load
    api_resp = json.loads(requests.get('https://api.nal.usda.gov/fdc/v1/' + foodID + '?api_key=' + apiKey).text)
    #only return nutrition information
    api_nutrients = api_resp['foodNutrients']
    #first entry is its description, foodID, and database entry type
    nutrientDict = {"FoodID": [api_resp['description'],foodID, api_resp['dataType']]}

    for items in api_nutrients:
        if 'amount' in items:
            #each entry includes nutrient name, nutrient id, amount, and its respective unit
            nutrientDict.update({(items['nutrient']['name']): [(items['nutrient']['id']),
                (items['amount']),(items['nutrient']['unitName'])]})
        #print(nutrientDict)
    return(nutrientDict)


def phenylfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        phenyl_g=(dataframe['Phenylalanine'][1])
    except KeyError:
        phenyl_g=0
    except:
        raise        
#does some more stuff
    print(f'Phenylanine {phenyl_g}')
    return phenyl_g

def valinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        valine_g=(dataframe['Valine'][1])
    except KeyError:
        valine_g=0
    except:
        raise        
#does some more stuff
    print(f'Valine {valine_g}')
    return valine_g

def threoninefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        threonine_g=(dataframe['Threonine'][1])
    except KeyError:
        threonine_g=0
    except:
        raise        
#does some more stuff
    print(f'Threonine {threonine_g}')
    return threonine_g

def trypfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        tryp_g=(dataframe['Tryptophan'][1])
    except KeyError:
        tryp_g=0
    except:
        raise        
#does some more stuff
    print(f'Trptophan {tryp_g}')
    return tryp_g

def methioninefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        methionine_g=(dataframe['Methionine'][1])
    except KeyError:
        methionine_g=0
    except:
         raise
#does some more stuff
    print(f'Methionine {methionine_g}')
    return methionine_g

def leucinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        leucine_g=(dataframe['Leucine'][1])
    except KeyError:
        leucine_g=0
    except:
         raise
#does some more stuff
    print(f'Leucine {leucine_g}')
    return leucine_g

def isoleucinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        isoleucine_g=(dataframe['Isoleucine'][1])
    except KeyError:
        isoleucine_g=0
    except:
         raise
#does some more stuff
    print(f'Isoleucine {isoleucine_g}')
    return isoleucine_g

def lysinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        lysine_g=(dataframe['Lysine'][1])
    except KeyError:
        lysine_g=0
    except:
        raise
#does some more stuff
    print(f'Lysine {lysine_g}')
    return lysine_g

def histidinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        histidine_g=(dataframe['Histidine'][1])
    except KeyError:
        histidine_g=0
    except:
         raise
#does some more stuff
    print(f'Histidine {histidine_g}')
    return histidine_g

def argininefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        arginine_g=(dataframe['Arginine'][1])
    except KeyError:
        arginine_g=0
    except:
        raise
#does some more stuff
    print(f'Arginine {arginine_g}')
    return arginine_g

def cystinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        cystine_g=(dataframe['Cystine'][1])
    except KeyError:
        cystine_g=0
    except:
         raise
#does some more stuff
    print(f'Cystine {cystine_g}')
    return cystine_g

def glycinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        glycine_g=(dataframe['Glycine'][1])
    except KeyError:
        glycine_g=0
    except:
         raise
#does some more stuff
    print(f'Glycine {glycine_g}')
    return glycine_g

def glutaminefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        glutamine_g=(dataframe['Glutamine'][1])
    except KeyError:
        glutamine_g=0
    except:
         raise
#does some more stuff
    print(f'Glutamine {glutamine_g}')
    return glutamine_g

def prolinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        proline_g=(dataframe['Proline'][1])
    except KeyError:
       proline_g=0
    except:
         raise
#does some more stuff
    print(f'Proline {proline_g}')
    return proline_g

def tyrosinefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        tyrosine_g=(dataframe['Tyrosine'][1])
    except KeyError:
        tyrosine_g=0
    except:
         raise
#does some more stuff
    print(f'Tyrosine {tyrosine_g}')
    return tyrosine_g

def alaninefunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try: 
        alanine_g=(dataframe['Alanine'][1])
    except KeyError:
        alanine_g=0
    except:
         raise
#does some more stuff
    print(f'Alanine {alanine_g}')
    return alanine_g

def proteinfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        protein_g=(dataframe['Protein'][1])
    except KeyError:
        protein_g=0
    except:
         raise
    return protein_g

def calciumfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        calc_g=(dataframe['Calcium, Ca'][1])
    except KeyError:
        calc_g=0
    except:
         raise
    return calc_g

def sugarfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        sugar_g=(dataframe['Sugars, total including NLEA'][1])
    except KeyError:
        sugar_g=0
    except:
         raise
    return sugar_g

def carbfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    carb_g=(dataframe['Carbohydrate, by difference'][1])
    return carb_g

def fiberfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    fiber_g=(dataframe['Fiber, total dietary'][1])
    return fiber_g

def fatfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    fat_g=(dataframe['Total lipid (fat)'][1])
    return fat_g

def energyfunc(foodID):
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    energy_g=(dataframe['Energy'][1])
    return energy_g
    
def essentialAminoAcid(foodID):
    myAminoAcid=[]
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    #print(dataframe)
    #foodname=(dataframe.iat[0,0])
    try: 
        histidine_g=(dataframe['Histidine'][1])
    except KeyError:
        histidine_g=0 
    except:
         raise
    try: 
        isoleucine_g=(dataframe['Isoleucine'][1])
    except KeyError:
        isoleucine_g=0 
    except:
         raise
    try: 
        leucine_g=(dataframe['Leucine'][1])
    except KeyError:
        leucine_g=0         
    except:
         raise
    try: 
         lysine_g=(dataframe['Lysine'][1])
    except KeyError:
        lysine_g=0         
    except:
         raise
    try: 
        methionine_g=(dataframe['Methionine'][1])
    except KeyError:
        methionine_g=0         
    except:
         raise
    try: 
        cystine_g=(dataframe['Cystine'][1])
    except KeyError:
        cystine_g=0         
    except:
         raise
    try: 
        phenyl_g=(dataframe['Phenylalanine'][1])
    except KeyError:
        phenyl_g=0         
    except:
         raise
    try: 
        tyrosine_g=(dataframe['Tyrosine'][1])
    except KeyError:
        tyrosine_g=0         
    except:
         raise
    try: 
        threonine_g=(dataframe['Threonine'][1])
    except KeyError:
        threonine_g=0         
    except:
         raise
    try: 
        tryp_g=(dataframe['Tryptophan'][1])
    except KeyError:
        tryp_g=0         
    except:
         raise
    try: 
        valine_g=(dataframe['Valine'][1])
    except KeyError:
        valine_g=0         
    except:
         raise
    #myAminoAcid.append(f'<b>{foodname}</b>\n')
    myAminoAcid.append(f'Valine: {valine_g}\n')
    myAminoAcid.append(f'Trypofan: {tryp_g}\n')
    myAminoAcid.append(f'Threonine: {threonine_g}\n')
    myAminoAcid.append(f'Tyrosine: {tyrosine_g}\n')
    myAminoAcid.append(f'Lysine: {lysine_g}\n')
    myAminoAcid.append(f'Leucine: {leucine_g}\n')
    myAminoAcid.append(f'Isoleucine: {isoleucine_g}\n')
    myAminoAcid.append(f'Histidine: {histidine_g}\n')
    myAminoAcid.append(f'Methionine: {methionine_g}\n')
    myAminoAcid.append(f'Cystine: {cystine_g}\n')
    myAminoAcid.append(f'Phenyline: {phenyl_g}\n')

    return myAminoAcid 

def conditionalEssentialAminoAcid(foodID):
    myAminoAcid=[]
    dataframe = pd.DataFrame(nutrient_API(apiKey, foodID))
    try:
        arginine_g=(dataframe['Arginine'][1])
    except KeyError:
        arginine_g=0
    except:
        raise
    try:
        glycine_g=(dataframe['Glycine'][1])
    except KeyError:
        glycine_g=0
    except:
         raise
    try:
        proline_g=(dataframe['Proline'][1])
    except KeyError:
        proline_g=0
    except:
        raise
    try:
        alanine_g=(dataframe['Alanine'][1])
    except KeyError:
        alanine_g=0
    except:
         raise
    myAminoAcid.append(arginine_g)
    myAminoAcid.append(arginine_g)
    myAminoAcid.append(proline_g)
    myAminoAcid.append(alanine_g)
    return myAminoAcid 

