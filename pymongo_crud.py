from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Access the database
db = client["library"]

# Create collections
books_collection = db["books"]
users_collection = db["users"]

# Create
def create_book(title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": year
    }
    inserted_book = books_collection.insert_one(book)
    print("Inserted ID:", inserted_book.inserted_id)

def create_user(name, age):
    user = {
        "name": name,
        "age": age
    }
    inserted_user = users_collection.insert_one(user)
    print("Inserted ID:", inserted_user.inserted_id)

# Read
def find_books(query={}):
    books = books_collection.find(query)
    for book in books:
        print(book)

def find_users(query={}):
    users = users_collection.find(query)
    for user in users:
        print(user)

# Update
def update_book(query, new_values):
    update_result = books_collection.update_one(query, {"$set": new_values})
    print("Matched:", update_result.matched_count)
    print("Modified:", update_result.modified_count)

def update_user(query, new_values):
    update_result = users_collection.update_one(query, {"$set": new_values})
    print("Matched:", update_result.matched_count)
    print("Modified:", update_result.modified_count)

# Delete
def delete_book(query):
    delete_result = books_collection.delete_one(query)
    print("Deleted count:", delete_result.deleted_count)

def delete_user(query):
    delete_result = users_collection.delete_one(query)
    print("Deleted count:", delete_result.deleted_count)

if __name__ == "__main__":
    # Create some example books
    create_book("Introduction to Python", "John Smith", 2020)
    create_book("Web Development Basics", "Jane Doe", 2019)
    create_book("Data Science Essentials", "Alice Johnson", 2021)

    # Create some example users
    create_user("Alice", 28)
    create_user("Bob", 35)
    create_user("Charlie", 22)

    # Find and display books and users
    print("All books:")
    find_books()

    print("All users:")
    find_users()

    # Update books and users
    update_book({"title": "Introduction to Python"}, {"year": 2022})
    update_user({"name": "Bob"}, {"age": 36})

    # Display updated books and users
    print("Updated books:")
    find_books()

    print("Updated users:")
    find_users()

    # Delete books and users
    delete_book({"author": "Jane Doe"})
    delete_user({"name": "Charlie"})

    # Display remaining books and users
    print("Remaining books:")
    find_books()

    print("Remaining users:")
    find_users()