import sqlite3
from flask_restful import  Resource
from flask_restful import reqparse
from models.user import UserModel

class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("username",type = str , required = True,
                        help = "This field cannot be null")
    parser.add_argument("password", type=str, required=True,
                        help="This field cannot be null")

    def post(self):

        data = UserRegistration.parser.parse_args()
        # Checking for existing user in the data base
        if UserModel.find_by_username(data['username']):

            return ({"message": "user already in the data base"}, 400)


        # connection = sqlite3.connect('./test.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO users VALUES (NULL,?,?)"
        #
        # cursor.execute(query,(data['username'],data['password']))
        # connection.commit()
        # connection.close()

        user = UserModel(username=data['username'],password=data['password'])
        user.register()

        return({"message": "user created successfully"},201)


