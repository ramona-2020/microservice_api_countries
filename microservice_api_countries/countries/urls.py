from django.urls import path, include

from microservice_api_countries.countries.views import show_countries, country_details, country_update, country_delete

urlpatterns = (
    path('country/', include([
        path('', show_countries, name='show countries'),
        path('<int:pk>/', country_details, name='country details'),
        path('<int:pk>/update/', country_update, name='country update'),
        path('<int:pk>/delete/', country_delete, name='country delete'),
    ])),
)
