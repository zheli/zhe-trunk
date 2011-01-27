from piston.handler import BaseHandler
from books.models   import Book, Author

class BookHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    fields = ('title', 'publication_date', ('authors', ('first_name', 'last_name')), 'publisher')
    model = Book

    def read(self,request, book_id = None):
        base = Book.objects

        if book_id:
            return base.get(pk=book_id)
        else:
            return base.all()

    def create(self, request):
        if request.content_type:
            data = request.data

            em = self.model(title = data['title'], authors=data['authors'], publisher=data['publisher'], publication_date = data['publication_date'])
            em.save()

            return rc.CREATED

class AuthorHandler(BaseHandler):
    allowed_methods = ('GET', 'POST',)
    fields = ('first_name', 'last_name', 'email')
    model = Author

    def read(self, request):
        base = Author.objects
        return base.all()

    def create(self, request):
        print request.data
        if request.content_type:
            data = request.data
            print data
            em = self.mode(first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'])
            em.save()

            return rc.CREATED
