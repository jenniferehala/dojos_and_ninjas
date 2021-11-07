from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html", dojos=dojos)

@app.route("/insertdojo", methods=["POST"])
def insert_dojo():
    data = {
        "name":request.form["name"]
    }
    Dojo.insert_dojo(data)
    return redirect("/")

@app.route("/dojos/<int:id>")
def get_dojo_ninjas(id):
    data = {
        "id":id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)
    return render_template("showdojo.html", dn=dojo_ninjas)

@app.route("/ninjas")
def ninja():
    return render_template("ninjas.html")

@app.route("/getdojos")
def get_all_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos=dojos)

@app.route("/insertninja", methods=["POST"])
def insert_new_ninja():
    data = {
        "Dojo": request.form["dojo"],
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"]
    }
    Dojo.insert_ninja(data)
    return redirect("ninjas.html")

if __name__ == "__main__":
    app.run(debug=True)