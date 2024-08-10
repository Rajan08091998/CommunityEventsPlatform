from django.urls import path, include

urlpatterns = [
    path("", include("apis.events.urls")),
    path("", include("apis.users.urls"))
]
