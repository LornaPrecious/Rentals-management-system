"""
URL configuration for apartmentManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from userAccount import views as v

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import(
      PasswordResetView,
      PasswordResetDoneView,
      PasswordResetConfirmView,
      PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('home/', include("main.urls")),
    path('aboutus/', include("main.urls")),
    path('contactus/', include("main.urls")),
    path('apartments/', include("main.urls")),
    path('apartment-details/', include("main.urls")),
        
    path('register/', v.register, name ='register'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('login/', v.custom_login, name='login'), 
    path('logout/', v.signout, name='signout'), 
    path('activate/<uidb64>/<token>', v.activate, name='activate'),

    path('password-reset/', PasswordResetView.as_view(
           template_name='registration/password_reset_form.html',
           html_email_template_name='registration/password_reset.html'
           ),
           name='password-reset'), 
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
            #email_template_name='passwordConfirmation.html'
            ),
            name='password_reset_complete'),

]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    #path('logout/', LogoutView.as_view(next_page='login'),name='logout'),


