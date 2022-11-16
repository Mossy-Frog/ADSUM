#Import all modules
import joblib, os, pickle
from joblib import load
import sklearn
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
import shap
#remove unwanted warnings
warnings.filterwarnings("ignore")
#def the function that will be called by the backend
def AIprediction(AIsymptoms):
    #need to be fixed, tells where to look for files
    os.chdir('c:/Users/Maxence/Desktop/BT5/ADSUM/backend')
    os.listdir()
    #load list of symptoms in the DB
    fileDB = joblib.load("list_symptoms.sav")

    #load AI
    with open('adsum_model.sav' , 'rb') as f:
        fileAI = pickle.load(f)
    #transform string of symptoms given by doctor to a list of words
    text_tokens = word_tokenize(AIsymptoms)
    #remove stopwords
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    #create empty list of a length of the different possible disease
    list_pred = [0]*len(fileDB)
    #the loop will fill the empty list with ones corresponding to the presence symptoms
    for i in tokens_without_sw:
        j = " " + i
        if i in fileDB :
            a = fileDB.index(i)
            list_pred[a]+=1
        elif j in fileDB:
            a = fileDB.index(j)
            list_pred[a]+=1
    #prediction of the AI
    probalist = fileAI.predict_proba([list_pred])[0]
    #transform array of disease and probabilities to a list
    probalist = probalist.tolist()
    #classes will contain every possible disease for the AI
    classes = fileAI.classes_
    maxprobas = []
    synclass = []
    #find the 3 most probables disease and their according probabilities
    for i in range(3):
        maxprobas.append(max(probalist))
        synclass.append(classes[probalist.index(max(probalist))])
        probalist.remove(max(probalist))
    fintext = "La première possibilité est "+ str(synclass[0]) + " avec une probabilité de " + str(maxprobas[0]) + " la deuxième probabilité est " + str(synclass[1]) + " avec " + str(maxprobas[1]) + " et la dernière " + str(synclass[2]) +" Avec " + str(maxprobas[2])   
    #return the text for the backend then the frontend 
    return fintext