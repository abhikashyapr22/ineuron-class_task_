from flask import request, Flask, jsonify
import mysql.connector as con

app = Flask(__name__)


@app.route("/get_data", methods=['POST'])
def get_data():
    mydb = con.connect(host="localhost", user="root", password="Abhishek@1067", database="mysql_python")
    cursor = mydb.cursor()

    try:
        cursor.execute("select * from user_accounts limit 5")
        data = cursor.fetchall()
        mydb.close()
        return jsonify(data)
    except Exception as e:
        return str(e)


@app.route("/insert", methods=['POST'])
def insert_data():
    mydb = con.connect(host="localhost", user="root", password="Abhishek@1067", database="mysql_python")
    cursor = mydb.cursor()

    first_name = request.json['firstname']
    last_name = request.json['lastname']
    gender = request.json['gender']
    country = request.json['country']
    email = request.json['email']
    create_password = request.json['create_p']
    confirm_password = request.json['confirm_p']

    sql = "INSERT INTO user_accounts " \
          "(First_Name, Last_Name, Gender, Country, Email, Create_password, Confirm_password) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (first_name, last_name, gender, country, email, create_password, confirm_password)

    try:
        cursor.execute(sql, values)
        mydb.commit()
        mydb.close()
        return "success"
    except Exception as e:
        return str(e)


@app.route("/update", methods=['POST'])
def update_data():
    mydb = con.connect(host="localhost", user="root", password="Abhishek@1067", database="mysql_python")
    cursor = mydb.cursor()

    first_name = request.json['firstname']
    email = request.json['email']

    query = "update user_accounts set Email = %s where First_Name = %s "
    values = ([email], [first_name])

    try:
        cursor.execute(query, values)
        mydb.commit()
        mydb.close()
        return "success"
    except Exception as e:
        return str(e)


@app.route("/delete", methods=['POST'])
def delete_record():
    mydb = con.connect(host="localhost", user="root", password="Abhishek@1067", database="mysql_python")
    cursor = mydb.cursor()

    first_name = request.json['firstname']
    query = "delete from user_accounts where First_Name = %s"

    try:
        cursor.execute(query, [first_name])
        mydb.commit()
        mydb.close()
        return "success"
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
