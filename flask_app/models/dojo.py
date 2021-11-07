from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
    
    @classmethod
    def insert_dojo(cls,data):
        query="INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def get_all_dojos(cls):
        query="SELECT * FROM dojos"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo))
        return dojos
    
    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s"
        all_dojo_ninjas = connectToMySQL("dojos_and_ninjas").query_db(query,data)

        dojo = Dojo(all_dojo_ninjas[0])

        for dojo_njs in all_dojo_ninjas:
            ninja_data = {
                "id": dojo_njs["ninjas.id"],
                "first_name": dojo_njs["first_name"],
                "last_name": dojo_njs["last_name"],
                "age": dojo_njs["age"],
                "dojo_id": dojo_njs["dojo_id"],
                "created_at": dojo_njs["created_at"],
                "updated_at": dojo_njs["updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
            return dojo

    @classmethod
    def insert_ninja(cls,data):
        query="INSERT INTO ninjas (first_name, last_name, age) VALUES (%(fname)s,%(lname)s,%(age)s"
        return connectToMySQL("dojos_and_ninjas").query_db(query,data)