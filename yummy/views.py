from django.shortcuts import render
from .models import Dish, DishCategory


def main(request):
    categories = DishCategory.objects.filter(is_visible=True)

    context = {
        'categories': categories,
    }

    return render(request, 'yummy_main.html', context=context)
