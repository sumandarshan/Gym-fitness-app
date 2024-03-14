from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('workouts/', views.workouts, name='workouts'),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact"),
    path('signup', views.signup, name="signup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('enroll', views.enroll, name="enroll"),
    path('workoutlog', views.workoutlog, name="workoutlog"),
    path('profile', views.profile, name="profile"),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('workout', views.workout, name="workout")
]
