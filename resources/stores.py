from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help='This field cannot be blank')
    @jwt_required()
    def get(self,name):

        returned_store = StoreModel.find_by_name(name)


        return(returned_store.json(), 200 if returned_store else 404)

    def post(self,name):

        returned_store = StoreModel.find_by_name(name)
        if returned_store:
            return({"message":"Item already exists"})
        store = StoreModel(name)
        store.save_to_db()
        return(store.json())

    def delete(self,name):

        returned_store = StoreModel.find_by_name(name)
        if returned_store is None:
            return({"message":"{} doesn't exists".format(name)})

        returned_store.delete()
        return({"message":"{} deleted".format(name)},200)



class Store_list(Resource):

    def get(self):

        stores = StoreModel.find_all()
        return({'stores':[k.json() for k in stores]})