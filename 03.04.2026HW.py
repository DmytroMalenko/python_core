# Task 1

class Book:
    def __init__(self, name, authors, year):
        self.name = name
        self.authors = authors
        self.year = year

    def __str__(self):
        authors_text = ", ".join(self.authors)
        return f'Name: {self.name}\n\tAuthors: {authors_text}\n\tYear: {self.year}'


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.book_list = []

    def __str__(self):
        return f'Name: {self.name}\n\tAddress: {self.address}\n\tAvailable Books: {len(self.book_list)}'
    
    def all_books(self):
        if not self.book_list:
            print("This books wasn't found in our Library!")
        else:
            for book in self.book_list:
                print(book)

    def add_book(self, book):
        self.book_list.append(book)
        print("Book added.")

    def delete_book(self, name):
        new_books = []

        for book in self.book_list:
            if book.name.lower() != name.lower():
                new_books.append(book)

        if len(new_books) == len(self.book_list):
            print("Book wasn't found")
        else:
            self.book_list = new_books
            print("Book deleted")
        
    def search_book_by_name(self, name):
        found = False
        for book in self.book_list:
            if name.lower() in book.name.lower():
                print(book,"was found.")

                found = True

            if not found:
                print(name,"wasn't found.")

    def search_book_by_author(self, author):
        found = False
        for book in self.book_list:
            for a in book.authors:
                if author.lower() in a.lower():
                    print("Found by author:", book)
                    found = True
                    break
        if not found:
            print("Books by",author,"wasn't found")




library = Library("Library", "Garden 253")

while True:
    print("<---------- MENU ---------->")
    print("1. All Books               |")
    print("2. Add Book                |")
    print("3. Delete Book             |")
    print("4. Search book by name     |")
    print("5. Search book by author   |")
    print("6. Exit                    |")
    print("----------------------------")

    choice = input("Choose: ")

    if choice == "1":
        library.all_books()

    elif choice == "2":
        name = input("Write book name: ")
        authors_text = input("Write authors(,): ")
        year = int(input("Enter year: "))
        authors = [a.strip() for a in authors_text.split(",")]
        book = Book(name, authors, year)
        library.add_book(book)

    elif choice == "3":
        name = input("Write book name to delete: ")
        library.delete_book(name)  
        

    elif choice == "4":
        name = input("Enter book name: ")
        library.search_book_by_name(name)


    elif choice == "5":
        author = input("Enter author: ")
        library.search_book_by_author(author)

    elif choice == "6":
        print("End!")
        break
















































