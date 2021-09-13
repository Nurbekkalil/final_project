from django.urls import path
from . import views
urlpatterns = [
    path('auth/', views.OTPViews.as_view()),
    path('confirm/', views.OTPConfirmView.as_view()),

]