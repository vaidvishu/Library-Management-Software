
class library:
    def __init__(self):
        __book_name = "book1"
        __publisher_name = ""
        __writer_name = ""
        __category = ""
        __book_id = ""

    def add_book(self):
        library.__book_name = input("Enter the Book Name : ")
        print(f"Enter the details of {library.__book_name}")
        library.__publisher_name = input(" ->Enter the Publisher Name : ")
        library.__writer_name = input(" ->Enter the Writer Name : ")
        library.__category = input(" ->Enter the Category : ")
        library.__book_id = input(" ->Enter the Book ID : ")
        #save to db


    def add_books(self):

        self.ch = 'y'

        while self.ch == 'y' or self.ch == 'yes':

            library.__book_name = input("Enter the Book Name : ")
            print(f"Enter the details of {library.__book_name}")
            library.__publisher_name = input(" ->Enter the Publisher Name : ")
            library.__writer_name = input(" ->Enter the Writer Name : ")
            library.__category = input(" ->Enter the Category : ")
            library.__book_id = input(" ->Enter the Book ID : ")
            #save to db


    def view_book(self):
        #return dictionary
        # view book from db
        pass

    def encrypt(self,book_name = 'all'):
        #encrypt book in db
        pass

    def decrypt(self,book_name = 'all'):
        #decrypt book in db
        pass

    def list_books(self):   #add default values : category = "all", initialized_with = None, list_by = 'author'/'category' etc
        pass


    def delete_book(self, book_name):
        pass

    def delete_books(self):
        #parameters: category,etc
        pass

    def issue_book(self,book_details_list):
        pass

    def details(self, b_list):
        print("details function called...")
        pass