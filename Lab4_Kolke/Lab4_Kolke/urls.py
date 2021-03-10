from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import Lab_4.urls
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('Lab_4.urls')),
    path('', include('Lab_4.urls')),
    path('api/v1/rest_auth/', include('rest_auth.urls')),
    path('api/v1/rest_auth/registration/', include('rest_auth.registration.urls')),
    path('api/v1/rest_auth/login/', include('rest_auth.registration.urls')),
    ]
