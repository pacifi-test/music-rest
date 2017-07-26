from django.conf.urls import url, include
from rest_framework import routers

from .views import AutorModelViewSet

router = routers.DefaultRouter()
router.register('autores', AutorModelViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),

]