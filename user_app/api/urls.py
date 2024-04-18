from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_view,loguot_view
from rest_framework_simplejwt.views import MyTokenObtainPairView, MyTokenRefreshView

urlpatterns = [
    path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name='register'),
    path('logout/',loguot_view,name='logout'),
     path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
]
