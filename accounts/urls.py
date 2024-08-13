from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

class CustomLogoutView(auth_views.LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'),
]
