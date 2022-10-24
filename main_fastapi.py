from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
app = FastAPI() #uvicorn main_fastapi:app --reload


class Patient(BaseModel):
    patient_name :str
    date_joined : str
    location : str
    symptoms : str
    age : int


user_db = {
    'jack': {'patient_name': 'jack', 'date_joined': '2021-12-01', 'location': 'New York', 'age': 28, "symptoms": "cough"},
    'jill': {'patient_name': 'jill', 'date_joined': '2021-12-02', 'location': 'Los Angeles', 'age': 19, "symptoms": "runny_nose"},
    'jane': {'patient_name': 'jane', 'date_joined': '2021-12-03', 'location': 'Toronto', 'age': 52,"symptoms": "amnesia"}
}

@app.get('/users')
def get_users():
    user_list = list(user_db.values())
    return user_list


@app.get('/users/{patient_name}')
def get_users_path(patient_name: str):
    return user_db[patient_name]

@app.post("/users")
def create_patient(user: Patient):
    patient_name =user.patient_name
    user_db[patient_name] = user.dict()
    return {"message": f"Successfully created patient : {patient_name}"}

