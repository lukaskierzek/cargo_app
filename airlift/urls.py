from django.urls import path
from . import views

app_name = 'airlift'

urlpatterns = [
    path(
        '',
        views.index_view,
        name='index_view'
    ),
    # path(
    #     'destination/<int:pk>',
    #     views.DestinationsView
    # )
]
