from django.shortcuts import render
from datetime import datetime
# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView
from .models import Product
from .filters import ProductFilter


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())

        return context
# Create your views here.
#class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
  #  model = Product
    # Используем другой шаблон — product.html
  #  template_name = 'product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
  #  context_object_name = 'product'
