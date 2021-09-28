from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


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
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    path('order_form/<int:livestock_id>/<int:cart_id>', views.order_form),
    path('esewa_verify', views.esewa_verify),
    path('my_order', views.my_order),

    path('password_change_user', auth_views.PasswordChangeView.as_view(
        template_name='livestocks/password_change.html')),
    path('password_change_done_user', auth_views.PasswordChangeView.as_view(
        template_name='livestocks/password_change_done.html'), name='password_change_done')


]