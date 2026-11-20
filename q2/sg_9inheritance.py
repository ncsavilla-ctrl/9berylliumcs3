class Publication: # This defines a method named display_info that belongs to the class.
    def __init__(self, title, author): # This is a constructor that runs whenever a Publication object is created
        self.__title = title  # This stores the title
        self.__author = author # This stores the author

    def get_title(self, title): # This is a getter method that returns the title of the publication
        return self.__title

    def get_author(self, author): # This is a getter method that returns the author of the publication
        return self.__author 

    def set_title(self, title): # This is a setter method that changes the title of the publication
        self.__title = title

    def set_author(self, author): # This is a setter method that changes the author of the publication
        self.__author = author

    def display_info(self):  # This is a method that displays the title and author of the publication
        print(f"Title: {self.__title}") # This prints the title of the publication
        print(f"Author: {self.__author}") # This prints the author of the publication

class Book(Publication): # This creates a child class Book that inherits from publication
    def __init__(self, title, author, number_of_pages): # This is a constructor for the book class
        super().__init__(title, author) # The calls the constructor of the parent class to initialize title and author
        self.__number_of_pages = number_of_pages # This stores the number of pages in a private attribute

    def get_number_of_pages(self, number_of_pages): # This is a getter method that returns the number of pages
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages): # This is a setter method that changes the number of pages
        if number_of_pages > 0: # This means that the number of pages must be positive
          self.__number_of_pages = number_of_pages # This stores the number of pages in a private attribute
        else: # If the number of pages is negative this will be the result
          print("The number of pages must be positive") # A negative number of pages will print this
        
    

class Magazine(Publication): # This creates a child class Magazine that inherits from publication
    def __init__(self, title, author, issue_number): # This is a constructor for the magazine class
        super().__init__(title, author) # The calls the constructor of the parent class to initialize title and author
        self.__issue_number = issue_number # This stores the issue number in a private attribute

    def get_issue_number(self, issue_number):  # This is a getter method that returns the issue number
        return self.__issue_number 

    def set_issue_number(issue_number): # This is a setter method that changes the issue number
        if issue > 0:  # This means that the issue number must be positive
          self.__issue_number = issue_number # This stores the issue number in a private attribute
        else: # If the issue number is negative this will be the result
          print("The issue number must be positive")  # A negative number of pages will print this




pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information: ")
pub1.display_info()

print("\nBook Information: ")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_number_of_pages())

print("\nMagazine Information: ")
mag1.display_info()
print(mag1.get_issue_number())
