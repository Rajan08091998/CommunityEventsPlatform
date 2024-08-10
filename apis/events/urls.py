from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apis.events.views import EventViewSet

router = SimpleRouter()
router.register(r'v1/events', EventViewSet, 'events_v1')

urlpatterns = [
    path('', include(router.urls)),
]
