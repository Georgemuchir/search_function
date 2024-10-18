from models import User, Book
from database import db
from app import app  # Import the Flask app instance to use its context

# Use the application context to avoid working outside of it
with app.app_context():
    # Drop all tables and recreate them to ensure fresh data
    db.drop_all()
    db.create_all()

    # Create some sample users
    users = [
        User(username='user1'),
        User(username='user2'),
        User(username='user3'),
        User(username='user4'),
        User(username='user5'),
    ]

    # Create some sample books and associate them with users
    books = [
        Book(title='Book 1', author='Author 1', user=users[0]),
        Book(title='Book 2', author='Author 2', user=users[0]),
        Book(title='Book 3', author='Author 3', user=users[1]),
        Book(title='Book 4', author='Author 4', user=users[1]),
        Book(title='Book 5', author='Author 5', user=users[2]),
    ]

    # Add users and books to the session
    db.session.add_all(users)
    db.session.add_all(books)

    # Commit the session to save the changes in the database
    db.session.commit()

    print("Sample data populated successfully.")
