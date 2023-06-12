class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for index, book in enumerate(self.books,1):
            print(f"{index}. {book}")
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName} Please keep it safe & return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available.")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Hacve a great day ahead") 

class Student: 
    def requestBook(self):
        self.book = input("Enter the book you want to Borrow: ")
        return self.book 
    def returntBook(self):
        self.book = input("Enter the book you want to return: ")
        return self.book 
    
if __name__ == "__main__":
    centralLibrary = Library(["Math" , "Physics", "English", "Algorithms", "Bangla", "Science"])
    # centralLibrary.displayAvailableBooks()
    student = Student()
    while(True):
        welcomeMSg ='''****Welcome to central library****
        Please choose an option:
        1.List all the books
        2.Request a book
        3.Add/Return a book
        4.Exit the library
        '''
        print(welcomeMSg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returntBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great Day ahead ")
            exit()
        else:
            print("Invalid Choice")
        
