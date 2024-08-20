from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup_view,name='signup_page'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/edit',views.edit_view,name='profile_edit'),
]