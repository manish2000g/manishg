from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard),
    path('all_orders',views.all_orders),
    path('delete_order/<int:delete_id>',views.delete_order),
    path("deliver/<int:id>", views.delivered),
    path("pending/<int:id>", views.pending)


]