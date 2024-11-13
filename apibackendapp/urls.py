from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path

#create an instance router of the DefaultRouter class

router = DefaultRouter()


router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)
#creating urls for the login and signup API views
#they are not viewset, the are API views so it should be added to the url pattern list directly
urlpatterns = [
    path("signup/",views.SignupAPIView.as_view(), name="user-signup"),
    path("login/",views.LoginAPIView.as_view(), name="user-login"),
]

urlpatterns = urlpatterns + router.urls
