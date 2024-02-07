from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import Book, Category, Author, db
from flask_restful import Resource, Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

migrate = Migrate(app, db)
api = Api(app)
db.init_app(app)

@app.route('/')
def home():
    return 'BOOK-REVIEW'

class Books(Resource):
    def get(self):
        books = Book.query.all()
        book_dict = [book.serialize() for book in books]
        return jsonify(book_dict)

api.add_resource(Books, '/books')

class BooksById(Resource):
    def get(self, id):
        book = Book.query.get(id)
        if not book:
            return {'error': 'Book not found'}, 404
        return jsonify(book.serialize())

    def delete(self, id):
        book = Book.query.get(id)
        if not book:
            return {'error': 'Book not found'}, 404
        db.session.delete(book)
        db.session.commit()
        return jsonify(book.serialize()), 201

api.add_resource(BooksById, '/books/<int:id>')

class Categories(Resource):
    def get(self):
        categories = Category.query.all()
        category_dict = [category.serialize() for category in categories]
        return jsonify(category_dict)

api.add_resource(Categories, '/categories')

class CategoriesById(Resource):
    def get(self, id):
        category = Category.query.get(id)
        if not category:
            return {'error': 'Category not found'}, 404
        return jsonify(category.serialize())

    def patch(self, id):
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        genre = data.get('genre')
        category = Category.query.get(id)
        if not category:
            return {'error': 'Category not found'}, 404
        category.name = name
        category.description = description
        category.genre = genre
        db.session.commit()
        return jsonify(category.serialize()), 201

api.add_resource(CategoriesById, '/categories/<int:id>')

class Authors(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        nationality = data.get('nationality')
        new_data = Author(name=name, nationality=nationality)
        db.session.add(new_data)
        db.session.commit()
        return jsonify(new_data.serialize()), 200

api.add_resource(Authors, '/authors')

if __name__ == '__main__':
    app.run(port=5555)

   



   