FROM python:3.8.5

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD streamlit run --server.port 8501 --server.enableCORS false mainstreamlit.py