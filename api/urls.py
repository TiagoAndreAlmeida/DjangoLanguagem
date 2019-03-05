from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('languagem', views.LanguagemViews)

urlpatterns = [
    path('index', router.register),
    path('', include(router.urls)),
]
