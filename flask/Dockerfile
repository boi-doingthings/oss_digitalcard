FROM python:3.9
ADD . /app
WORKDIR /app
RUN pip3 install flask pymongo passlib
EXPOSE 5000
ENV FLASK_APP=apps.py
ENV admin_user=admin_user
ENV admin_pass=pass123