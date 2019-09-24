from db import db

class ItemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    store_id = db.Column(db.Integer,db.ForeignKey('store.id'))

    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):

        self.name = name
        self.price = price
        self.store_id = store_id

    @classmethod
    def find_by_name(cls,name,store_id):

        return(ItemModel.query.filter_by(name=name,store_id=store_id).first())

    @classmethod
    def find_all(cls):

        return (ItemModel.query.all())

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def json(self):

        return({'name':self.name,'price':self.price,'store_id':self.store_id})