from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('fe7.api.urls'))
]
