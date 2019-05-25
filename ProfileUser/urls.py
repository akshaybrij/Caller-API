from django.urls import path,include
from ProfileUser import views

urlpatterns = [
        path('contact/<int:pk>',views.ContactView.as_view(),name='contactview'),
        path('user/',views.UserRegisterView.as_view(),name='user-register'),
        path('contact/',views.SearchView.as_view(),name='contact-search'),
        path('contact/add',views.CreateContactsView.as_view(),name='create-contat'),
        ]
