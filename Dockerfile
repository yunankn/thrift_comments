FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

COPY ./entrypoint.sh /code/entrypoint.sh

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
