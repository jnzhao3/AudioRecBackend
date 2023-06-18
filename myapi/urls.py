from django.urls import include, path
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register(r'recordings', views.RecordingAPIView.as_view())

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('recordings/', views.RecordingAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('/',view.BaseAPIView.as_view())
]