from django.contrib import admin
from django.urls import path, include
from accounts.views import signup, home, login, logout

urlpatterns = [
    path('', home, name="home"),
    path('admin/', admin.site.urls),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('compte/nouveau/', signup, name="signup"),
]
