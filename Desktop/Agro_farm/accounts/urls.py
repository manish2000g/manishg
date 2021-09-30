from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('', views.homepage),
    path('login', views.login_user),
    path('signup', views.signup_user),
    path('logout', views.logout_user),
    path('admins/users',views.get_users),
    path('admins/admins', views.get_admins),
    path('promote_user/<int:user_id>', views.promote_user),
    path('demote_user/<int:user_id>', views.demote_user),
    path('profile', views.profile),
    path('deactivate_user/<int:user_id>', views.deactivate_user),
    path('deactivate_admin/<int:user_id>', views.deactivate_admin),
    path('activate_user/<int:user_id>', views.activate_user),
    path('activate_admin/<int:user_id>', views.activate_admin),

    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),

]