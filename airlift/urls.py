from django.urls import path, include
from . import views

app_name = 'airlift'

# -----Main page----- #
urlpatterns = [
    path(
        '',
        views.index_view,
        name='index_view'
    ),
]

# -----Destinations paths----- #
urlpatterns.extend([
    path(
        'destinations/',
        include([
            path(
                '',
                views.DestinationsListViews.as_view(
                    extra_context={
                        'title': 'destinations',
                    }
                ),
                name='destinations'
            ),
            path(
                '<int:pk>',
                views.DestinationsDetailView.as_view(),
                name='destinations_detail'
            ),
        ])
    ),
])

# -----Aircrafts paths----- #
urlpatterns.extend([
    path(
        'aircrafts/',
        include([
            path(
                '',
                views.AircraftsListViews.as_view(),
                name='aircrafts'
            ),
            path(
                '<int:pk>',
                views.AircraftsDetailView.as_view(),
                name='aircrafts_detail'
            )
        ])
    ),
])

# -----Pilots paths----- #
urlpatterns.extend([
    path(
        'pilots/',
        include([
            path(
                '',
                views.PilotsListViews.as_view(),
                name='pilots'
            ),
            path(
                '<int:pk>',
                views.PilotsDetailView.as_view(),
                name='pilots_detail'
            ),
        ])
    ),
])

# -----Cargos paths----- #
urlpatterns.extend([
    path(
        'cargos/',
        include([
            path(
                '',
                views.CargosListViews.as_view(),
                name='cargos'
            ),
            path(
                '<int:pk>',
                views.CargosDetailViews.as_view(),
                name='cargos_detail'
            ),
        ])
    ),
])
