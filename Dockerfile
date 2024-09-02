FROM python:3.11
#FROM python:3.11.9-alpine3.20

#FROM python:3.11.9-slim-bullseye

WORKDIR /code

#COPY . /code/
COPY src/fishmlserv/main.py /code/
#COPY requirements.txt /code/

#COPY ./requirements.txt /code/requirements.txt

#RUN pip install --no-cache-dir --upgrade /code/requirements.txt
RUN pip install --no-cache-dir --upgrade git+https://github.com/HaramSs/fishmlserv.git@0.7/MANIFEST

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
