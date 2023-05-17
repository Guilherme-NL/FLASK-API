import psycopg2
import requests

conn = psycopg2.connect('postgresql://myuser:123456@127.0.0.1:1234/data-eng')

cursor = conn.cursor()

def createTable():
    try:
        sql = f"CREATE TABLE users (id int GENERATED ALWAYS AS IDENTITY, first_name varchar(255), last_name varchar(255), email varchar(255), gender varchar(255), date_of_birth varchar(255));"
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(str(e))

def addData():
    response = requests.get('https://random-data-api.com/api/users/random_user?size=100')
    data = response.json()

    for obj in data:
        sql = "INSERT INTO users (first_name, last_name, email, gender, date_of_birth) VALUES (%s, %s, %s, %s, %s)"
        val = (obj["first_name"], obj["last_name"], obj["email"], obj["gender"], obj["date_of_birth"])
        cursor.execute(sql, val)
        conn.commit()
        print("sucesso!")
    print("sucesso!")

if __name__ == "__main__":
    #createTable()
    addData()