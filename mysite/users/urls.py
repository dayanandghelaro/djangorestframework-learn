from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from users.views import TokenView, RegisterUserView


urlpatterns = [
    path('login/', TokenView.as_view(), name='token'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterUserView.as_view(), name="register"),
]