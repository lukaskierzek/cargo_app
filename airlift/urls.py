from django.urls import path
from . import views

app_name = 'airlift'

urlpatterns = [
    path(
        '',
        views.index_view,
        name='index_view'
    ),
    path(
        'destinations/',
        views.DestinationsListViews.as_view(),
        name='destinations'
    ),
    path(
        'destinations/<int:pk>',
        views.DestinationsDetailView.as_view(),
        name='destinations_detail'
    ),
    path(
        'aircrafts/',
        views.AircraftsListViews.as_view(),
        name='aircrafts'
    )
]
