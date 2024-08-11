from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
ok = JsonResponse({"ok": True})
urlpatterns = [
    path('ht/', lambda x: ok),
    path('/', lambda x: ok),
    path('admin/', admin.site.urls),
    path('api/', include('apis.urls')),
]
