from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentViewSet, UserCreateAPIView, DonationCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", PaymentViewSet)

urlpatterns = [
                  path("register/", UserCreateAPIView.as_view(), name="register"),
                  path(
                      "login/",
                      TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
                      name="login",
                  ),
                  path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
                  path("donations/", DonationCreateAPIView.as_view(), name="donations"),
              ] + router.urls
