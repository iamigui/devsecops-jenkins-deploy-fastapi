FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app.py /code/app.py

COPY ./templates /code/templates

ENV BACKEND_URL=http://51.105.208.163:8000

CMD ["flask", "run", "--host=0.0.0.0"]