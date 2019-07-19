from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hvset2')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
router.register('post',views.PostViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login', views.UserLoginApiView.as_view()),
    path('hv2/', views.HelloApiView2.as_view()),
    path('', include(router.urls)),
]
