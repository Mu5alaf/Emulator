from django.urls import path
from . import views

app_name = 'home' 

urlpatterns = [
    path('', views.home_view, name='home_page'),
    path('upload/', views.upload_app, name='upload_app'),
    path('run/<int:id>/', views.run_app, name='run_app'),
    path('apk_info/<int:id>/', views.app_info, name='apk_info'),
    path('change-language/', views.change_language, name='change_language'),
]