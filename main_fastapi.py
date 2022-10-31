from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from show_patient import patient_show
from add_patient import patient_add
#launch the fastapi app
app = FastAPI() #uvicorn main_fastapi:app --reload

#Create class for each functions
class User_inputadd(BaseModel):
    patient_name :str
    age : int
    weight : int
    symptoms : str

class User_inputshow(BaseModel):
    param : str

#create callable functions 

@app.post('/show')
def operate(input:User_inputshow):
    result = patient_show(input.param)
    return result


@app.post('/add')
def operateadd(input : User_inputadd):
    resultadd= patient_add(input.patient_name,input.age,input.weight,input.symptoms)
    return resultadd


##uvicorn main_fastapi:app --reload 
#to launch the back end
