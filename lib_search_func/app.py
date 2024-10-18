from flask import Flask, render_template, request, redirect, url_for
from config import Config
from database import db, init_db  # Import `db` and `init_db` from `database.py`
from sqlalchemy import or_
from models import User, Book
from schemas import UserSchema, BookSchema
from sqlalchemy import func


app = Flask(__name__)
app.config.from_object(Config)

# Initialize db and ma using init_db function
init_db(app)

# Initialize schemas
user_schema = UserSchema()
book_schema = BookSchema()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query').strip().lower().replace(" ", "")  # Strip spaces and convert to lowercase
    search_type = request.form.get('search_type')  # Get the search type (user or book)
    
    users = []
    books = []

    if search_type == 'user':
        # Case-insensitive search for users
        users = User.query.filter(func.replace(func.lower(User.username), " ", "").like(f'%{query}%')).all()
    elif search_type == 'book':
        # Case-insensitive and space-agnostic search for books by title or author
        books = Book.query.filter(
            or_(
                func.replace(func.lower(Book.title), " ", "").like(f'%{query}%'),
                func.replace(func.lower(Book.author), " ", "").like(f'%{query}%')
            )
        ).all()

    return render_template('search_results.html', query=query, users=users, books=books, search_type=search_type)

@app.route('/user/<int:user_id>')
def user_books(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user_books.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)

