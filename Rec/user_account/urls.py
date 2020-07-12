from django.contrib import admin
from django.urls import path, include
from user_account import views
from menu import views as menu_view


urlpatterns = [
    path('', menu_view.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret2/', views.SecretPage.as_view(), name='secret2'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
