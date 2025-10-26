from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoalsViewSet, JournalEntriesViewSet, ProgressTrackersViewSet, registerUserView
from rest_framework.authtoken import views as drf_views

router=DefaultRouter()
router.register(r'goals', GoalsViewSet, basename='goals')  
router.register(r'journal-entries', JournalEntriesViewSet, basename='journal-entries')
router.register(r'progress-trackers', ProgressTrackersViewSet, basename='progress-trackers')

urlpatterns=[
    path('', include(router.urls)),
    path('register/', registerUserView.as_view(), name='signup'),# Added registration endpoint
    path('login/', drf_views.obtain_auth_token, name='login'),# Added login endpoint
]