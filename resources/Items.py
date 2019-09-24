from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import json
from models.Item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=False,
                        help='This field cannot be blank')

    parser.add_argument('store_id',
                        type=float,
                        required=True,
                        help='This field cannot be blank')
    @jwt_required()
    def get(self,name):
        data = Item.parser.parse_args()
        returned_item = ItemModel.find_by_name(name,data['store_id'])
        return(returned_item.json(), 200 if returned_item else 404)

    def post(self,name):

        data = Item.parser.parse_args()
        returned_item = ItemModel.find_by_name(name,data['store_id'])
        if returned_item:
            return({"message":"Item already exists"})
        item = ItemModel(name,data['price'],data['store_id'])
        item.save_to_db()
        return(item.json())

    def delete(self,name):
        data = Item.parser.parse_args()
        returned_item = ItemModel.find_by_name(name,store_id=1)
        if returned_item is None:
            return({"message":"{} doesn't exists".format(name)})

        returned_item.delete()
        return({"message":"{} deleted".format(name)},200)


    def put(self,name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name,data['store_id'])
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()

        return (item.json())


class Items_list(Resource):

    def get(self):

        items = ItemModel.find_all()
        print(items)
        return({'items':[k.json() for k in items]})