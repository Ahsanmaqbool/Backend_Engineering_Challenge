from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token
from passlib.hash import sha256_crypt


app = Flask(__name__)

# Configure the Flask app for JWT
app.config['JWT_SECRET_KEY'] = '123'  
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  

jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost:3306/e_commerce'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# db.init_app(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    price = db.Column(db.Float())
    quantity = db.Column(db.Float())

    def serialize(self):
        return {
                'id': self.id, 
                'name': self.name, 
                'price': self.price, 
                'quantity': self.quantity
            }
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        # Hash the password using passlib's sha256_crypt
        self.password = sha256_crypt.hash(password)

    def check_password(self, password):
        # Verify the password using passlib's sha256_crypt
        return sha256_crypt.verify(password, self.password)
    
# Your other routes and configurations

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = User.query.filter_by(username=username).first()
    # print("User:", user, "Username:", username, "Password:", password)

    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 400


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the username already exists in the database
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"msg": "Username already exists"}), 400

    # Create a new user
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    # Create and return an access token for the newly registered user
    access_token = create_access_token(identity=new_user.id)
    return jsonify(access_token=access_token), 201

@app.route('/')
def start():
    return 'Application is been started, hit /products to continue.'

@app.route('/products')
def get_all_products():
    return jsonify(products=[p.serialize() for p in Product.query.all()])
    
@app.route('/products/<int:_id>', methods=['GET'])
def get_product(_id):
    product = Product.query.get(_id)
    if not product:
        return jsonify(success=False), 404
    return jsonify(product.serialize())
    
@app.route('/products', methods=['POST'])
def create_product():
    p = {'name':request.json.get('name'), 'price':request.json.get('price'), 'quantity':request.json.get('quantity')}
    product = Product(**p)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.serialize()), 201

@app.route('/products/<int:_id>', methods=['PUT'])
def update_product(_id):
    product = Product.query.get(_id)
    if not product:
        return jsonify(success=False), 404
    product.name = request.json.get('name')
    product.price = request.json.get('price')
    product.quantity = request.json.get('quantity')
    db.session.add(product)
    db.session.commit()
    return jsonify(product.serialize())
    
@app.route('/products/<int:_id>', methods=['DELETE'])
def delete_product(_id):
    product = Product.query.get(_id)
    if not product:
        return jsonify(success=False), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify(success=True)

# Creating tables if they do not exist
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)