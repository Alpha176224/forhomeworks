Task1
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author} ({'Borrowed' if self.is_borrowed else 'Available'})"

class Member:
    MAX_BORROWED_BOOKS = 3
    
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= Member.MAX_BORROWED_BOOKS:
            raise MemberLimitExceededException(f"{self.name} cannot borrow more than {Member.MAX_BORROWED_BOOKS} books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"The book '{book.title}' is already borrowed.")
        
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)

    def __str__(self):
        return f"{self.name} (Borrowed books: {', '.join(book.title for book in self.borrowed_books) if self.borrowed_books else 'None'})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def add_member(self, name):
        self.members.append(Member(name))

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found in the library.")

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        
        book = self.find_book(book_title)
        member.borrow_book(book)
        print(f"{member_name} successfully borrowed '{book_title}'.")
    
    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        if not member:
            raise ValueError(f"Member '{member_name}' not found.")
        
        book = self.find_book(book_title)
        member.return_book(book)
        print(f"{member_name} successfully returned '{book_title}'.")

    def display_books(self):
        for book in self.books:
            print(book)
    
    def display_members(self):
        for member in self.members:
            print(member)

# Test the Library System
library = Library()

# Adding books
library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("1984", "George Orwell")
library.add_book("To Kill a Mockingbird", "Harper Lee")

# Adding members
library.add_member("Alice")
library.add_member("Bob")

# Borrowing books
try:
    library.borrow_book("Alice", "1984")
    library.borrow_book("Alice", "The Great Gatsby")
    library.borrow_book("Alice", "To Kill a Mockingbird")
    library.borrow_book("Alice", "Moby Dick")  # Should raise BookNotFoundException
except Exception as e:
    print(e)

# Attempting to borrow more than 3 books
try:
    library.borrow_book("Alice", "The Great Gatsby")  # Should raise MemberLimitExceededException
except Exception as e:
    print(e)

# Attempting to borrow an already borrowed book
try:
    library.borrow_book("Bob", "1984")  # Should raise BookAlreadyBorrowedException
except Exception as e:
    print(e)

# Returning a book
library.return_book("Alice", "1984")
library.borrow_book("Bob", "1984")  # Now Bob can borrow it

# Display books and members
library.display_books()
library.display_members()



Task2
import csv
from collections import defaultdict

# Step 1: Read the CSV file and store data
grades = defaultdict(list)

with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"])
        grades[subject].append(grade)

# Step 2: Calculate the average grade for each subject
average_grades = {subject: sum(grades_list) / len(grades_list) for subject, grades_list in grades.items()}

# Step 3: Write the results to a new CSV file
with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, round(avg_grade, 2)])

print("Average grades have been calculated and saved to 'average_grades.csv'.")




Task3
import json
import csv

# Load tasks from JSON file
def load_tasks(filename="tasks.json"):
    with open(filename, "r") as file:
        return json.load(file)

# Save tasks to JSON file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    print("\nTask List:")
    print("ID | Task Name         | Completed | Priority")
    print("------------------------------------------------")
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:<15} | {task['completed']}  | {task['priority']}")

# Calculate statistics
def calculate_statistics(tasks):
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks > 0 else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {round(avg_priority, 2)}")

# Convert JSON to CSV
def convert_json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    tasks = load_tasks(json_filename)
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])
    print(f"Tasks have been converted to {csv_filename}.")

# Main execution
tasks = load_tasks()
display_tasks(tasks)
calculate_statistics(tasks)
convert_json_to_csv()


