from django.urls import path, include
from users.views import obtain_confirmation_code, obtain_auth_token

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')


auth_urls = [
    path('signup/', obtain_confirmation_code, name='gen_confirmation_code'),
    path('token/', obtain_auth_token, name='gen_token')
]

urlpatterns = [
    path('v1/auth/', include(auth_urls)),
    path('v1/', include(v1_router.urls)),
]
