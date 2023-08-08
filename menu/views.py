from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import MenuItem
from .forms import MenuItemForm


class MenuItemView(ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItem.objects.all()


class MenuItemCategoryView(ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_items'
    allow_empty = False

    def get_queryset(self):
        return MenuItem.objects.filter(category=self.kwargs['category'])


def add_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('home')
    else:
        form = MenuItemForm()
    return render(request, 'menu/add_menu_item.html', {'form': form})

