from django.urls import path

from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),  
    path('<search/', views.search, name='search'),  

    # Contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),  
    path('contact/create/', views.create, name='create'),  
]
