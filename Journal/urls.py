from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GoalsViewSet, JournalEntriesViewSet, ProgressTrackersViewSet

router=DefaultRouter()
router.register(r'goals', GoalsViewSet, basename='goals')  
router.register(r'journal-entries', JournalEntriesViewSet, basename='journal-entries')
router.register(r'progress-trackers', ProgressTrackersViewSet, basename='progress-trackers')

urlpatterns=[
    path('', include(router.urls))
]