FROM python:3.9

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt
RUN pip install scikit-optimize

CMD ["uvicorn", "main_fastapi:app" ,"--reload", "--host" ,"0.0.0.0"]