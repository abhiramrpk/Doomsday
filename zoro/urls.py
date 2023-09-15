"""zoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path, re_path
from stream import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from stream.forms import UserLoginForm, CustomPasswordChangeForm, CustomPasswordResetForm

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$',views.base, name='base'),
    #re_path(r'^home/$',views.home, name='home'),
    #re_path(r'^list/$',views.list, name='list'),
    re_path(r'^signup/$',views.signup, name='signup'),
    re_path(r'^accounts/',include('django.contrib.auth.urls')),
    re_path(r'^login/$',auth_views.LoginView.as_view(authentication_form=UserLoginForm),name='login'),
    #re_path(r'^password_change/$',auth_views.PasswordChangeView.as_view(form_class=CustomPasswordChangeForm),name='password_change'),
    #re_path(r'^password_reset/$',auth_views.PasswordResetView.as_view(form_class=CustomPasswordResetForm),name='password_reset'),
    # re_path(r'^profile/$',views.profile, name='profile'),
    re_path(r'^index/$',views.index, name='index'),
    re_path(r'^leader/$',views.leader, name='leader'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)