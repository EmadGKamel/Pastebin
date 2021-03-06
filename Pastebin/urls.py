from rest_framework.authtoken import views as auth_views
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
               path('admin/', admin.site.urls),
               path('api/', include(('api.urls', 'api'), namespace='api')),
               path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
               path('api-token-auth/', auth_views.obtain_auth_token),
               path('', include(('app.urls', 'app'), namespace='app')),
               ]


