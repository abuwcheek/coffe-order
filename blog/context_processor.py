from .models import Blog


def index_processor(request):
     blogcontext = Blog.objects.filter(is_active=True, is_fact=False).order_by('?')


     context = {
          'blogcontext': blogcontext,
     }

     return context