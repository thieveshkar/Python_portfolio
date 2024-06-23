#Author: Thieveshkar
#Task :Library Database Program

def add_book(library, ISBN, BookTitle):
    if ISBN in library:
        print("Book with ISBN", ISBN, "already exists in the library.")
        return
    else:
        library[ISBN] = BookTitle.upper()
        print("The Book has been added successfully!")

def display_books(library):
    if not library:
        print("Library is empty.")
    else:
        print("Books already exist in the library:")
        for ISBN, title in library.items():
            print("ISBN:", ISBN, "- Title:", title)

def main():
    library = {}
    
    while True:
        print("\nLibrary Management System")
        print("Type '1' to add a new book to the library")
        print("Type '2' to display all books that are there in the library")
        print("Type '3' to Exit the Program")
        
        User_Option = input("Enter your input from the options given (1/2/3): ")
        
        if User_Option == '1':
            ISBN = input("Enter ISBN of the book: ")
            BookTitle = input("Enter title of the book: ")
            add_book(library, ISBN, BookTitle)
        elif User_Option == '2':
            display_books(library)
        elif User_Option == '3':
            print("The program has been stopped")
            break
        else:
            print("Invalid User Option. Try again by entering 1, 2, or 3.")


main()


