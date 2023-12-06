from django.shortcuts import render, redirect
from .models import Dish, DishCategory
from django.views.generic import TemplateView
from .forms import ReservationForm
from django.contrib import messages

# def main(request):
#     categories = DishCategory.objects.filter(is_visible=True)
#     context = {
#         'categories': categories,
#     }
#     return render(request, 'yummy_main.html', context=context)


class IndexPage(TemplateView):
    template_name = 'yummy_main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        context['categories'] = categories
        context['reservation_form'] = ReservationForm()
        return context

    def post(self, *args, **kwargs):
        reservation_form = ReservationForm(self.request.POST)

        if reservation_form.is_valid():
            reservation_form.save()
            messages.success(self.request, 'Reservation done')
            return redirect('/')

        context = self.get_context_data()
        context['reservation_form'] = reservation_form
        messages.error(self.request, 'Errors in form Reservation')
        return render(self.request, self.template_name, context=context)





