from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter,SimpleRouter
from api.views import beachs

router = SimpleRouter()
router.register(r'beach', beachs.BeachListView, basename='beach')
print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
