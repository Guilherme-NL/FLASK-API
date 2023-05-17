from flask import Flask, jsonify, render_template, request
import requests
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


import sqlalchemy

app = Flask(__name__)

username = "myuser"
password = "123456"
host = "35.198.24.35"
port = "5432"
database = "data-eng"
postgres = "postgresql+pg8000://" + username + ":" + password + "@" + host  + ":" + port + "/" + database

engine = create_engine(postgres)
Session = sessionmaker(bind=engine)
Base = declarative_base()

#db=SQLAlchemy(app)

# class User(Model):
#     __tablename__= 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50))
#     last_name = db.Column(db.String(50))
#     email = db.Column(db.String(50))
#     gender = db.Column(db.String(50))
#     date_of_birth = db.Column(db.String(50))

#     def __init__(self, first_name, last_name, email, gender, date_of_birth):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.email=email
#         self.gender=gender
#         self.date_of_birth=date_of_birth


# @app.route("/users", methods=['POST'])
# def post_post():

#     response = requests.get('https://random-data-api.com/api/users/random_user?size=100')
#     data = response.json()
    
#     for obj in data:
#         user=User(obj["first_name"], obj["last_name"], obj["email"], obj["gender"], obj["date_of_birth"])
#         db.session.add(user)
#         db.session.commit()
#     print("sucesso!")
#     return "ok"


@app.route("/users", methods=['GET'])
def get_posts():
    session = Session()
    sql = text("SELECT * FROM users;")
    result = session.execute(sql)
    data = [{'id': row[0], 'first_name': row[1], 'last_name': row[2], 'email': row[3], 'gender': row[4], 'date_of_birth': row[5]} for row in result]
    session.close()
    print(data)

    # json_data = []
    # for item in data:
    #     json_data.append({
    #         "id": item.id,
    #         "first_name" : item.first_name,
    #         "last_name" : item.last_name,
    #         "email" : item.email,
    #         "gender" : item.gender,
    #         "date_of_birth" : item.date_of_birth
    #     })
    return data
    

@app.route("/subscription", methods=['GET'])
def get_subscription():
    response = requests.get('https://random-data-api.com/api/subscription/random_subscription?size=100')
    data = response.json()
    for i, obj in enumerate(data):
        obj['userId'] = i + 1
    return data

if __name__ == '__main__':
    app.run(port=5000, host="localhost", debug=True)