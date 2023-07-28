from django.views.generic import ListView
from .models import MenuItem


class MenuItemView(ListView):
    model = MenuItem
    template_name = 'menu/menu_list.html'
    context_object_name = 'menu_items'
    allow_empty = False

    def get_queryset(self):
        return MenuItem.objects.filter(category=self.kwargs['category'])