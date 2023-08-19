from django.urls import path
from .views import MenuItemView, MenuItemCategoryView, add_item


menu_app = 'menu'

urlpatterns = [
    path('', MenuItemView.as_view(), name='menu'),
    path('<str:category>', MenuItemCategoryView.as_view(), name='category_menu'),
    path('add-item/', add_item, name='add_item'),
]