FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENV mongo_url=mongodb+srv://capFashion:U2vk7Abh1NIAeBTI@capfashion.z921epc.mongodb.net/?retryWrites=true&w=majority
ENV mongo_collection=posts
ENV mongo_database=capfashion

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]