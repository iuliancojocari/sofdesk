from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import SignupViewSet

router = routers.SimpleRouter()
router.register(r"signup", SignupViewSet, basename="signup")

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + router.urls
