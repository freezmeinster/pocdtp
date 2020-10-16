from django.contrib import admin
from django.urls import path
from account.views import login_page, dashboard

urlpatterns = [
    path("", login_page, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path('admin/', admin.site.urls),
]
