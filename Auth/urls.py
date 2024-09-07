from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('new_token/', TokenObtainPairView.as_view(), name='novo token'),
    path('refresh_token/', TokenRefreshView.as_view(), name="atualizar token"),
    path('verify_token/', TokenVerifyView.as_view(), name="verificar token"),
]
