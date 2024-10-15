from ecommerceweb import db, login_manager
from datetime import datetime
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from ecommerceweb import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contactno = db.Column(db.Numeric(10,0), unique=True)
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Seller(db.Model, UserMixin):
    __tablename__="seller"
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(75), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    contactno = db.Column(db.Numeric(10,0), unique=True)
    address_line1 = db.Column(db.String(50))
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer)
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    country = db.Column(db.String(50))
    description = db.Column(db.String(300))
    website = db.Column(db.String(120))

    def __repr__(self):
        return f"Seller('{self.name}', '{self.email}')"

class Category(db.Model):
    __tablename__="category"
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    __tablename__="product"
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    details = db.Column(db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(Category.__table__.c.cid), nullable=False)
    sid = db.Column(db.Integer, db.ForeignKey(Seller.__table__.c.sid), nullable=False)
    image_file1 = db.Column(db.LargeBinary, nullable=False, default='default.jpg')
    image_file2 = db.Column(db.LargeBinary, default='default.jpg')
    image_file3 = db.Column(db.LargeBinary, default='default.jpg')
    image_file4 = db.Column(db.LargeBinary, default='default.jpg')
    stock = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    __tablename__="order"
    oid = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), nullable=False)
    pid = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    order_status = db.Column(db.String, nullable=False)

class Shipping(db.Model):
    __tablename__="shipping"
    ship_id = db.Column(db.Integer, primary_key=True)
    oid = db.Column(db.Integer, db.ForeignKey(Order.__table__.c.oid), nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    details = db.Column(db.String(100))
    contactno = db.Column(db.Integer, unique=True, nullable=False)
    address_line1 = db.Column(db.String(50), nullable=False)
    address_line2 = db.Column(db.String(50))
    address_line3 = db.Column(db.String(50))
    pincode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)


class Cart(db.Model):
    __tablename__="cart"
    uid = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), primary_key=True)
    pid = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

class Review(db.Model):
    __tablename__="review"
    user_id = db.Column(db.Integer, db.ForeignKey(User.__table__.c.id), primary_key=True, nullable=False)
    prod_id = db.Column(db.Integer, db.ForeignKey(Product.__table__.c.pid), primary_key=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(300), nullable=False)
    user_name = db.Column(db.String(75))

    def __repr__(self):
        return f"Review('{self.user_id}', '{self.prod_id}')"