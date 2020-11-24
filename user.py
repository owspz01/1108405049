from flask_restful import Resource,reqparse
import pymysql
from flask import jsonify
parser=reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('gender')
parser.add_argument('birth')
parser.add_argument('note')
class User(Resource):
    def init_db(self):
        db=pymysql.connect("localhost","root","123456","api")
        cursor=db.cursor(pymysql.cursors.DictCursor)
        return db,cursor
    def get(self,userid):
        db,cursor=self.init_db()
        sql="SELECT*FROM api.users WHERE id={}".format(userid)
        cursor.execute(sql)
        db.commit()
        user=cursor.fetchone()
        db.close()

        return jsonify({'data':user})
    def delete(self,userid):
        db,cursor=self.init_db()
        sql="DELETE FROM api.users WHERE id = {}".format(userid)
        response = {}
        try:
            cursor.execute(sql)
            db.commit()
            response["msg"]="success"
        except:
            response["msg"]="fail" 
        db.close()
        return jsonify(response)
class Users(Resource):
    def init_db(self):
        db=pymysql.connect("localhost","root","123456","api")
        cursor=db.cursor(pymysql.cursors.DictCursor)
        return db,cursor
    def get(self):
        db,cursor=self.init_db()
        sql="SELECT * FROM api.users"
        cursor.execute(sql)
        db.commit()
        users=cursor.fetchall()
        db.close()


        return jsonify(users)

    def post(self):
        db,cursor=self.init_db()
        arg=parser.parse_args()
        user={
            'name':arg['name'],
            'gender':arg['gender'],
            'birth':arg['birth'],
            'note':arg['note'],
        }
        sql="""
        INSERT INTO users (name,gender,note,birth) VALUES('{}','{}','{}','{}');
        """.format(user["name"],user["gender"],user["note"],user["birth"])
        response = {}  
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            response["msg"]="success"
        except:
            response["msg"]="fail" 
        db.close()
        return jsonify(response)
        
