from django.urls import path

from . import views

urlpatterns=[ path('', views.Home, name='home'),
              path('thankyou', views.Home, name="thank you"),
            ]
