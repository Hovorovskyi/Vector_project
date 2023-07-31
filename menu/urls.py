from django.urls import path
from .views import MenuItemView


menu_app = 'menu'

urlpatterns = [
    path('', MenuItemView.as_view(), name='menu'),
    path('<str:category>', MenuItemView.as_view(), name='category_menu'),
]