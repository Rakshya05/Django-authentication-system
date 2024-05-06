"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from authentication.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Define a custom test for superuser check
'''def is_superuser(user):
    return user.is_authenticated and user.is_superuser'''
def is_user(user):
    return user.is_authenticated


urlpatterns = [
    path('', LoginPage, name='login'),
    path('admin/', admin.site.urls),
    path('signup/', SignupPage, name='signup'),  # Make sure to add a trailing slash for consistency
    path('login/', LoginPage, name='login'),    # Make sure to add a trailing slash for consistency
    # Apply the user_passes_test decorator to restrict access to superusers only
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 9868299624