FROM python:3.7
RUN python3 -m pip install --upgrade pip

EXPOSE 5000

RUN mkdir /app 
COPY . /app

RUN pip install -r app/code/requirements.txt
RUN pip install -e app/code/.

WORKDIR /app/code

CMD gunicorn --bind :5000 --log-level debug  "smallapp.api:create_api()"