'''
练习题：创建图书馆系统

问题描述：
创建一个图书馆系统，其中包含图书馆、书籍和会员三个类。

    创建一个 Book 类，具有以下属性：
        书名（title）
        作者（author）
        ISBN 号（isbn）

    创建一个 Library 类，具有以下功能：
        初始化方法 __init__(self, name)，用于初始化图书馆名称和一个空的书籍列表。
        方法 add_book(self, book)，接受一个书籍对象，将书籍添加到图书馆中。
        方法 find_book(self, title)，接受书名，查找并返回匹配的书籍对象，如果不存在则返回 None。
        方法 display_books(self)，显示图书馆中所有书籍的信息。

    创建一个 Member 类，具有以下属性：
        姓名（name）
        会员编号（member_id）

    在 Library 类中添加一个方法 borrow_book(self, member, book_title)，接受会员对象和书名，将对应书籍从图书馆中移除并与会员关联。
'''

class Book:
    def __init__(self, title, author, isbn):
        # your code
        pass

class Library:
    def __init__(self, name):
        # your code
        pass
        
    def add_book(self, book):
        # your code
        pass
        
    def find_book(self, title):
        # your code
        pass
    
    def display_books(self):
        # your code
        pass
            
    def borrow_book(self, member, book_title):
        # your code
        pass

class Member:
    def __init__(self, name, member_id):
        # your code
        pass
    

# 创建图书馆实例
library = Library("Central Library")

# 创建书籍实例
book1 = Book("Python Programming", "John Smith", "123456")
book2 = Book("Introduction to Algorithms", "Thomas Cormen", "789012")

# 添加书籍到图书馆
library.add_book(book1)
library.add_book(book2)

# 创建会员实例
member = Member("Alice", "A001")

# 显示图书馆中的书籍
library.display_books()

# 借书
library.borrow_book(member, "Python Programming")
library.display_books()  # 显示更新后的书籍列表



# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn

# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []  # 使用列表来存储图书馆中的书籍
        
#     def add_book(self, book):
#         self.books.append(book)
        
#     def find_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#         return None
    
#     def display_books(self):
#         print(f"Books in {self.name} library:")
#         for book in self.books:
#             print(f"{book.title} by {book.author}")
            
#     def borrow_book(self, member, book_title):
#         book = self.find_book(book_title)
#         if book:
#             self.books.remove(book)
#             member.borrowed_books.append(book)
#             print(f"{member.name} borrowed '{book.title}'.")
#         else:
#             print(f"'{book_title}' not found in the library.")

# class Member:
#     def __init__(self, name, member_id):
#         self.name = name
#         self.member_id = member_id
#         self.borrowed_books = []