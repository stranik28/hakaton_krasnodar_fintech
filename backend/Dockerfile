FROM python:latest
WORKDIR /backend
RUN apt-get install libmariadb-dev
COPY requirements.txt /backend
RUN pip3 install --upgrade pip -r requirements.txt
RUN pip install -U flask-cors
COPY . /backend
EXPOSE 5000
# RUN gunicorn main:"create_flask_app()" -b 0.0.0.0:5000 --reload
