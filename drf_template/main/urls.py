from django.urls import path

from main.views import HelloView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
]