
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('CarDekho_app.urls')),
    path('account/',include('user_app.api.urls')),
    #path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
