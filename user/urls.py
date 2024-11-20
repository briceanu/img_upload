from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CreateListUserAPI


# Create a router and register the viewset with it
router = DefaultRouter()
router.register(r'user', CreateListUserAPI)

# Use the router's URLs
urlpatterns = router.urls