from flask import Flask, request, make_response, redirect, render_template
import json
import os

app = Flask(__name__)


nombres = ["María", "Lisset", "José", "David", "Sofía"]
ruta = os.path.join("data", "data_dos.json")
with open(ruta, "r") as archivo:
    datos_json = json.load(archivo)


@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/perfil_user"))
    response.set_cookie("user_ip", user_ip_information)
    return response


@app.route("/perfil_user")
def perfil():
    ip_user = request.cookies.get("user_ip")

    context = {"ip_usera": ip_user, "nombres": nombres, "datos": datos_json}
    return render_template("index.html", **context)


@app.route("/user_data")
def user_data():
    return "<h1>DATOS DEL USUARIO</h1>"


app.run(debug=True, host="0.0.0.0", port=3000)
