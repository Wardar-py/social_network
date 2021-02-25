"""social_network URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('images/', include('images.urls', namespace='images')),
#     #отредактируйте файл
# /etc/hosts и добавьте следующую строку:
# 127.0.0.1 mysite.com
# Это укажет вашему компьютеру, что при обращении к mysite.com необходимо использовать адрес 127.0.0.1. Если вы пользуетесь Windows, сделайте то же
# самое. Файл находится в C:\Windows\System32\Drivers\etc\hosts.
# Для того чтобы проверить, что домен настроен на нужный адрес, запустите сервер командой pythonmanage.pyrunserver и откройте страницу http://mysite.
# com:8000/account/login/. Вы должны будете увидеть ошибку:
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)