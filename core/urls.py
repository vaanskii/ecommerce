from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html", authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
