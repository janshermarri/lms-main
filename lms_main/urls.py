from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from lms_main.views import TeacherStudentSessionViewSet, TeacherViewSet, StudentViewSet, CommentViewSet, MyTokenObtainPairView

router = routers.SimpleRouter()
router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'sessions', TeacherStudentSessionViewSet, basename='comments')
urlpatterns = [
    path('api/', include((router.urls, 'lms_main'))),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
