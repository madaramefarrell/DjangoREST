from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import beachs
from django.conf.urls import url

router = DefaultRouter()
router.register(r'beach', beachs.BeachListView, basename='beach')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
