"""
    Class Name   : BookStoreClass
    Description     : Stores book details and counts number of books
                      using class variable.
    Input           : Book Name, Author Name
    Output          : Displays book details with total number of books
    Author          : Shweta Narayan Gogawale
    Date            : 2026-02-01
"""

class BookStore:
    NoOfBooks = 0   # Class variable

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name, "by", self.Author,
              ". No of books:", BookStore.NoOfBooks)


# Example usage
Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()