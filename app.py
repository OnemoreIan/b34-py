from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()
host=os.getenv("DB_HOST")
user=os.getenv("DB_USER")
port = os.getenv("DB_PORT")
password=os.getenv("DB_PASSWORD")
database=os.getenv("DB_NAME")

db_conection = mysql.connector.connect(
    host=host,
    user=user,
    port=port,
    password=password,
    database=database
)

db = SQLAlchemy()

#coneccion

app = Flask(__name__)
db.init_app(app)

#acceso a db


#rutas
@app.route('/item',methods=['GET'])
def default():
    query = "select * from personas"
    return "me muero"


@app.route('/item',methods=['POST'])
def posterior():
    data = request.json
    info = data['texto']
    sql = "insert into personas ()"
    texto = f"mortificacion {info}"
    return texto

@app.route('/item',methods=["DELETE"])
def borrado():
    return "borre un dato"

@app.route('/item',methods=["PUT"])
def edicion():
    return "movimiento"



""" class Ultron:
    def __init__(self,log,moles):
        self.log = log
        self.moles = moles
        pass

    def Imprimir(self):
        print(f"solo imprimo  {self.log}  \n{self.moles}")

    def saludar(self):
        print("solo saludo")
 """



if __name__ == "__main__":
    app.run(debug=True,port=6060)