from piston.handler import BaseHandler
from books.models   import Book

class BookHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Book

    def read(self,request, book_id = None):
        base = Book.objects
        if book_id:
            return base.get(pk=book_id)
        else:
            return base.all()

    #def 
