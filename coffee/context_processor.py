from .models import CoffeeModel, OrderModel, Testimonals


def index_processor(request):
          coffees = CoffeeModel.objects.all()
          solo_coffee = CoffeeModel.objects.filter(is_active=True, is_popular=True).order_by('-created_at')[:1]
          testimonals = Testimonals.objects.all()
          orders = OrderModel.objects.all()

          
          context = {
               'coffees': coffees,
               'testimonals': testimonals,
               'orders': orders
          }
          return context