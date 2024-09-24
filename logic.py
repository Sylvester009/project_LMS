class Book:
    def __init__(self, title: str, author: str, publish_year: int, isbn: str = None):
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.isbn = isbn
        
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "publish_year": self.publish_year,
            "isbn": self.isbn
        }
        
