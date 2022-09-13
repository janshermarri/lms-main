from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from lms_main.views import TeacherViewSet, StudentViewSet, CommentViewSet

router = routers.SimpleRouter()
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'comments', CommentViewSet, basename='comments')
urlpatterns = [
    path('api/', include((router.urls, 'lms_main'))),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
