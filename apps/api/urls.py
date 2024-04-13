from django.urls import path
from .views import AuthorAPIView, AuthorGenericAPIView
from django.urls import include
from .views import AuthorViewSet, EntryViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register(r'authors_viewset', AuthorViewSet, basename='authors-viewset')
router_entry = DefaultRouter()
router_entry.register(r'entrys_viewset', EntryViewSet, basename='entrys-viewset')


urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorAPIView.as_view(), name='author-detail'),
    path('authors_generic/', AuthorGenericAPIView.as_view(), name='author-generic-list'),
    path('authors_generic/<int:pk>/', AuthorGenericAPIView.as_view(), name='author-generic-detail'),
    path('', include(router.urls)),
    path('', include(router_entry.urls)),
]

