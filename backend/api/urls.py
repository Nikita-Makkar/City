from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from api.views import SmokeViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(r'smokes', SmokeViewSet)

urlpatterns = [
    # Создание и удаление токена.
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'', include(router_v1.urls)),
]
