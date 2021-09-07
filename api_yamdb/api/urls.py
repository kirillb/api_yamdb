from django.urls import path, include
from users.views import gen_confirmation_code, gen_access_token

from rest_framework.routers import DefaultRouter

from users.views import UserViewSet

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')


auth_urls = [
    path('signup/', gen_confirmation_code, name='gen_confirmation_code'),
    path('token/', gen_access_token, name='gen_access_token')
]

urlpatterns = [
    path('v1/auth/', include(auth_urls)),
    path('v1/', include(v1_router.urls)),
]
