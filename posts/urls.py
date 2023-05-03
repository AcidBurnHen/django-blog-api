from django.urls import path
from .views import PostList, PostDetail, VerifyEmailView

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('dj-rest-auth/registration/account-confirm-email/<str:key>/', VerifyEmailView.as_view(),  name='account_confirm_email')
]


