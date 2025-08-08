from flask_restful import Resource, reqparse
from db import get_connection

class User(Resource):
    

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        data = parser.parse_args()
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "User added"}, 201
