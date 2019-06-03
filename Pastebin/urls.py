from django.urls import include, path
from django.contrib import admin


urlpatterns = [
               path('admin/', admin.site.urls),
               path('', include(('app.urls', 'app'), namespace='app')),
               path('api/', include(('api.urls', 'api'), namespace='api')),
               path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
               ]

