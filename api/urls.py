from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('intro/', views.Intro,name="intro"),
    path('reg/', views.Reg_view.as_view(),name="reg"),
    path('', views.Notes.as_view(),name="notes"),
    path('shared/', views.Shared.as_view(),name="share"),
    # path('shared/<int:id>/', views.Sharedurl.as_view(),name="shareurl"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]