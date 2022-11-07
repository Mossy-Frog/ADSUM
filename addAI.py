import joblib, os, pickle
from joblib import load
import sklearn
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings("ignore")
def AIprediction(AIsymptoms):
    os.chdir('c:/Users/Maxence/Desktop/BT5/ADSUM')
    os.listdir()

    fileDB = joblib.load("list_symptoms.sav")


    with open('adsum_model.sav' , 'rb') as f:
        fileAI = pickle.load(f)
    text_tokens = word_tokenize(AIsymptoms)

    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    list_pred = [0]*len(fileDB)
    for i in tokens_without_sw:
        j = " " + i
        if i in fileDB :
            a = fileDB.index(i)
            list_pred[a]+=1
        elif j in fileDB:
            a = fileDB.index(j)
            list_pred[a]+=1
    return fileAI.predict([list_pred])[0]