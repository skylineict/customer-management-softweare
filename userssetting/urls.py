from django.urls import path
from .views import UserSetting


urlpatterns = [
    path('', UserSetting.as_view(), name="userstting")

]
