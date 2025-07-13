class Book:
    def __init__(self, title, author,):
       self.title = title
       self.author = author
       self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books=[]

    def borrow_book(self,book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
             self.borrowed_books.append(book)
            return f"Successfully borrowed '{book.title}' by '{book.author}'"
        else:
            return f"Book {book.title} is already borrowed"

    def return_book(self,book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            return f"Successfully returned '{book.title}'"
        else:
            return f"You haven't borrowed '{book.title}'"

    def list_borrowed_books(self):
        if not self.borrowed_books:
            return f"You haven't borrowed any books"
        return [book.title for book in self.borrowed_books]

if __name__ == "__main__":
    book1=Book("The Kite Runner","Khaled Hosseini")
    book2=Book("The Forty Rules of Love","Elif Shafak")
    book3=Book("Life Above All","Allan Stratton")

    member_name=input("Enter name: ")
    member_id=int(input("Enter ID: "))
    member=LibraryMember(member_name,member_id)

    while True:
       print("\nLibrary Management System")
       print("1.Borrow book")
       print("2.Return book")
       print("3.List borrowed book")
       print("4.Exit")

       choice=input("Enter your choice: ")

       if choice== "1":
              print("Available books: ")
              books=[book1, book2, book3]
              for i, book in enumerate(books,1):
                  status="(Available)" if not book.is_borrowed else "(Borrowed)"
                  print(f"{i}. {book.title} by {book.author}{status}")

              book_choice=input("Enter your choice: ")
              try:
                selected_book=books[int(book_choice)-1]
                print(member.borrow_book(selected_book))
              except (ValueError, IndexError):
                print("Invalid choice")

        elif choice== "2":
              borrowed=member.list_borrowed_books()
              if not borrowed or isinstance(borrowed,str):
                print(borrowed)
          else:
              print("\nBooks borrowed: ")
              for i, title in enumerate(borrowed ,1):
                 print(f"{i}. {title}")
              return_choice=input("Enter book to return: ")

              try:
                selected_book=member.borrowed_books[int(return_choice)-1]
                print(member.return_book(selected_book)
               except(ValueError, IndexError):
                   print("Invalid choice")

        elif choice =="3":
            borrowed=member.list_borrowed_books()
            if isinstance(borrowed,list):
               print("\nBooks borrowed: ")
               for i, title in enumerate(borrowed,1):
                   print(f"{i}. {title}")
            else:
              print(borrowed)

        elif choice =="4":
            print("Goodbye")
            break

        else:
         print("Invalid choice.Enter a number between 1 and 4")
