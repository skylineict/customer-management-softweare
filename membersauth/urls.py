from django.urls import path
from .views import Registrationsview, Usernamenamevelidation, Emailvelidation, AccountActivation, UserLogin
from dashapp .views import Searchexpens
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path("register/", Registrationsview.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path("activate/<uidb64>/<token>",
         AccountActivation.as_view(), name="activate"),
    path("username-validation", csrf_exempt(Usernamenamevelidation.as_view()),
         name="username-validate"),
    # my email url for email validation
    path("email-validation", csrf_exempt(Emailvelidation.as_view()),
         name="email-validate"),

     path("SearchText-expenses", csrf_exempt( Searchexpens.as_view()),
         name="SearchText"),
    #     path('password-validation/', csrf_exempt(Passwordvelidation.as_view()),
    #          name="password-validation")

 


]
