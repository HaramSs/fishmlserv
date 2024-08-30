FROM python:3.11
#FROM python:3.11.9-slim-bullseye


WORKDIR /code

#COPY ./requirements.txt /code/requirements.txt

COPY . /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


CMD ["uvicorn", "src.fishmlserv.main:app", "--host", "0.0.0.0", "--port", "8765"]

