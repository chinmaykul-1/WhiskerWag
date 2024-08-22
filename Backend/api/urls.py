from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, AppointmentViewSet,check_doctor_status,GetInfo,GetUserById,GetDoc,GetUserInfo,ProfileUpdateView

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
router2 = DefaultRouter()
router2.register(r'profile', ProfileUpdateView, basename='profile')
# router2 = DefaultRouter()
# router2.register(r'doctors', DoctorViewSet)
urlpatterns = [
    # path('posts/',views.CreateUserView.as_view(),name='post-list'),
    path('posts/',views.PostListCreate.as_view(),name='post-list'),
    path('posts/delete/<int:pk>/',views.PostDelete.as_view(),name='delete-post'),
    path('petpal/blogs/',views.PetPalAV.as_view(),name='petpal-list'),
    path('petpal/blogs/delete/<int:pk>/',views.PetPalDeleteAV.as_view(),name='delete-petpal'),
    path('', include(router.urls)),
    path('check-doctor-status/', check_doctor_status),
    path('get_info/', GetInfo.as_view()),
    path('get_user/<int:pk>/', GetUserById.as_view()),
    path('get_doc/', GetDoc.as_view()),
    path('get_user/', GetUserInfo.as_view()),
    # path('profile/', ProfileUpdateView.as_view() ), 
    # path('get_doctors/', DoctorViewSet.as_view()),
     path('', include(router2.urls)),
    
]
