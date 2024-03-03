FROM tiangolo/uvicorn-gunicorn:python3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./app /app 
CMD ["python3", "-Xfrozen_modules=off", "-m", "debugpy", "--listen", "0.0.0.0:5678", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
