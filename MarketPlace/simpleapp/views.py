from django.shortcuts import render
from datetime import datetime
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Product


class ProductsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = ['-price']
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 1
    #def get(self, request):
    #    products = Product.objects.order_by('-price')
    #    p = Paginator(products, 1)

     #   products = p.get_page(request.GET.get('page', 1))

      #  data = {
       #     'products': products,
        #}

        #return render(request, 'products.html', data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None

        return context
# Create your views here.
#class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
  #  model = Product
    # Используем другой шаблон — product.html
  #  template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
  #  context_object_name = 'product'
