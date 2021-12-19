from django.contrib import admin
from django.urls import path, include
from drivers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('driver/', include([
        path('', views.read_driver, name='read_driver'),
        path('create/', views.create_driver, name="create_driver"),
        path('update/<int:driver_id>/', views.update_driver, name="update_driver"),
        path('delete/<int:driver_id>/', views.delete_driver, name="delete_driver"),
    ])),
    path('autopark/', include([
        path('', views.read_autopark, name='read_autopark'),
        path('create/', views.create_autopark, name="create_autopark"),
        path('update/<int:autopark_id>/',
             views.update_autopark, name="update_autopark"),
        path('delete/<int:autopark_id>/',
             views.delete_autopark, name="delete_autopark"),
    ])),
    path('report/', views.report, name="report"),
]
