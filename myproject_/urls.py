"""
URL configuration for myproject_ project.

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
from django.urls import include, path
from menu.views import t_parfum, ubp, hapus_p
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from myproject_ import settings

urlpatterns = [
    path('', include('menu.urls')),
    path('admin/', admin.site.urls),
    path('t_parfum/', t_parfum),
    path('ubps/ubah/<int:id_produk>', ubp, name="ubp"),
    path('parfum/hapus/<int:id_produk>', hapus_p, name="hapus_p"),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
