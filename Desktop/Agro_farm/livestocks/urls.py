from django.urls import path
from . import views



urlpatterns = [
    path('homepage', views.homepage),
    path('category_form', views.category_form),
    path('get_category', views.get_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('update_category/<int:category_id>', views.category_update_form),

    path('livestock_form', views.livestock_form),
    path('get_livestock', views.get_livestock),
    path('delete_livestock/<int:livestock_id>', views.delete_livestock),
    path('update_livestock/<int:livestock_id>', views.livestock_update_form),

    path('get_category_user', views.show_categories),
    path('get_livestock_user', views.show_livestocks),
    path('checklist', views.checklist),
    path('add_to_cart/<int:livestock_id>',views.add_to_cart),
    path('mycart', views.show_cart_items),

]