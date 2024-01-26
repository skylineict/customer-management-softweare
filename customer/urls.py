"""customer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashapp.urls')),
    # path('userauth/', include('membersauth.urls')),
    path('contactus/', include('contactus.urls')),
    path("userauth/", include('django.contrib.auth.urls')),
    path('usersetting', include('userssetting.urls')),
    path('membersauth/', include('membersauth.urls')),
    path('email', include('bulkemail.urls')),
    path('news/', include('newsletter.urls')),
    path('', include('incomeapp.urls')),
    path('chart/',include('chart.urls')),
    path('forget/', include('credentail.urls')),
    path('incomesummary/', include('incomesummary.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
