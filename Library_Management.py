#modules
from operations import *
#program
global s_name

if __name__ == "main":
    s_name = input("Enter your name to take entry in Library : ")

    lib = library()

    ch = 'y'
    while ch == 'y' or ch == 'yes':
        
        print(f"Welcome {s_name} to Library")
        print("Choose an option...\n")
        print("\nList book(s) (L)")
        print("View book(s) (V)")
        print("Add book(s) (A)")
        print("Delete book(s) (D)")
        choice = input("\nEnter the option : ").lower()

        if choice == 'L':
            lib.list_books()

            choice = input("Do you want to see the details of book(s) ?(y/n) : ").lower()

            if choice == 'y' or choice == 'yes':
                s_no_of_books = input("Enter the serial no. of books (seprated by comma (,) ) : ").split(",")
                lib.details(s_no_of_books)