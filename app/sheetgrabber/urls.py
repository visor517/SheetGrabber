from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from grabber.views import OrdersListView, OrderViewSet


router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', OrdersListView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
