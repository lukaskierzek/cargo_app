from django.urls import path, include

from . import views

app_name = 'airlift'

# region Main page

urlpatterns = [
    path('', views.index_view, name='index_view')
]

# endregion


# region Destinations paths

urlpatterns.extend([
    path(
        'destinations/',
        include([
            path('', views.DestinationsListViews.as_view(extra_context={'title': 'destinations'}), name='destinations'),
            path('<int:pk>', views.DestinationsDetailView.as_view(), name='destinations_detail'),
            path('<int:pk>/update', views.DestinationsUpdate.as_view(), name='destinations_update')
        ])
    ),
])

# endregion


# region Aircrafts paths

urlpatterns.extend([
    path(
        'aircrafts/',
        include([
            path('', views.AircraftsListViews.as_view(), name='aircrafts'),
            path('<int:pk>', views.AircraftsDetailView.as_view(), name='aircrafts_detail'),
            path('<int:pk>/update', views.AircraftsUpdate.as_view(), name='aircrafts_update')
        ])
    ),
])

# endregion


# region Pilots paths

urlpatterns.extend([
    path(
        'pilots/',
        include([
            path('', views.PilotsListViews.as_view(), name='pilots'),
            path('<int:pk>', views.PilotsDetailView.as_view(), name='pilots_detail'),
            path('<int:pk>/update-basic-information', views.PilotsUpdate.as_view(), name='pilots_update'),
            path('<int:pk>/update-additional-information', views.PilotsInformationsUpdate.as_view(),
                 name='pilots_informations_update')
        ])
    ),
])

# endregion


# region Cargos paths

urlpatterns.extend([
    path(
        'cargos/',
        include([
            path('', views.CargosListViews.as_view(), name='cargos'),
            path('<int:pk>', views.CargosDetailViews.as_view(), name='cargos_detail'),
            path('<int:pk>/update', views.CargosUpdate.as_view(), name='cargos_update')
        ])
    ),
])

# endregion


# region Dashboard paths

urlpatterns.extend([
    path(
        'dashboard/',
        include([
            path('', views.dashboard_views, name='dashboard')
        ])
    ),
])

# endregion
